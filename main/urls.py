from django.contrib.sitemaps.views import sitemap
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from portfolio_app.sitemaps import (
    TitleSitemap, SocialIconSitemap, BasicInformationSitemap,
    EducationSitemap, SkillSitemap,
    ExperianceSitemap, RefrencesSitemap, BackgroundImagesSitemap,
    Portfolio_GallerySitemap, CategorySitemap, )

sitemaps = {
    'title': TitleSitemap,
    'social': SocialIconSitemap,
    'basic': BasicInformationSitemap,
    'education': EducationSitemap,
    'skill': SkillSitemap,
    'experiance': ExperianceSitemap,
    'refrence': RefrencesSitemap,
    'background': BackgroundImagesSitemap,
    'portfolio': Portfolio_GallerySitemap,
    'category': CategorySitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio_app.urls', namespace='portfolio_app')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
