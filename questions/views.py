from django.shortcuts import render
from django.http import HttpResponse
import cv2
import subprocess
import os
from django.core.files.storage import FileSystemStorage

def type_questions(request):
    if request.method == 'POST':
        q1 = request.POST['q1']
        q2 = request.POST['q2']
        return HttpResponse(q1)
    return render(request,"home.html")