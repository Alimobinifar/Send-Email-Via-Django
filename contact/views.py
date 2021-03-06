from django.shortcuts import render, HttpResponse
from django.views import View
from django.core.mail import send_mail, EmailMessage
from .forms import EmailForm
from django.conf import settings



class SendMailView(View):

    def get(self, request):
        form_data = EmailForm
        return render(request, 'content.html', {"form": form_data})

    def post(self, request):
        form_data = EmailForm(request.POST)
        if form_data.is_valid():
            subject = form_data.cleaned_data['subject']
            message = form_data.cleaned_data['text']
            from_email = settings.EMAIL_HOST_USER
            recipient_list=[]
            recipient_list.append(form_data.cleaned_data['email'])
            email = send_mail(subject, message, from_email, recipient_list)
            if email is 1:
                return HttpResponse("Email has been send successfully")
            else:
                return HttpResponse(form_data.errors)

        else:
            return HttpResponse(form_data.errors)

