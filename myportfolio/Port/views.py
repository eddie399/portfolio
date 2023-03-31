from django.shortcuts import render, redirect
from .models import RecentWork
from .forms import ContactForm
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from wsgiref.util import FileWrapper
from django.http import StreamingHttpResponse
import mimetypes
import os

""""
class HomeTemplateView(TemplateView):
    template_name = 'Home.html'


    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['works'] = RecentWork.objects.all()
       # context['contact'] = ContactForm.objects.all()

        return context
        #return render(request, 'Home.html')


    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():

            return render(request, 'Home.html', {'form': form})
"""""


def HomeView(request):
    work = RecentWork.objects.all()
    return render(request, 'Home.html', {'works': work})


def projectview(request, pk):
    project = RecentWork.objects.get(id=pk)
    context = {'project': project}

    return render(request, 'Project.html', context)

def contact(request):

    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            subject = request.POST.get('subject')
            #print(name,message,subject,email)


            send_mail(subject,message,name,['eddiendamera1@gmail.com',email])

            """"
             name = request.POST.get['name']
            #email = request.POST.get['email']
            #message = request.POST.get['message']
            #subject = request.POST.get['subject']
            """
    return render(request, 'Home.html', {'form':form})

# Code for downloading CV

def downloadFile(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'Edister Ndamera_CV.docx'
    filepath= base_dir + '/Files/' + filename
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(thefile,'rb'),chunk_size),content_type=mimetypes.guess_type(thefile)[0])
    response['Content-length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "Attachment;filename=%s"%filename
    return response









