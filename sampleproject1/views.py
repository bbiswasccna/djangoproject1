from django.http import HttpResponse
from django.shortcuts import render

def aboutUs(request):
    return render(request,"about.html")

def homePage(request):
    # data = {
    #     "title" : "This is Title",
    #     "description" : "This long text.......",
    #     "clist" : ["PHP","Java", "Python", "Golang"],
    #     "students" : [
    #         {"name":"Abir","phone":"9856457859"},
    #         {"name":"Boni","phone":"9856454125"},
    #         {"name":"Dinesh","phone":"9841257865"},
    #         ],
    #     "numbers" : [10,20,30,40,50,60,80]
    # }
    return render(request,"index.html")

def contactUs(request):
    return render(request,"contact.html")

def userForm(request):
    try:
        n1 = int(request.GET.get('num1'))
        n2 = int(request.GET.get('num2'))
        output = n1+n2
        # print(n1+n2)
    except:
        pass
    return render(request,"userform.html",{'output':output})

def courseDetails(request,courseid):
    return HttpResponse(courseid)