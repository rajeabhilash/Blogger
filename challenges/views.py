from django.shortcuts import render, redirect
from django.urls import reverse
from .data.challenge_list import challenges
import datetime

def get_month_name_from_number(month_number):
    try:
        return datetime.date(2000, month_number, 1).strftime('%B')
    except ValueError:
        return None

def index(request):
    months = list(challenges.keys())

    context = {
        'months': months,
        'page_title': 'Explore Monthly Challenges',
        'current_year': datetime.datetime.now().year
    }
    return render(request, 'challenges/index.html', context)

def month_name_challenge(request, month_name):
    formatted_month_name = month_name.capitalize()
    challenge_data = challenges.get(formatted_month_name)
    if not challenge_data:
         context = {
            'month_name': formatted_month_name,
            'page_title': 'Challenge Not Found',
            'error_message': "The challenge for this month does not exist or is not available."
            }
         return render(request, 'challenges/challenge_not_found.html', context, status=404)
    context = {
        'month_name': formatted_month_name,
        'challenge': challenge_data, # Pass the entire dictionary for the month
        'page_title': f"{formatted_month_name} Challenge"
    }
    return render(request, 'challenges/challenge_detail.html', context)


def month_number_challenge(request, month_number):
    month_name = get_month_name_from_number(month_number)
    
    if not month_name:
        context = {
            'month_name': f"Month number {month_number}",
            'page_title': 'Invalid Month Number',
            'error_message': f"Month number {month_number} is not a valid month."
        }
        return render(request, 'challenges/challenge_not_found.html', context, status=404)
    redirect_url = reverse('challenges:month_name_challenge', args=[month_name.lower()])
    return redirect(redirect_url)