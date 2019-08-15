from django.urls import path
from portfolio_app.views import index
from .views import (
    BackgroundImagesDetailView,
    Portfolio_GalleryDetailView, CategoryDetailView, SkillDetailView,
    EducationDetailView, ExperianceDetailView, SocialIconDetailView,
    BasicInformationDetailView, TitleDetailView, RefrencesDetailView
)


app_name = 'portfolio_app'

urlpatterns = [
    path('', index, name='home'),
    path('background/<int:pk>', BackgroundImagesDetailView.as_view(), name='image'),
    path('portfolio/<int:year>/<int:month>/<int:day>/<int:id>/<slug:post>/',
         Portfolio_GalleryDetailView.as_view(), name='portfolio'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category'),
    path('skill/<int:pk>', SkillDetailView.as_view(), name='skill'),
    path('education/<int:pk>', EducationDetailView.as_view(), name='education'),
    path('social/<int:pk>', SocialIconDetailView.as_view(), name='social'),
    path('experiance/<int:pk>', ExperianceDetailView.as_view(), name='experiance'),
    path('information/<int:pk>',
         BasicInformationDetailView.as_view(), name='information'),
    path('title/<int:pk>', TitleDetailView.as_view(), name='title'),
    path('refrence/<int:pk>', RefrencesDetailView.as_view(), name='refrence'),

]
