from django.shortcuts import render, redirect
from django.core.mail import send_mail
# Create your views here.

def home(request):
	return render(request, 'Golden/homepage.html')

def prodone(request):
    return render(request, 'Golden/productone.html')

def prodtwo(request):
    return render(request, 'Golden/producttwo.html')

def prodthree(request):
    return render(request, 'Golden/productthree.html')

def track(request):
    return render(request, 'Golden/track.html')


def quicksend(request):
    if request.method=='POST':
        fname = request.POST['cpname']
        email = request.POST['cpemail']
        phone = request.POST['cpphone']
        message = request.POST['cpmessage']

        send_mail(fname + '(' + phone + ')' + ' has sent you an email', message, email, ['n.s.joarder@se15.qmul.ac.uk'])


        return redirect('home')