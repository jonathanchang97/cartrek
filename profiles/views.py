import json
from datetime import date

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group

from .models import Profile, Organization, Message, Car
from .forms import ProfileForm, MsgForm

from treks.models import Trek

@csrf_exempt
def readmsg(req, m_id):
    if req.method != 'POST':
        raise Http404

    msg = Message.objects.get(pk=m_id)
    msg.read = True
    msg.save()
    return redirect('inbox')

@csrf_exempt
def msg_count(req):
    if req.method != 'POST':
        raise Http404
    data = json.loads(req.body.decode('utf-8'))
    user = User.objects.get(pk=data['user'])
    count = len(Message.objects.filter(receiver=user, read=False))
    return HttpResponse(count, content_type='text/plain')
    
def edit(req):
    if req.method != 'POST':
        raise Http404
    if not req.user.groups.filter(name='adults').exists():
        req.user.groups.clear()
        Group.objects.get(name='adults').user_set.add(req.user)
        print('send verification email') #TODO

    form = ProfileForm(req.POST)
    if form.is_valid():
        newcar = None
        if form.cleaned_data['car_make'] != '' and form.cleaned_data['car_model'] != '' and form.cleaned_data['plate'] != '':
            newcar = Car(make=form.cleaned_data['car_make'],
                         model=form.cleaned_data['car_model'],
                         plate=form.cleaned_data['plate'])
            newcar.save()
        profile = req.user.profile
        profile.hometown = form.cleaned_data['hometown']
        if form.cleaned_data['affiliation'] != None:
            profile.affiliation = Organization.objects.get(name=form.cleaned_data['affiliation'])
        else:
            profile.affiliation = None
        profile.org_email = form.cleaned_data['org_email']
        profile.venmo = form.cleaned_data['venmo']
        profile.major = form.cleaned_data['major']
        profile.phone_number = form.cleaned_data['phone_number']
        profile.car = newcar
        profile.bio = form.cleaned_data['bio']
        profile.save()
    else:
        print('notvalid')
    return redirect('browse')

@csrf_exempt
def profile(req, user):
    if req.method != 'POST':
        raise Http404
    u = User.objects.get(username=user)
    p = serializers.serialize('json', [u.profile])
    driving = Trek.objects.filter(driver=u, date__gt=date.today())
    taking = Trek.objects.filter(passengers__username=user)
    treks = json.loads(serializers.serialize('json', driving | taking))

    for i in range(len(treks)):
        treks[i]['fields']['id'] = treks[i]['pk']
        treks[i] = treks[i]['fields']
        treks[i]['seats_taken'] = len(treks[i]['passengers'])
    try:
        p = json.loads(p)[0]['fields']
    except IndexError:
        raise Http404
    except AttributeError:
        raise Http404

    p['treks'] = treks
    return HttpResponse(json.dumps(p), content_type='application/json')

def sendmsg(req):
    if req.method != 'POST':
        raise Http404

    form = MsgForm(req.POST)
    if form.is_valid():
        sender = User.objects.get(username=form.cleaned_data['sender'])
        receiver = User.objects.get(username=form.cleaned_data['receiver'])
        content = form.cleaned_data['content']
        msg = Message(sender=sender, receiver=receiver, content=content)
        msg.save()
    return redirect('profile', user=receiver)
