from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from MaLSTM import test
def type_questions(request):
    return render(request,"home.html")

def check(request):
    if request.method == 'POST':
        q1 = request.POST['q1']
        q2 = request.POST['q2']
        result = None
        if q1 and q2:
            print('here')
            result = test.main(q1,q2)
    return render(request,'result.html',{"similar":result})