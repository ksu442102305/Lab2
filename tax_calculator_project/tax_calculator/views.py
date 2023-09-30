from django.shortcuts import render
from django.http import HttpResponse


def default(request):
    return HttpResponse("<h1>This is a site to calculate tax.</h1>")


def calculate_tax(request, number):
    tax_rate = 0.15
    try:
        number = float(number)  
        total_price = number * (1 + tax_rate)
        return HttpResponse(f"<h1>Total Price after {tax_rate * 100}% tax: ${total_price:.2f}</h1>")
    except ValueError:
        return HttpResponse("<h1>Invalid input. Please provide a valid number.</h1>")


def tax_rate(request):
    tax_rate = 0.15
    return HttpResponse(f"<h1>Tax Rate: {tax_rate * 100}%</h1>")
