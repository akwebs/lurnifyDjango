from django.shortcuts import render
from web_src.models import *
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
# Create your views here.

def home(request):
    return render(request, 'web_src/index.html')

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('mobile')
        dream  = request.POST.get('dream')
        email = request.POST.get('email')
        member_obj=Register.objects.create(
            name = name,
            dream = dream,
            email = email,
            mobile= phone,
        )
        member_obj.save()
        messages.success(request, 'Form submission successful')
        return render(request, 'web_src/index.html')
    hero = hero_section.objects.all().first()
    features = feature_section.objects.all()
    video = video_section.objects.all().first()
    growth = growth_section.objects.all().first()
    growth_data = growth_section_data.objects.all()
    step = steps_section.objects.all().first() 
    steps_data = steps.objects.all()
    showcase    = showcase_section.objects.all().first()
    showcase_data = showcase_section_data.objects.all()
    testimonial =testimonial_section.objects.all().first()
    testimonial_data = testimonials.objects.all()
    faq_sect_data    =faq_section.objects.all().first()
    faqs            =faq.objects.all()
    context = {
        
        'hero': hero,
        'features': features,
        'video': video,
        'growth': growth,
        'growth_data': growth_data,
        'step': step,
        'steps_data': steps_data,
        'showcase': showcase,
        'showcase_data': showcase_data,
        'test': testimonial,
        'test_data': testimonial_data,
        'faq_data': faq_sect_data,
        'faqs': faqs,
    }
    return render(request, 'web_src/base.html', context)

def privacy(request):
    privacy = privacy_policy.objects.filter(slug="privacy").first()
    context = {
        'privacy_data': privacy,
    }
    return render(request, 'web_src/privacy.html', context)

def terms(request):
    privacy = privacy_policy.objects.filter(slug="terms").first()
    context = {
        'privacy_data': privacy,
    }
    return render(request, 'web_src/terms.html', context)

def refund(request):
    privacy = privacy_policy.objects.filter(slug="refund").first()
    context = {
        'privacy_data': privacy,
    }
    return render(request, 'web_src/refund.html', context)
    
def about_us(request):
    privacy = privacy_policy.objects.filter(slug="about").first()
    context = {
        'privacy_data': privacy,
    }
    return render(request, 'web_src/about_us.html', context)
    
def our_mission(request):
    privacy = privacy_policy.objects.filter(slug="mission").first()
    context = {
        'privacy_data': privacy,
    }
    return render(request, 'web_src/mission.html', context)   



def our_vision(request):
    privacy = privacy_policy.objects.filter(slug="vision").first()
    context = {
        'privacy_data': privacy,
    }
    return render(request, 'web_src/vision.html', context)       
    
    
    
    