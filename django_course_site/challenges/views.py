from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
monthly_challenges = {
    "january": "Eat no meat for the entire month of january",
    "february": "Walk for at least 30 minutes every day in february",
    "march": "Learn Django for at least 1 hour every day in march",
    "april": "Eat no meat for the entire month in april",
    "may": "Walk for at least 30 minutes every day in may",
    "june": "Learn Django for at least 1 hour every day in june",
    "july": "Eat no meat for the entire month",
    "august": "Walk for at least 30 minutes every day",
    "september": "Learn Django for at least 1 hour every day",
    "october": "Eat no meat for the entire month",
    "november": "Walk for at least 30 minutes every day",
    "december": "Learn Django for at least 1 hour every day"
}


def monthly_challenge(request, month):
    print(request)
    try:
        challenge_text = monthly_challenges[month.lower()]
        return HttpResponse(challenge_text)
    except Exception:
        return HttpResponseNotFound("This is not supported")


def monthly_challenge_by_number(request, month):
    print(request)
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    month = months[month - 1]
    return HttpResponseRedirect("/challenges/"+month)
