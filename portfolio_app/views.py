import json  # import for google recaptcha
import urllib  # import for google recaptcha
from django.conf import settings
from django.shortcuts import render, redirect  # , get_object_or_404, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib import messages
# from .forms import ContactForm
from django.views.generic import DetailView

from .models import (
    Portfolio_Gallery,
    Category,
    Skill,
    Education,
    Refrences,
    Experiance,
    SocialIcon,
    BasicInformation,
    Title,
    BackgroundImages,
)

# Create your views here.


class BackgroundImagesDetailView(DetailView):
    model = BackgroundImages
    # template_name = ".html"


class Portfolio_GalleryDetailView(DetailView):
    model = Portfolio_Gallery
    # template_name = ".html"


class CategoryDetailView(DetailView):
    model = Category
    # template_name = ".html"


class SkillDetailView(DetailView):
    model = Skill
    # template_name = ".html"


class EducationDetailView(DetailView):
    model = Education
    # template_name = ".html"


class ExperianceDetailView(DetailView):
    model = Experiance
    # template_name = ".html"


class RefrencesDetailView(DetailView):
    model = Refrences
    # template_name = ".html"


class SocialIconDetailView(DetailView):
    model = SocialIcon
    # template_name = ".html"


class BasicInformationDetailView(DetailView):
    model = BasicInformation
    # template_name = ".html"


class TitleDetailView(DetailView):
    model = Title
    # template_name = ".html"


def index(request):
    # title = Title.objects.get(id=1)
    countT = Title.objects.count()
    if countT > 0:
        title = Title.objects.get(id=1)
    else:
        title = None

    countB = Title.objects.count()
    if countB > 0:
        basic_information = BasicInformation.objects.get(id=1)
    else:
        basic_information = None

    socialicon = SocialIcon.objects.all()
    skill = Skill.objects.all()
    refrence = Refrences.objects.all()
    experiance = Experiance.objects.all()
    educations = Education.objects.all()
    category = Category.objects.all()

    countI = BackgroundImages.objects.count()
    if countI > 0:
        background_images = BackgroundImages.objects.get(id=1)
    else:
        background_images = None

    portfolios = Portfolio_Gallery.objects.all()
    development = Portfolio_Gallery.development.all()
    photography = Portfolio_Gallery.photography.all()
    design = Portfolio_Gallery.design.all()

    # This code is for contact us form
    if request.method == 'POST':
        user_name = request.POST['full_name']
        user_subject = request.POST['subject']
        user_email = request.POST['email']
        user_phone = request.POST['phone']
        user_message = request.POST['message']

        subject = 'Contact Form Received'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [settings.DEFAULT_FROM_EMAIL]

        template = get_template('portfolio_app/contact_template.txt')
        context = {
            'name': user_name,
            'subject': user_subject,
            'from_email': user_email,
            'phone': user_phone,
            'message': user_message,
        }
        message = template.render(context)

        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.PRIVATE_GOOGLE_RECAPTCHA_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req = urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())

        if result['success']:
            try:
                send_mail(
                    subject,
                    message,
                    from_email,
                    to_email,
                    fail_silently=True,
                )
                messages.success(
                    request, ('Message sent success!............'))
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/')
        else:
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')

    return render(
        request,
        'portfolio_app/index.html',
        {
            'title': title,
            'basic_information': basic_information,
            'socialicon': socialicon,
            'skill': skill,
            'refrence': refrence,
            'educations': educations,
            'experiance': experiance,
            'category': category,
            'backgroundimages': background_images,
            'portfolio': portfolios,
            # 'form': form,
            'developments': development,
            'designs': design,
            'photographys': photography
        })
