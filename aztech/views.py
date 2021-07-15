from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.timezone import get_current_timezone
import datetime

from .models import *

'''navigation__item_active     inside class="navigation__item'''


# Create your views here.
def home(request):
    baseEverywhere(request=request)
    context = {
    }
    return render(request, 'index.html', context=context)


def challenges(request):
    context = {
    }
    return render(request, 'challenges.html', context=context)


# class About(ListView):
#     model = about
#     template_name = 'index.html'

def about(request):
    aboutObj = AboutPage.objects.get(about_id=1)
    context = {
        'aboutImage': aboutObj.about_pic.url,
        'aboutImageAlt': aboutObj.about_title,
    }
    return render(request, 'about.html', context=context)


def job_portal(request):
    if request.method == 'POST':
        p_name = request.POST['participant-name']
        p_mail = request.POST['participant-email']
        p_phone = request.POST['participant-phone']
        p_linkedIn = request.POST['participant-linkedin']
        p_github = request.POST['participant-github']
        p_msg = request.POST['participant-message']
        p_resume = request.FILES['participant-resume']
        p_cover_letter = request.FILES['participant-covLetter']
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

            subject = f'Thanks {newParticipant.participant_name} for applying into Aztech Valley'
            body = render_to_string(template_name='promotional_congratulations.html',
                                    context={'participantName': newParticipant.participant_name,
                                             'participantPhone': newParticipant.participant_phone,
                                             'participantGithub': newParticipant.participant_github,
                                             'participantLinkedIn': newParticipant.participant_linkedIn, })
            sender = settings.EMAIL_HOST_USER
            recipient_list = [newParticipant.participant_mail, ]
            send_mail(subject=subject, message=body, from_email=sender, recipient_list=recipient_list,
                      fail_silently=False, )
        except:
            messages.error(request=request, message="Something Went Wrong, Kindly Try Again")
    context = {
    }
    return render(request, 'job_portal.html', context=context)


def contact(request):
    baseEverywhere(request=request)
    context = {
    }
    return render(request, 'contact.html', context=context)


def eCommerce(request):
    context = {
    }
    return render(request, 'programme/eCommerce.html', context=context)


def eLearning(request):
    context = {
    }
    return render(request, 'programme/eLearning.html', context=context)


def eHealthSoftware(request):
    context = {
    }
    return render(request, 'programme/eHealthSoft.html', context=context)


def eHealthApp(request):
    context = {
    }
    return render(request, 'programme/eHealthApp.html', context=context)


def eLogistics(request):
    context = {
    }
    return render(request, 'programme/eLogistics.html', context=context)


def eRetail(request):
    context = {
    }
    return render(request, 'programme/eRetailSoft.html', context=context)


def sCloud(request):
    context = {
    }
    return render(request, 'sarvices/cloud.html', context=context)


def sAI(request):
    context = {
    }
    return render(request, 'sarvices/AI/artificial_intelligence.html', context=context)


def sAI_retail(request):
    context = {
    }
    return render(request, 'sarvices/AI/ai_for_retail.html', context=context)


def sAI_education(request):
    context = {
    }
    return render(request, 'sarvices/AI/ai_for_education.html', context=context)


def sAI_health(request):
    context = {
    }
    return render(request, 'sarvices/AI/ai_for_healthcare.html', context=context)


def sAI_automation(request):
    context = {
    }
    return render(request, 'sarvices/AI/ai_for_automation.html', context=context)


def sAugmentedReality(request):
    context = {
    }
    return render(request, 'sarvices/augmentedReality.html', context=context)


def sDigiTransform(request):
    context = {
    }
    return render(request, 'sarvices/digitalTransformation.html', context=context)


def sTeam(request):
    context = {
    }
    return render(request, 'sarvices/team/dedicatedTeams.html', context=context)


def sTeamCto(request):
    context = {
    }
    return render(request, 'sarvices/team/cto_service.html', context=context)


def sDevops(request):
    context = {
    }
    return render(request, 'sarvices/devops.html', context=context)


def sTechnologyConsulting(request):
    context = {
    }
    return render(request, 'sarvices/technologyConsulting.html', context=context)


def sAppDevelopment(request):
    context = {
    }
    return render(request, 'sarvices/appDevelopment.html', context=context)


def sDataConsulting(request):
    context = {
    }
    return render(request, 'sarvices/dataConsulting.html', context=context)


def sSoftwareTesting(request):
    context = {
    }
    return render(request, 'sarvices/softwareTesting.html', context=context)


def error(request, anything):
    context = {
    }
    return render(request, 'error.html', context=context)


def baseEverywhere(request):
    if request.POST.get('send-message'):
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

            subject = f'Thanks {newContact.contact_name} for contacting Aztech Valley'
            message = render_to_string(template_name='promotional_Advertise.html',
                                       context={'personName': newContact.contact_name,
                                                'personPhone': newContact.contact_phone, })
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [newContact.contact_mail, ]
            send_mail(subject, message, email_from, recipient_list, fail_silently=False)
        except:
            messages.error(request=request, message="Something Went Wrong, Kindly Try Again")
