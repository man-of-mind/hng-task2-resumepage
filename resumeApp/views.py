from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

#class HomePage(models.CreateView):
#    pass

def HomePage(request):
    return render(request, 'resumeApp/index.html')


def sendMessage(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        body = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'subject': request.POST.get('subject'),
            'message': request.POST.get('message'),
        }

        mail_body = "\n".join(body.values())

        try:
            send_mail(subject, mail_body, 'admin@example.com', ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid Header')
        messages.success(request, 'Message sent successfully!!!')
        return redirect('home')
    return render(request, 'resumeApp/index.html')
