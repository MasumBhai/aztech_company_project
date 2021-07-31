import json
import urllib
from urllib import parse,request
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views import generic
from django.views.generic import ListView
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.timezone import get_current_timezone
import datetime
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from aztech.forms import CommentForm,BlogPostForm
from django.contrib.auth import authenticate, login, logout
import time
import webbrowser as web
import pyautogui as pg
import threading
from threading import Thread
from .models import *

'''navigation__item_active     inside class="navigation__item'''


# Create your views here.
class EmailThread(threading.Thread):

    def __init__(self, subject, message, sender, recipient, fail_silently):
        self.subject = subject
        self.message = message
        self.sender = sender
        self.recipient = recipient
        self.fail_silently = fail_silently
        threading.Thread.__init__(self)

    def run(self):
        send_mail(self.subject,self.message,self.sender,self.recipient,self.fail_silently)

def whatsappMsg(phone,msg):
    web.open('https://web.whatsapp.com/send?phone=+88'+phone+'&text='+msg)
    time.sleep(10)
    pg.press('enter')

def auth_logout(request):
  logout(request)
  return redirect('home')

def baseEverywhere(request):
    if request.POST.get('send-message'):
        messages.success(request, 'You successfully sent your msg')
        nameOfContact = request.POST.get('contact-name')
        emailAddress = request.POST.get('contact-email')
        phoneNumber = request.POST.get('contact-phone')
        msgOfContact = request.POST.get('contact-message')
        msgTime = str(datetime.datetime.now(tz=get_current_timezone()))
        try:
            newContact = ContactUs.objects.create(
                contact_name=nameOfContact,
                contact_phone=phoneNumber,
                contact_mail=emailAddress,
                contact_msg=msgOfContact,
                contact_time=msgTime,
            )
            messages.success(request=request, message="An email is sent to your mailing address")

            companyInfo = SoftwareCompany.objects.get(company_code__exact="coded by Masum phone(+8801551805248)")

            subject = f'Thanks {newContact.contact_name} for contacting Aztech Valley'
            message = render_to_string(template_name='promotional_Advertise.html',
                                       context={'personName': newContact.contact_name,
                                                'personPhone': newContact.contact_phone,
                                                'companyName': companyInfo.company_name,
                                                'companyPhone': companyInfo.company_phone,
                                                'companyMail': companyInfo.company_mail,
                                                })
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [newContact.contact_mail, ]
            EmailThread(subject=subject, message=message, sender=email_from, recipient=recipient_list,
                        fail_silently=False).start()
            # send_mail(subject, message, email_from, recipient_list, fail_silently=False)
        except:
            messages.error(request=request, message="Something Went Wrong, Kindly Try Again")


def home(request):
    baseEverywhere(request=request)
    context = {
    }
    return render(request, 'index.html', context=context)


def blog(request):
    baseEverywhere(request=request)
    postSuccess = False
    recapchaError = False
    object_list = BlogPost.objects.filter(status=1).order_by('-created_on')
    paginator = Paginator(object_list, 5)  # 5 posts in each page
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # jodi page number integer na hoy tobe first page-e retun koro
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    if request.method == 'POST':
        print("submit_button")
        post_form = BlogPostForm(request.POST,request.FILES)
        if post_form.is_valid():
            print("valid_post")
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            print("recapcha checked")

            if result['success']:
                print("right")
                post_form.save()
                postSuccess = True
                messages.success(request, 'Thanks, your post is in moderation section')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                recapchaError = True
                print("wrong")
    else:
        post_form = BlogPostForm()

    context = {
        'page': page,
        'post_list': post_list,
        'post_form': post_form,
        'post_Success': postSuccess,
        'recaptchaError': recapchaError,
    }
    return render(request, 'Our_Blog.html', context=context)

# class BlogDetails(generic.DetailView):
#     model = BlogPost
#     template_name = 'Blog_Details.html'
def post_detail(request, slug):
    baseEverywhere(request=request)
    template_name = 'Blog_Details.html'
    post = get_object_or_404(BlogPost, slug=slug)
    comments = post.comments.filter(comment_status=1)
    new_comment = None
    successful = False
    recapchaError = False
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.commented_post = post
            # Save the comment to the database but via recaptcha
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())

            if result['success']:
                comment_form.save()
                successful = True
                messages.success(request, 'New comment added in queue!')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                recapchaError = True
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'commentSuccess': successful,
                                           'recapchaError': recapchaError})


def project_detil(request, slug):
    baseEverywhere(request=request)
    template_name = 'latest_projects.html'
    proj = get_object_or_404(LatestProjects, project_slug=slug)
    context = {
        'project': proj,
    }
    return render(request, template_name=template_name, context=context)


def about(request):
    baseEverywhere(request=request)
    context = {

    }
    return render(request, 'about.html', context=context)

def job_portal(request):
    baseEverywhere(request=request)
    if request.POST.get('job-applied'):
        p_name = request.POST.get('participant-name',False)
        p_mail = request.POST.get('participant-email',False)
        p_phone = request.POST.get('participant-phone',False)
        p_linkedIn = request.POST.get('participant-linkedin',False)
        p_github = request.POST.get('participant-github',False)
        p_msg = request.POST.get('participant-message',False)
        p_resume = request.FILES.get('participant-resume',False)
        p_cover_letter = request.FILES.get('participant-covLetter',False)
        clicked_at = str(datetime.datetime.now(tz=get_current_timezone()))
        try:
            newParticipant = JobRequest.objects.create(
                participant_name=p_name,
                participant_mail=p_mail,
                participant_phone=p_phone,
                participant_linkedIn=p_linkedIn,
                participant_github=p_github,
                participant_msg=p_msg,
                participant_resume=p_resume,
                participant_cover_letter=p_cover_letter,
                participant_time=clicked_at
            )
            messages.success(request=request, message="An email is sent to your mailing address")

            companyInfo = SoftwareCompany.objects.get(company_code__exact="coded by Masum phone(+8801551805248)")

            subject = f'Thanks {newParticipant.participant_name} for applying into Aztech Valley'
            body = render_to_string(template_name='promotional_congratulations.html',
                                    context={'participantName': newParticipant.participant_name,
                                             'participantPhone': newParticipant.participant_phone,
                                             'participantGithub': newParticipant.participant_github,
                                             'participantLinkedIn': newParticipant.participant_linkedIn,
                                             'companyName': companyInfo.company_name,
                                             'companyPhone': companyInfo.company_phone,
                                             'companyMail': companyInfo.company_mail,
                                             })
            sender = settings.EMAIL_HOST_USER
            recipient_list = [newParticipant.participant_mail, ]

            EmailThread(subject=subject,message=body,sender=sender,recipient=recipient_list,fail_silently=False).start()
            # send_mail(subject=subject, message=body, from_email=sender, recipient_list=recipient_list,
            #           fail_silently=False, )
        except:
            messages.error(request=request, message="Something Went Wrong, Kindly Try Again")
        try:
            whatsappMsg(phone=p_phone, msg=p_msg)
        except:
            messages.error("Wrong Mobile Info")
    context = {
    }
    return render(request, 'job_portal.html', context=context)


def contact(request):
    baseEverywhere(request=request)
    context = {
    }
    return render(request, 'contact.html', context=context)


def eCommerce(request):
    baseEverywhere(request=request)
    context = {
    }
    return render(request, 'programme/eCommerce.html', context=context)


def eLearning(request):
    baseEverywhere(request=request)
    context = {
    }
    return render(request, 'programme/eLearning.html', context=context)


def eHealthSoftware(request):
    baseEverywhere(request=request)
    context = {
    }
    return render(request, 'programme/eHealthSoft.html', context=context)


def eHealthApp(request):
    baseEverywhere(request=request)
    context = {
    }
    return render(request, 'programme/eHealthApp.html', context=context)


def eLogistics(request):
    baseEverywhere(request=request)
    context = {
    }
    return render(request, 'programme/eLogistics.html', context=context)


def eRetail(request):
    baseEverywhere(request=request)
    context = {
    }
    return render(request, 'programme/eRetailSoft.html', context=context)


def sCloud(request):
    baseEverywhere(request=request)
    context = {
    }
    return render(request, 'sarvices/cloud.html', context=context)


def sAI(request):
    baseEverywhere(request=request)
    context = {
    }
    return render(request, 'sarvices/AI/artificial_intelligence.html', context=context)


def sAI_retail(request):
    baseEverywhere(request=request)
    context = {
    }
    return render(request, 'sarvices/AI/ai_for_retail.html', context=context)


def sAI_education(request):
    baseEverywhere(request=request)
    context = {
    }
    return render(request, 'sarvices/AI/ai_for_education.html', context=context)


def sAI_health(request):
    baseEverywhere(request=request)
    context = {
    }
    return render(request, 'sarvices/AI/ai_for_healthcare.html', context=context)


def sAI_automation(request):
    baseEverywhere(request=request)
    context = {
    }
    return render(request, 'sarvices/AI/ai_for_automation.html', context=context)


def sAugmentedReality(request):
    baseEverywhere(request=request)
    context = {
    }
    return render(request, 'sarvices/augmentedReality.html', context=context)


def sDigiTransform(request):
    baseEverywhere(request=request)
    context = {
    }
    return render(request, 'sarvices/digitalTransformation.html', context=context)


def sTeam(request):
    baseEverywhere(request=request)
    context = {
    }
    return render(request, 'sarvices/team/dedicatedTeams.html', context=context)


def sTeamCto(request):
    baseEverywhere(request=request)
    context = {
    }
    return render(request, 'sarvices/team/cto_service.html', context=context)


def sDevops(request):
    baseEverywhere(request=request)
    context = {
    }
    return render(request, 'sarvices/devops.html', context=context)


def sTechnologyConsulting(request):
    baseEverywhere(request=request)
    context = {
    }
    return render(request, 'sarvices/technologyConsulting.html', context=context)


def sAppDevelopment(request):
    baseEverywhere(request=request)
    context = {
    }
    return render(request, 'sarvices/appDevelopment.html', context=context)


def sDataConsulting(request):
    baseEverywhere(request=request)
    context = {
    }
    return render(request, 'sarvices/dataConsulting.html', context=context)


def sSoftwareTesting(request):
    baseEverywhere(request=request)
    client_details = OurClients.objects.all()
    context = {
        'clientInfo': client_details,
    }
    return render(request, 'sarvices/softwareTesting.html', context=context)


def error(request, anything=None): # template missing
    # baseEverywhere(request=request)
    context = {
    }
    return render(request, 'error.html', context=context)
