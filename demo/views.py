from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
 
#check which checkbox is on
def analyze(request):
    djangotext = request.POST.get('text','default')
    removingpunc = request.POST.get('removingpunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    exspaceremover = request.POST.get('exspaceremover','off')
    
    
    if removingpunc =="on":
        punchuations ='''.!()[]{};:'"\/?<>@#$_-,$%^&*'''
        analyzed=""
        for char in djangotext:
            if char not in punchuations:
                analyzed = analyzed +char
        params = {'purpose':'removing tyhe punchuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif(fullcaps == "on"):
        analyzed = ""
        for char in djangotext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'changing to upper case','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif(newlineremover == "on"):
        analyzed = ""
        for char in djangotext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose':'changing to upper case','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif(exspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate (djangotext):
            if not(djangotext[index] ==" " and djangotext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose':'removing the space','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    else:
           return HttpResponse('error')

# def about(request):
#     return HttpResponse("<h1> zayik malik</h1>")