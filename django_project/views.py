
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"home.html")

# def contactUs(request):
#     data={
#         "title":"Contact Page",
#         "bdata":"Welcome to Contact Page",
#         "clist":["python","django","java"],
#         "student_details":[
#             {"name":"vikram","mobNo":"123456789"},
#             {"name":"Leo","mobNo":"987654321"}
#         ],
#         "numbers":[10,20,30,40,50]
#     }
#     return render(request,"contact.html",data)

def contact(request):
    return render(request,"Contact.html")

# def aboutUs(request):
#     return HttpResponse("Welcome to django tutorials.....")

def about(request):
    return render(request,"About.html")

def course(request):
    return HttpResponse("you are seeing course.....")

def courseDetails(request,courseId):
    return HttpResponse(courseId)


