from django.contrib.sitemaps import Sitemap
from .models import (Title, SocialIcon, Category, BasicInformation,
                     Education, Skill, Experiance, Refrences, BackgroundImages, Portfolio_Gallery)


class TitleSitemap(Sitemap):

    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Title.objects.all()

    def lastmod(self, obj):
        return obj.updated


class SocialIconSitemap(Sitemap):

    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return SocialIcon.objects.all()

    def lastmod(self, obj):
        return obj.updated


class BasicInformationSitemap(Sitemap):

    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return BasicInformation.objects.all()

    def lastmod(self, obj):
        return obj.updated


class EducationSitemap(Sitemap):

    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Education.objects.all()

    def lastmod(self, obj):
        return obj.updated


class SkillSitemap(Sitemap):

    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Skill.objects.all()

    def lastmod(self, obj):
        return obj.updated


class ExperianceSitemap(Sitemap):

    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Experiance.objects.all()

    def lastmod(self, obj):
        return obj.updated


class RefrencesSitemap(Sitemap):

    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Refrences.objects.all()

    def lastmod(self, obj):
        return obj.updated


class BackgroundImagesSitemap(Sitemap):

    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return BackgroundImages.objects.all()

    def lastmod(self, obj):
        return obj.updated


class Portfolio_GallerySitemap(Sitemap):

    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Portfolio_Gallery.objects.all()

    def lastmod(self, obj):
        return obj.updated


class CategorySitemap(Sitemap):

    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.updated
