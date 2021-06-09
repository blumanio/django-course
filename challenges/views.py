from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
monthly_challenges = {
    "january": "walk at least 20 minutes every day!",
    "february": "this works",
    "march": "stop drinking coeffe for the entire month",
    "april": "stop drinking coeffe for the entire month!",
    "may": "sleep early before 23:00 for the entire month!",
    "june": "go for a run every morning before starting!",
    "july": "skip breakfast!",
    "august": "learn django for 20 minutes for the entire month!!",
    "september": "learn new language for at least 220 minutes!",
    "october": "write 100 words every day for at least one month!",
    "november": "stop smoking!",
    "december": "don't eat meat for this month!"
}


def index(request):
    return HttpResponse("this works")


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    forward_month = months[month-1]
    return HttpResponseRedirect("/challenges/" + forward_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported")
