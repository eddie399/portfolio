import uuid
from django.db import models
from django.urls import reverse



class About(models.Model):
    short_description = models.TextField()
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='static')

    class Meta:
        verbose_name = 'About me'
        verbose_name_plural = 'About me'

    def __str__(self):
        return 'About me'

# service models
class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name="service_name")
    description = models.TextField(verbose_name="About_service")

    def __str__(self):
        return self.name

# recent_work models
class RecentWork(models.Model):
    title = models.CharField(max_length=100, verbose_name="Work_title", null=True)
    image = models.ImageField(upload_to="static")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    description = models.TextField()
    def __str__(self):
        return self.title

#code for reversing project view with 'pk' argument from project url
    def get_absolute_url(self):
        return reverse("Project-page",kwargs={"pk": self.pk})





class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=500)
    subject = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Create your models here.
