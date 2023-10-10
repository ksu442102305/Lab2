from django.shortcuts import render

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

people = []  

def add_person(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        new_person = Person(username, password)
        people.append(new_person)
    return render(request, "myapp/add_person.html")

def show_people(request):
     return render(request, "myapp/show_people.html", {"people": people})