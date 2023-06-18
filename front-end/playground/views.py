from django.shortcuts import render
from django.http import HttpResponse

import pyrebase

# Remember the code we copied from Firebase.
# This can be copied by clicking on the settings icon > project settings, then scroll down in your firebase dashboard
config = {
    "apiKey": "AIzaSyBLv1DiRB6egmpaoIKfjODXZF5fYheQKIM",
    "authDomain": "realtimedatabasetest-f226a.firebaseapp.com",
    "databaseURL": "https://realtimedatabasetest-f226a-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "realtimedatabasetest-f226a",
    "storageBucket": "realtimedatabasetest-f226a.appspot.com",
    "messagingSenderId": "348704796176",
    "appId": "1:348704796176:web:b19a37e276fd097a2ce495"
}

# here we are doing firebase authentication
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

def say_hello(request):
    # Accessing the "users" table and retrieving the first 5 records
    users = database.child('users').order_by_child("Email").limit_to_first(5).get()

    user_list = []
    for result in users.each():
        user_data = result.val()
        user_list.append(user_data)

    context = {
        'users': user_list,
    }
    return render(request, 'polyHack/employees_page.html', context)


def go_to_dashboard(request):
    return render(request, 'polyHack/dashboard.html')

def go_to_posts(request):
    return render(request, 'polyHack/posts.html')

def go_to_accounts(request):
    return render(request, 'polyHack/accounts.html')

def create_record(data, table):
    # Push the provided data dictionary as a new record in the database
    new_record = database.child(table).push(data)
    return new_record

# data = {
#     "Name": "Mohammed Alshami",
#     "Email": "mshami2021@gmail.com",
#     "Profession": "Software Engineer",
#     "Phone":"01164504470",
#     "Project": "Data Mining",
#     "KPI": "10.23 / 20",
# }
# new_record_key = create_record(data, "users")
# print("New record created with key:", new_record_key)
