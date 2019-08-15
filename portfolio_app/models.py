import os

from django.db import models
from django.dispatch import receiver
from django.shortcuts import reverse
from django.utils import timezone

# Create your models here.


class Title(models.Model):
    title = models.CharField(max_length=255)
    website_title = models.CharField(max_length=255)
    favicon_icon = models.ImageField(
        upload_to='favicon_icon', default=None, blank=False,)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.title + self.website_title

    def get_absolute_url(self):
        return reverse("portfolio_app:title", args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.id,
            self.title,
        ])


class SocialIcon(models.Model):
    name = models.CharField(max_length=255)
    tooltip_text = models.CharField(max_length=255)
    font_awesome_link = models.CharField(max_length=255)
    actual_link = models.CharField(max_length=255)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("portfolio_app:social", args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.id,
            self.name,
        ])


class Category(models.Model):
    name = models.CharField(max_length=255)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("portfolio_app:category", args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.id,
            self.name,
        ])


class BasicInformation(models.Model):
    full_name = models.CharField(max_length=255)
    profile_photo = models.ImageField(
        upload_to='Profile_Photo', default=None, blank=False)
    profession = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email1 = models.EmailField()
    email2 = models.EmailField()
    phone1 = models.CharField(max_length=15)
    phone2 = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    resume = models.FileField(
        upload_to='Resume/', blank=False
    )
    about = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.email1

    def get_absolute_url(self):
        return reverse("portfolio_app:information", args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.id,
            self.full_name,
        ])


class Education(models.Model):
    education_name = models.CharField(max_length=255)
    started_from = models.DateField()
    upto = models.DateField()
    # time_duraction = models.DurationField()
    institute_name = models.CharField(max_length=255)
    institute_address = models.CharField(max_length=255)
    institute_email = models.CharField(max_length=255)
    institute_contact_number = models.CharField(max_length=15)
    institute_websites = models.CharField(max_length=255)
    description = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    objects = models.Manager()

    def __str__(self):
        return self.education_name

    def get_absolute_url(self):
        return reverse("portfolio_app:education", args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.id,
            self.education_name,
        ])


class Skill(models.Model):
    name = models.CharField(max_length=255, unique='True')
    skill_percentage = models.PositiveIntegerField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("portfolio_app:skill", args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.id,
            self.name,
        ])


class Experiance(models.Model):
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    company_address = models.CharField(max_length=255)
    company_contact_no = models.CharField(max_length=15)
    started_from = models.DateField()
    upto = models.DateField()
    description = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("portfolio_app:image", args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.id,
            self.name,
        ])


class Refrences(models.Model):
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    refrence_word = models.TextField()
    refrencer_photo = models.ImageField(
        upload_to='Profile_Photo', default=None, blank=False
    )
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("portfolio_app:refrence", args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.id,
            self.name,
        ])


class BackgroundImages(models.Model):
    name = models.CharField(max_length=255)
    header_background_image = models.ImageField(
        upload_to='header_background',
        blank=False,
        default=None
    )
    contact_us_background_image = models.ImageField(
        upload_to='contact_us_background',
        blank=False,
        default=None
    )
    publish = models.DateTimeField(default=timezone.now)
    updated = models.TimeField(auto_now=True, auto_now_add=False)
    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("portfolio_app:background", args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.id,
            self.name,
        ])


class DevelopmentManager(models.Manager):
    def get_queryset(self):
        return super(DevelopmentManager, self).get_queryset().filter(category='web development')


class DesignManager(models.Manager):
    def get_queryset(self):
        return super(DesignManager, self).get_queryset().filter(category='web design')


class PhotographyManager(models.Manager):
    def get_queryset(self):
        return super(PhotographyManager, self).get_queryset().filter(category='photography')


class Portfolio_Gallery(models.Model):
    category_choices = (
        ('web development', 'web development'),
        ('web design', 'web design'),
        ('photography', 'photography'),
    )
    project_name = models.CharField(max_length=255)
    project_image = models.ImageField(
        upload_to='project',
        blank=False,
        default=None
    )
    category = models.CharField(
        max_length=255,
        choices=category_choices,
        default='web development',)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta():
        ordering = ('created',)

    objects = models.Manager()
    development = DevelopmentManager()
    design = DesignManager()
    photography = PhotographyManager()

    def __str__(self):
        return self.project_name

    def get_absolute_url(self):
        return reverse("portfolio_app:portfolio", args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.id,
            self.project_name,
        ])


@receiver(models.signals.pre_save, sender=BackgroundImages)
def auto_delete_file_on_change_header_image(sender, instance, **kwargs):
    if not instance.pk:
        return False
    else:
        try:
            old_file = sender.objects.get(
                pk=instance.pk).header_background_image
        except sender.DoesNotExist:
            return None

        new_file = instance.header_background_image
        if not old_file == new_file:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)


@receiver(models.signals.pre_save, sender=BackgroundImages)
def auto_delete_file_on_change_contact_us_image(sender, instance, **kwargs):
    if not instance.pk:
        return False
    else:
        try:
            old_file = sender.objects.get(
                pk=instance.pk).contact_us_background_image
        except sender.DoesNotExist:
            return None

        new_file = instance.contact_us_background_image
        if not old_file == new_file:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)


@receiver(models.signals.pre_save, sender=BasicInformation)
def auto_delete_file_on_change_resume(sender, instance, **kwargs):
    if not instance.pk:
        return False
    else:
        try:
            old_file = sender.objects.get(pk=instance.pk).resume
        except sender.DoesNotExist:
            return None

        new_file = instance.resume
        if not old_file == new_file:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)


@receiver(models.signals.pre_save, sender=Title)
def auto_delete_file_on_change_title(sender, instance, **kwargs):
    if not instance.pk:
        return False
    else:
        try:
            old_file = sender.objects.get(pk=instance.pk).favicon_icon
        except sender.DoesNotExist:
            return None

        new_file = instance.favicon_icon
        if not old_file == new_file:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)


@receiver(models.signals.pre_save, sender=Refrences)
def auto_delete_file_on_change_refrences(sender, instance, **kwargs):
    if not instance.pk:
        return False
    else:
        try:
            old_file = sender.objects.get(pk=instance.pk).refrencer_photo
        except sender.DoesNotExist:
            return None

        new_file = instance.refrencer_photo
        if not old_file == new_file:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)


@receiver(models.signals.pre_save, sender=BasicInformation)
def auto_delete_file_on_change_profile_pic(sender, instance, **kwargs):
    if not instance.pk:
        return False
    else:
        try:
            old_file = sender.objects.get(pk=instance.pk).profile_photo
        except sender.DoesNotExist:
            return None

        new_file = instance.profile_photo
        if not old_file == new_file:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)
