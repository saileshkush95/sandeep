from django.urls import path
from portfolio_app.views import index

app_name = 'portfolio_app'

urlpatterns = [
    path('', index, name='home')

]
