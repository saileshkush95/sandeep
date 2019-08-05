from django.contrib import admin
from .models import (
    Title,
    Category,
    BasicInformation,
    SocialIcon,
    Education,
    Skill,
    Experiance,
    Refrences,
    Portfolio_Gallery,
    BackgroundImages
)
# Register your models here.


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('title',)

    def has_add_permission(self, request):
        count = self.model.objects.count()
        if count > 0:
            return False
        else:
            return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(BasicInformation)
class BasicInformationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date_of_birth', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('full_name', 'email1', 'email2')

    def has_add_permission(self, request):
        count = self.model.objects.count()
        if count > 0:
            return False
        else:
            return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(BackgroundImages)
class BackgroundImagesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'header_background_image',
        'contact_us_background_image'
        )
    list_filter = (
        'name',
        'header_background_image',
        'contact_us_background_image'
        )
    search_fields = (
        'name',
        'header_background_image',
        'contact_us_background_image')

    def has_add_permission(self, request):
        count = self.model.objects.count()
        if count > 0:
            return False
        else:
            return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('name',)


@admin.register(SocialIcon)
class SocialIconAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('name',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('education_name', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('education_name',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('name',)


@admin.register(Experiance)
class ExperianceAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('name',)


@admin.register(Refrences)
class RefrencesAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('name',)


@admin.register(Portfolio_Gallery)
class Portfolio_GalleryAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'category', 'created', 'updated')
    list_filter = ('project_name', 'category', 'created', 'updated')
    search_fields = ('project_name', 'category',)
