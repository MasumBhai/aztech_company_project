from django.shortcuts import render
from django.views.generic import ListView

from .models import *

'''navigation__item_active     inside class="navigation__item'''


# Create your views here.
def home(request):
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
    aboutObj = aboutpage.objects.get(about_id=1)
    context = {
        'aboutImage': aboutObj.about_pic.url,
        'aboutImageAlt': aboutObj.about_title,
    }
    return render(request, 'about.html', context=context)

def job_portal(request):
    context = {
    }
    return render(request, 'job_portal.html', context=context)


def contact(request):
    context = {
    }
    return render(request, 'contact.html', context=context)

def eCommerce(request):
    context = {
    }
    return render(request, 'industries/eCommerce.html', context=context)

def eLearning(request):
    context = {
    }
    return render(request, 'industries/eLearning.html', context=context)


def eHealthSoftware(request):
    context = {
    }
    return render(request, 'industries/eHealthSoft.html', context=context)

def eHealthApp(request):
    context = {
    }
    return render(request, 'industries/eHealthApp.html', context=context)

def eLogistics(request):
    context = {
    }
    return render(request, 'industries/eLogistics.html', context=context)

def eRetail(request):
    context = {
    }
    return render(request, 'industries/eRetailSoft.html', context=context)

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

def error(request,anything):
    context = {
    }
    return render(request, 'error.html', context=context)



