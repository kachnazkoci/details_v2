from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.generic import FormView

from user.forms import ContactForm
from nutrition.models import Contact, Home
from user.models import User
from django.views import View


class HomeView(View):
    model = Home
    template_name = 'home.html'
    extra_context = {'page_name': 'Home'}

    @staticmethod
    def get(request):
        context = {
            #'number_of_users': User.objects.all().count(),
            'page_name': 'Home'
        }
        return TemplateResponse(request, 'home.html', context=context)

    @staticmethod
    def post(request):
        return HttpResponse('Class based view')


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        phone_number = form.cleaned_data.get('phone_number')
        email = form.cleaned_data.get('email')
        subject = form.cleaned_data.get('subject')
        contact_at = form.cleaned_data.get('contact_at')

        Contact.objects.create(
            name=name,
            phone_number=phone_number,
            email=email,
            subject=subject,
            contact_at=contact_at
        )
        return TemplateResponse(self.request, 'contact.html', context={'form': ContactForm()})

    def form_invalid(self, form):
        return TemplateResponse(self.request, 'nutrition/templates/contact.html', context={'form': form})
