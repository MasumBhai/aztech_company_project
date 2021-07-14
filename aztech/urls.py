"""django_web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('challenges/', views.challenges, name='challenges'),
    path('career/', views.job_portal, name='job_portal'),

    path('programme/e-commerce/', views.eCommerce, name='eCommerce'),
    path('programme/e-learning/', views.eLearning, name='eLearning'),
    # path('programme/e-health-software/', views.eHealthSoftware, name='eHealthSoft'),  # navbar style change korte hobe
    path('programme/e-health-app/', views.eHealthApp, name='eHealthApp'),  # svg is not working
    path('programme/logistics/', views.eLogistics, name='eLogistics'),
    path('programme/retail-software/', views.eRetail, name='eRetail'),  # our clients part
    path('programme/retail-software/', views.eRetail, name='eRetail'),

    # path('sevices/cloud/', views.sCloud, name='sCloud'),
    # path('sevices/Augmented-Reality/', views.sAugmentedReality, name='sAugReality'),
    # path('sevices/data-consulting/', views.sDataConsulting, name='sDataConsulting'),
    # path('sevices/devops/', views.sDevops, name='sDevops'),
    path('sevices/AI/', views.sAI, name='sAI'),
    path('sevices/AI/ai-for-retail/', views.sAI_retail, name='sAI_retail'),
    path('sevices/AI/ai-for-education/', views.sAI_education, name='sAI_education'),
    path('sevices/AI/ai-for-health/', views.sAI_health, name='sAI_health'),
    path('sevices/AI/ai-for-automation/', views.sAI_automation, name='sAI_automation'),
    path('sevices/digital-transformation/', views.sDigiTransform, name='sDigiTransform'),
    path('sevices/dedicated-team/', views.sTeam, name='sTeam'),
    path('sevices/dedicated-team/cto/', views.sTeamCto, name='sTeamCto'),
    path('sevices/technology-consulting/', views.sTechnologyConsulting, name='sTechnologyConsulting'),
    path('sevices/app-development/', views.sAppDevelopment, name='sAppDevelopment'),
    path('sevices/software-testing/', views.sSoftwareTesting, name='sSoftwareTesting'),

    path('<slug:anything>', views.error, name='error'),

]
