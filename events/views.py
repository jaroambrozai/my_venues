from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue
from .forms import VenueForm, EventForm
from django.http import HttpResponseRedirect, HttpResponse


def venues_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename = venues.txt'

    # designate the model
    venues = Venue.objects.all().order_by('name')

    # create a blank list
    lines = []

    # lines = [
    #     "This is line 1\n",
    #     "This is line 2\n",
    #     "This is line 2\n",
    # ]

    # for venue in venues:
    #     lines.append(f'{venue.name}\n{venue.address}\n{venue.zip_code}\n{venue.phone}\n'
    #                  f'{venue.web}\n{venue.email_address}\n\n\n')

    for venue in venues:
        if venue.name is not "":
            lines.append(f'{venue.name}\n')
        if venue.address is not "":
            lines.append(f'{venue.address}\n')
        if venue.zip_code is not "":
            lines.append(f'{venue.zip_code}\n')
        if venue.phone is not "":
            lines.append(f'{venue.phone}\n')
        if venue.web is not "":
            lines.append(f'{venue.web}\n')
        if venue.email_address is not "":
            lines.append(f'{venue.email_address}\n')
        lines.append(f'\n\n')

    # write a textfile
    # response.writelines(lines)

    response.writelines(lines)
    return response


def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list-venues')

def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('list-events')

def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list-events')
    return render(request, 'events/update_event.html', {
        'event': event,
        'form': form,
    })


def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_event.html', {'form': form, 'submitted': submitted})


def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list-venues')
    return render(request, 'events/update_venue.html', {
        'venue': venue,
        'form': form,
    })


def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)
        return render(request, 'events/search_venues.html', {
            'searched': searched,
            'venues': venues,
        })
    else:
        return render(request, 'events/search_venues.html', {})

def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'events/show_venue.html', {
        'venue': venue,
    })


def list_venues(request):
    venue_list = Venue.objects.all().order_by('name')
    return render(request, 'events/venue.html', {
        'venue_list': venue_list,
    })


def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_venue.html', {'form': form, 'submitted': submitted})


def all_events(request):
    event_list = Event.objects.all().order_by('event_date')
    return render(request, 'events/event_list.html', {
        'event_list': event_list,
    })


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "Jaro"
    month = month.capitalize()
    # convert month from  name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    year = int(year)

    # create calendar
    cal = HTMLCalendar().formatmonth(year, month_number)

    # get current year
    now = datetime.now()
    current_year = now.year

    # get current time
    current_time = now.strftime('%H:%M %p')
    return render(request, 'events/home.html', {
        "name": name,
        "year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal,
        "current_year": current_year,
        "current_time": current_time,
        })

