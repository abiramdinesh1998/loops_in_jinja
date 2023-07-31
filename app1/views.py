from django.shortcuts import render

# Create your views here.

def loop(request):
    d = {'name':'dinesh','hobbies':['music','palying pubg']}
    return render(request,'loop.html',context=d)
