from .forms import EmailForm
from .models import Emails
from django.views.generic import ListView,FormView
from django.core.mail import send_mail, EmailMultiAlternatives
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

class BasicEmailView(FormView, ListView):
    template_name = "content/home.html"
    model = Emails
    context_object_name = 'mydata'
    form_class = EmailForm
    success_url = "/"
    #dja302ema2839@outlook.com
    def form_valid(self, form):
        my_subject = "Email from our Django app!"
        my_message = "This is a message from our app"
        my_recipient = form.cleaned_data['email']

        send_mail(
            subject = my_subject,
            message = my_message,
            recipient_list = [my_recipient],
            from_email = None,
            #from_email is only required to be filled if you do not want to use the value in our settings
            fail_silently=False,
        )

        obj = Emails(
            email = my_recipient,
            subject = my_subject,
            message = my_message
        )

        obj.save()
        
        return super().form_valid(form)


def content():
    result_list = list(Emails.objects.all()\
                .values('email', 
                        'subject',
                        'created_at',
                        'id',
                       ))
  
    return JsonResponse(result_list, safe=False)




class TemplateEmailView(FormView, ListView):
    template_name = "content/home2.html"
    model = Emails
    context_object_name = 'mydata'
    form_class = EmailForm
    success_url = "/"
    #dja302ema2839@outlook.com
    def form_valid(self, form):
        my_subject = "Email from our Django app!"
        my_message = "This is a message from our app"
        
        my_recipient = form.cleaned_data['email']
        
        
        html_message = render_to_string("content/email.html", context=context)
        plain_message = strip_tags(html_message)

        msg = EmailMultiAlternatives(
            subject= my_subject,
            body=plain_message,
            from_email = None,
            to=[my_recipient],
            fail_silently=False,
        )

        msg.attach_alternative(html_message, "text/html")
        msg.send()

        obj = Emails(
            email = my_recipient,
            subject = my_subject,
            message = my_message
        )

        obj.save()
        
        return super().form_valid(form)
    
    #myuser 
    #Testing321