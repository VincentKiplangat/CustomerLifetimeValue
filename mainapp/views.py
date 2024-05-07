from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Clv
from .serializers import ClvSerializer
import joblib
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import numpy as np
from django.template.loader import get_template

from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'predict.html')


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import joblib
import numpy as np

@api_view(['POST'])
def predict(request):
    try:
        # Load the XGBoost model
        xgb_model = joblib.load("xgb_tuned.pkl")

        # Extract form data from the request
        data = request.data

        # Extract form data and convert checkbox values to integers
        CustomerID = data.get('customerID')
        channel_email = 1 if data.get('channel_email') == 'on' else 0
        channel_phone = 1 if data.get('channel_phone') == 'on' else 0
        reason_signup = 1 if data.get('reason_signup') == 'on' else 0
        reason_support = 1 if data.get('reason_support') == 'on' else 0
        gender_female = 1 if data.get('gender_female') == 'on' else 0
        gender_male = 1 if data.get('gender_male') == 'on' else 0
        subscription_annual_subscription = 1 if data.get('subscription_annual_subscription') == 'on' else 0
        subscription_monthly_subscription = 1 if data.get('subscription_monthly_subscription') == 'on' else 0
        signup_period_Morning = 1 if data.get('signup_period_Morning') == 'on' else 0
        signup_period_Night = 1 if data.get('signup_period_Night') == 'on' else 0
        signup_period_Noon = 1 if data.get('signup_period_Noon') == 'on' else 0
        end_period_Morning = 1 if data.get('end_period_Morning') == 'on' else 0
        end_period_Night = 1 if data.get('end_period_Night') == 'on' else 0
        end_period_Noon = 1 if data.get('end_period_Noon') == 'on' else 0

        # Extract other numerical data
        age = float(data.get('age', 0))
        price = float(data.get('price', 0))
        lifetime_months = float(data.get('lifetime_months', 0))

        # Create a numpy array with the extracted data
        input_data = np.array([
            age, price, lifetime_months, channel_email, channel_phone, reason_signup, reason_support,
            gender_female, gender_male, subscription_annual_subscription, subscription_monthly_subscription,
            signup_period_Morning, signup_period_Night, signup_period_Noon, end_period_Morning,
            end_period_Night, end_period_Noon
        ]).reshape(1, -1)

        # Make predictions using the XGBoost model
        y_pred = xgb_model.predict(input_data)

        # Render api.html template with prediction result
        template = loader.get_template('api.html')
        context = {'prediction': y_pred}
        response = template.render(context, request)

        # Render predict.html with a SweetAlert pop-up message and redirect
        return render(request, 'predict.html', {'response': response})

    except Exception as e:
        # Return an error response if there's any exception
        return HttpResponse(f"<h1>Error: {e}</h1>", status=400)

# ************************************************************************************************************
def home(request):
    return render(request, 'index-1.html')


def about(request):
    return render(request, 'about-1.html')


def blog(request):
    return render(request, 'services-1.html')


def faq(request):
    return render(request, 'faq.html')


def contact1(request):
    return render(request, 'contact1.html')



# *****************************************************************************************
# views.py

from django.shortcuts import render
from django.core.mail import send_mail, EmailMultiAlternatives
from django.http import JsonResponse

def contact_form_submission(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Send an email
        send_mail(
            subject,
            f"Name: {name}\nEmail: {email}\nMessage: {message}",
            email,  # Sender's email
            ['vkorir.vkk@gmail.com'],  # Your email (Recipient's email)
            fail_silently=False,
        )

        # Return a JSON response indicating success
        return JsonResponse({'success': True})

    # Return a JSON response indicating failure if the request method is not POST
    return JsonResponse({'success': False})


# ******************************************************************************************
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            subject = "Welcome to Analytic Avengers where we help you predict your CLV"
            message = "Our team will contact you within 24hrs."
            email_from = settings.EMAIL_HOST_USER
            email = form.cleaned_data['email']
            recipient_list = [email]
            send_mail(subject, message, email_from, recipient_list)
            messages.success(request, 'Your message has been sent successfully. Our team will contact you within 24 hours.')
            return redirect('contact')  # Redirect to the same page to display the success message
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)



def error_404(request):
    return render(request, "404.html")


# *********************************************************************
# Newsletter
from .models import NewsletterUser
from .forms import NewsletterUserSignUpForm

# def newsletter_signup(request):
#     form = NewsletterUserSignUpForm(request.POST or None)
#
#     if form.is_valid():
#         instance = form.save(commit=False)
#         if NewsletterUser.objects.filter(email=instance.email).exists():
#             print('sorry, non-existence')
#         else:
#             instance.save()
#
#         context = {
#             'form':form,
#         }
#         template = 'newsletters/sign_up.html'
#         return render(request,template,context)
#
#
# def newsletter_unsubscribe(request):
#     form = NewsletterUserSignUpForm(request.POST or None)
#
#     if form.is_valid():
#         instance = form.save(commit=False)
#         if NewsletterUser.objects.filter(email=instance.email).exists():
#             NewsletterUser.objects.filter(email=instance.email).delete()
#
#         else:
#             print('no record')
#
#     context = {
#         "forms" : form,
#     }
#
#     template = 'newsletters/unsubscribe.html'
#     return render(request,template,context)



# APPROACH 1
# from django.shortcuts import render, redirect
# from .forms import NewsletterUserSignUpForm
# from .models import NewsletterUser
# # import the email send_mail
#
# def newsletter_signup(request):
#     form = NewsletterUserSignUpForm(request.POST or None)
#
#     if form.is_valid():
#         instance = form.save(commit=False)
#         if NewsletterUser.objects.filter(email=instance.email).exists():
#             print('Sorry, email already exists')
#             messages.warning(request, 'Your Email is already Signed up', "alert alert-warning alert-dismissible")
#         else:
#             instance.save()
#             messages.success(request, 'Your have successfully subscribed',
#                              "alert alert-success alert-dismissible")
#         # return redirect('success_url')  # Redirect to a success URL upon successful form submission
#
#         subject = "Thank you for subscribing to Analytics Avengers "
#         from_email = settings.EMAIL_HOST_USER
#         to_email = [instance.email]
#         signup_message = """Welcome to Analytics Avengers Newsletters."""
#         send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=signup_message, fail_silently=False)
#
#
#     # If the form is not valid, render the template with the form and context
#     context = {'form': form}
#     template = 'newsletters/sign_up.html'
#     return render(request, template, context)
#
# def newsletter_unsubscribe(request):
#     form = NewsletterUserSignUpForm(request.POST or None)
#
#     if form.is_valid():
#         instance = form.save(commit=False)
#         if NewsletterUser.objects.filter(email=instance.email).exists():
#             NewsletterUser.objects.filter(email=instance.email).delete()
#             messages.success(request, 'Your email has been successfully unsubscribed',
#                              "alert alert-success alert-dismissible")
#
#             subject = "You have been unsubscribed."
#             from_email = settings.EMAIL_HOST_USER
#             to_email = [instance.email]
#             signup_message = """We're saddened to see you unsubscribe from Analytics Avengers Newsletters. Sorry to see you leave. Let us know if there is an issue with our "
#                        "services"""
#             send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=signup_message,
#                       fail_silently=False)
#
#
#         else:
#             messages.warning(request, 'Your email is not subscribed',
#                              extra_tags="alert alert-warning alert-dismissible")
#
#         # return redirect('success_url')  # Redirect to a success URL upon successful form submission
#
#     # If the form is not valid, render the template with the form and context
#     context = {'form': form}
#     template = 'newsletters/unsubscribe.html'
#     return render(request, template, context)
#
#
#
# # ***********************************************************************************************************************************
# # ***********************************************************************************************************************************
# # ***********************************************************************************************************************************
from django.shortcuts import render, redirect
from .forms import NewsletterUserSignUpForm
from .models import NewsletterUser
# import the email send_mail
import os


def newsletter_signup(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            print('Sorry, email already exists')
            messages.warning(request, 'Your Email is already Signed up', extra_tags="alert alert-warning alert-dismissible")
        else:
            instance.save()
            messages.success(request, 'Your have successfully subscribed', extra_tags="alert alert-success alert-dismissible")

        subject = "Thank you for subscribing!"
        from_email = settings.EMAIL_HOST_USER
        to_email = [instance.email]

        # Correcting file path concatenation using os.path.join
        template_path = os.path.join(settings.BASE_DIR, "templates", "newsletters", "sign_up_email.txt")
        with open(template_path) as f:
            signup_message = f.read()

        message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_email)
        html_template = get_template("newsletters/sign_up_email.html").render()
        message.attach_alternative(html_template, "text/html")
        message.send()

    context = {'form': form}
    template = 'newsletters/sign_up.html'
    return render(request, template, context)




from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from .forms import NewsletterUserSignUpForm
from .models import NewsletterUser
from django.conf import settings
from django.template.loader import render_to_string

def newsletter_unsubscribe(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            messages.success(request, 'Your email has been successfully unsubscribed', extra_tags="alert alert-success alert-dismissible")

            subject = "You have been unsubscribed."
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]

            # Load the email message content from a template
            context = {'email': instance.email}
            signup_message = render_to_string('newsletters/unsubscribe_email.txt', context)

            # Send the email
            send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=signup_message, fail_silently=False)

        else:
            messages.warning(request, 'Your email is not subscribed', extra_tags="alert alert-warning alert-dismissible")

    context = {'form': form}
    template = 'newsletters/unsubscribe.html'
    return render(request, template, context)


