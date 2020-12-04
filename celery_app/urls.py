from django.conf.urls import url
from django.views.generic import RedirectView
from .views import ReviewEmailView

app_name = 'celery_app'

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/contact/')),
    url(r'^contact/$', ReviewEmailView.as_view(), name='contact'),
]