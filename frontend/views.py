import requests
import json
from datetime import datetime, date

from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from profiles.models import Organization, Message, Car
from profiles.forms import ProfileForm, MsgForm
from treks.models import Trek, Request
from treks.forms import TrekForm, ReqForm

URL = 'http://localhost:8000/'
#URL = 'https://www.cartrek.us/'

def homepage(req):
    context = {'x': 'Hello Michael'}
    return render(req, 'old_index.html', context=context)

def browse(req):
    # get json (depends on url params)
    context = {}
    post_data = {}
    all_treksjs = requests.post(URL + 'treks/all/').text

    # locations
    if req.GET.get('src') == None:
        context['from'] = 'From'
        if req.GET.get('dst') == None:
            context['to'] = 'To'
            post_data['src'] = ''
            post_data['dst'] = ''
        else:
            context['to'] = req.GET.get('dst')
            post_data['src'] = ''
            post_data['dst'] = req.GET.get('dst')
    elif req.GET.get('dst') == None:
        context['from'] = req.GET.get('src')
        context['to'] = 'To'
        post_data['src'] = req.GET.get('src')
        post_data['dst'] = ''
    else:
        context['from'] = req.GET.get('src')
        context['to'] = req.GET.get('dst')
        post_data['src'] = req.GET.get('src')
        post_data['dst'] = req.GET.get('dst')

    # other filters
    post_data['date'] = req.GET.get('date') if req.GET.get('date') else ''
    post_data['dtime'] = req.GET.get('dtime_range') if req.GET.get('dtime') else ''
    post_data['org_only'] = req.GET.get('org_only') if req.GET.get('org_only') else ''
    post_data['mutuals'] = req.GET.get('mutual') if req.GET.get('mutual') else ''
    post_data['fem_only'] = req.GET.get('gender') if req.GET.get('gender') else ''
    js = requests.post(URL + 'treks/some/', data=post_data).text
    treks = json.loads(js)

    # put actual drivers and passengers in dict (not just id)
    # and render time and date as strings
    # and count seats
    treks = fix_json(treks)

    # collect all sources and destinations
    from_cities = []
    from_states = []
    to_cities = []
    to_states = []
    for t in json.loads(all_treksjs):
        from_cities.append(t['from_city'])
        from_states.append(t['from_state'])
        to_cities.append(t['to_state'])
        to_states.append(t['to_state'])
    
    all_treks = json.loads(all_treksjs)
    sources = [', '.join([t['from_city'], t['from_state']]) for t in all_treks]
    destinations = [', '.join([t['to_city'],  t['to_state']]) for t in all_treks]

    # put together context and render
    context['title'] = 'CarTrek -- Browse'
    context['treks'] = treks
    context['requests'] = Request.objects.filter(date__gt=date.today())
    context['sources'] = set(sources)
    context['destinations'] = set(destinations)
    return render(req, 'browse.html', context=context)

@login_required
def post(req):
    if not req.user.groups.filter(name='adults').exists():
        return redirect('create')
    context = {
        'title': 'CarTrek -- Post a Ride',
        'form': TrekForm(initial={'from_city': '',
                                  'from_state': '',
                                  'to_city': '',
                                  'to_state': '',
                                  'date': '',
                                  'departure_time': '',
                                  'arrival_time': '',
                                 }),
    }
    return render(req, 'post.html', context=context)

@login_required
def request(req):
    if not req.user.groups.filter(name='adults').exists():
        return redirect('create')
    context = {
        'title': 'CarTrek -- Request a Ride',
        'form': ReqForm(initial={'from_city': '',
                                  'from_state': '',
                                  'to_city': '',
                                  'to_state': '',
                                  'date': '',
                                  'departure_time': '',
                                  'arrival_time': '',
                                 }),
    }
    return render(req, 'request.html', context=context)

def blog(req):
    context = {'title': 'CarTrek -- Blog'}
    return render(req, 'blog.html', context=context)

def about(req):
    context = {'title': 'CarTrek -- About'}
    return render(req, 'about.html', context=context)

@login_required
def trek(req, trekid):
    trek = Trek.objects.get(pk=trekid)
    js = requests.post(URL + 'treks/' + str(trekid) + '/').text
    t = fix_json([json.loads(js)])[0]
    context = {
        'title': 'Cartrek',
        't': t,
    }

    if trek.driver == req.user or req.user in trek.passengers.all():
        return redirect('browse')
    return render(req, 'trek.html', context=context)

def profile(req, user):
    if req.user.username == user and not req.user.groups.filter(name='adults').exists():
        return redirect('create')
    # get json
    js = requests.post(URL + 'profiles/' + user + '/').text
    p = json.loads(js)

    # fix json
    if p['affiliation'] != None:
        p['affiliation'] = Organization.objects.get(pk=p['affiliation'])
    if p['car'] != None:
        p['car'] = Car.objects.get(pk=p['car'])
    p['user'] = User.objects.get(pk=p['user'])
    fix_json(p['treks'])

    # render
    context = {
        'title': 'Cartrek -- ' + p['user'].first_name + '\'s profile',
        'profile': p,
    }
    return render(req, 'profile.html', context=context)

@login_required
def create_profile(req):
    if req.user.groups.filter(name='adults').exists():
        return redirect('browse')
    context = {
        'title': 'CarTrek -- Create Profile',
        'organizations': Organization.objects.all(),
        'form': ProfileForm(initial={'phone_number': '',
                                     'org_email': 'none',}),
    }
    return render(req, 'create.html', context=context)

@login_required
def edit_profile(req):
    if req.user.profile.car:
        form = ProfileForm(initial={'hometown': req.user.profile.hometown,
                                    'major': req.user.profile.major,
                                    'phone_number': req.user.profile.phone_number,
                                    'affiliation': req.user.profile.affiliation,
                                    'org_email': req.user.profile.org_email,
                                    'car_make': req.user.profile.car.make,
                                    'car_model': req.user.profile.car.model,
                                    'plate': req.user.profile.car.plate,
                                    'venmo': req.user.profile.venmo,
                                    'bio': req.user.profile.bio})
    else:
        form = ProfileForm(initial={'hometown': req.user.profile.hometown,
                                    'major': req.user.profile.major,
                                    'phone_number': req.user.profile.phone_number,
                                    'affiliation': req.user.profile.affiliation,
                                    'org_email': req.user.profile.org_email,
                                    'venmo': req.user.profile.venmo,
                                    'bio': req.user.profile.bio})
    context = {
        'title': 'CarTrek -- Edit Profile',
        'organizations': Organization.objects.all(),
        'form': form,
    }
    return render(req, 'edit.html', context=context)

@login_required
def inbox(req):
    context = {
        'title': 'CarTrek -- Inbox',
        'msgs_new': Message.objects.filter(receiver=req.user, read=False).order_by('-timestamp'),
        'msgs_old': Message.objects.filter(receiver=req.user, read=True).order_by('-timestamp'),
    }
    for m in context['msgs_new']:
        print(m.timestamp)
    return render(req, 'inbox.html', context=context)

@login_required
def send_msg(req, user):
    context = {
        'title': 'CarTrek -- Send Message',
        'recpt': User.objects.get(username=user),
        'form': MsgForm(initial={'sender': req.user.username,
                                 'receiver': user,
                                }),
    }
    return render(req, 'sendmsg.html', context=context)

def terms(req):
    context = {
        'title': 'CarTrek -- Terms &amp; Conditions',
    }
    return render(req, 'terms.html', context=context)

def privacy(req):
    context = {
        'title': 'CarTrek -- Privacy Policy',
    }
    return render(req, 'privacy.html', context=context)

def login(req):
    context = {
        'title': 'CarTrek',
    }
    return render(req, 'login.html', context=context)

def fix_json(treks):
    for t in treks:
        t['driver'] = User.objects.get(pk=t['driver'])
        for i in range(len(t['passengers'])):
            t['passengers'][i] = User.objects.get(pk=t['passengers'][i])
        dtime = datetime.strptime(t['departure_time'].split('.')[0], '%H:%M:%S').time()
        atime = datetime.strptime(t['arrival_time'].split('.')[0], '%H:%M:%S').time()
        date = datetime.strptime(t['date'], '%Y-%m-%d').date()
        t['departure_time'] = dtime.strftime('%I:%M%p')
        t['arrival_time'] = atime.strftime('%I:%M%p')
        t['date'] = date.strftime('%a %b %d')

    return treks
