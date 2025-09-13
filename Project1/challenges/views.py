from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

challenges = {
    'january': 'This is January month',
    'february': 'This is February month',
    'march': 'This is March month',
    'april': 'This is April month',
    'may': 'This is May month',
    'june': 'This is June month',
    'july': 'This is July month',
    'august': 'This is August month',
    'september': 'This is September month',
    'october': 'This is October month',
    'november': 'This is November month',
    'december': 'This is December month',
}

def index(request):
    months = list(challenges.keys())
    lst = ''       
    for month in months:
        month_path = reverse("month-challenge", args=[month])
        lst += f'<li><a href="{month_path}">{month.capitalize()}</a></li>'
    return HttpResponse(f'<ul>{lst}</ul>')

def challenge_by_no(request, month):
    months = list(challenges.keys())
    if month > len(months) or month < 1:
        return HttpResponseNotFound("This month is not supported")
    else:
        redirect_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)

def challenge(request, month):
    try:
        return render(request, "challenges/challenge.html")
    except:
        return HttpResponseNotFound("This month is not supported")
