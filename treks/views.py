import string
import json
from datetime import date, datetime, timedelta

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.core import serializers
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import Trek
from .forms import TrekForm, ReqForm
from profiles.models import Message

@login_required
def post(req):
    if req.method != 'POST':
        raise Http404

    form = TrekForm(req.POST)
    try:
        trek = form.save(commit=False)
        trek.driver = req.user
        trek.from_city = string.capwords(trek.from_city)
        trek.to_city = string.capwords(trek.to_city)
        trek.from_state = trek.from_state.upper()
        trek.to_state = trek.to_state.upper()
        trek.save()
    except ValueError:
        print('notvalid')
    return redirect('browse')

@login_required
def offer(req, rid):
    if req.method != 'POST':
        raise Http404

    rqst = Request.objects.get(pk=rid)

@login_required
def request_trek(req):
    if req.method != 'POST':
        raise Http404

    form = ReqForm(req.POST)
    try:
        rqst = form.save(commit=False)
        rqst.passenger = req.user
        rqst.from_city = string.capwords(rqst.from_city)
        rqst.to_city = string.capwords(rqst.to_city)
        rqst.from_state = rqst.from_state.upper()
        rqst.to_state = rqst.to_state.upper()
        rqst.save()
    except ValueError:
        print('ohno')
    return redirect('browse')

@csrf_exempt
def view_all(req):
    if req.method != 'POST':
        raise Http404
    query = Trek.objects.filter(date__gt=date.today())
    treks = json.loads(serializers.serialize('json', query))
    for i in range(len(treks)):
        treks[i] = treks[i]['fields']
        treks[i]['seats_taken'] = len(treks[i]['passengers'])
    return HttpResponse(json.dumps(treks), content_type='application/json')

@csrf_exempt
def view_some(req):
    if req.method != 'POST':
        raise Http404

    data = req.POST.dict()
    src = data['src']
    dst = data['dst']
    from_city = src.split(', ')[0] if src != '' else ''
    from_state = src.split(', ')[1] if src != '' else ''
    to_city = dst.split(', ')[0] if dst != '' else ''
    to_state = dst.split(', ')[1] if dst != '' else ''
    treks = '[]'
    query = []

    # filter by locations
    if src == '':
        if dst == '':
            query = Trek.objects.filter(date__gt=date.today())
        else:
            query = Trek.objects.filter(date__gt=date.today(),
                                        to_city=to_city, to_state=to_state)
    elif dst == '':
        query = Trek.objects.filter(date__gt=date.today(), from_city=from_city,
                                    from_state=from_state)
    else:
        query = Trek.objects.filter(date__gt=date.today(), from_city=from_city,
                                    from_state=from_state, to_city=to_city,
                                    to_state=to_state)
    # other filters
    if data['date'] != '':
        query = query.filter(date=data['date'])
    if data['dtime'] != '':
        dtime = datetime.strptime(data['dtime'], '%H')
        plusone = dtime + timedelta(hours=1)
        query = query.filter(departure_time__gte=dtime.time(), departure_time__lt=plusone.time())
    if data['org_only'] == 'on':
        query = query.filter(org_only=True)
    if data['mutuals'] == 'on':
        query = query.filter(mutuals_only=True)
    if data['fem_only'] == 'on':
        query = query.filter(fem_only=True)
        
    treks = json.loads(serializers.serialize('json', query))

    for i in range(len(treks)):
        treks[i]['fields']['id'] = treks[i]['pk']
        treks[i] = treks[i]['fields']
        treks[i]['seats_taken'] = len(treks[i]['passengers'])
    return HttpResponse(json.dumps(treks), content_type='application/json')

@login_required
def join(req, trekid):
    if req.method != 'POST':
        raise Http404

    data = req.POST.dict()
    t = Trek.objects.get(pk=trekid)
    if t.driver != req.user:
        if data['seats'] != '':
            t.seats -= int(data['seats'])
        t.passengers.add(req.user)
        dcontent = req.user.first_name + ' has joined your Trek! Here\'s their phone number so you two can get in touch: ' + req.user.profile.phone_number
        rcontent = 'You joined '  + t.driver.first_name + '\'s Trek! Here\'s their phone number so you two can get in touch: ' + t.driver.profile.phone_number
        driver_msg = Message(sender=req.user, receiver=t.driver, content=dcontent)
        rider_msg = Message(sender=t.driver, receiver=req.user, content=rcontent)
        driver_msg.save()
        rider_msg.save()
        if data['msg'] != '':
            msg = Message(sender=req.user, receiver=t.driver, content=data['msg'])
            msg.save()
    return redirect('browse')

@login_required
def delete(req, trekid):
    t = Trek.objects.get(pk=trekid)

    if req.user != t.driver:
        raise Http404
    t.delete()
    return redirect('profile', user=req.user.username)

@login_required
def leave(req, trekid):
    t = Trek.objects.get(pk=trekid)

    if req.user not in t.passengers.all():
        raise Http404
    t.passengers.remove(req.user)
    return redirect('profile', user=req.user.username)

@csrf_exempt
def trek(req, trekid):
    if req.method != 'POST':
        raise Http404

    t = json.loads(serializers.serialize('json', [Trek.objects.get(pk=trekid)]))[0]

    t['fields']['id'] = t['pk']
    t = t['fields']
    t['seats_taken'] = len(t['passengers'])

    return HttpResponse(json.dumps(t), content_type='application/json')
