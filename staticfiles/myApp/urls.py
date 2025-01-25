from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
from .views import appointment_view
from .views import contact_view


urlpatterns = [
    path('', views.home, name='home'), 
    path('login/', views.login_view, name='login'),
    path('logout/', views.user_logout,name='logout'), 
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('gallery/', views.gallery, name='gallery'),
    path('team/', views.team, name='team'),
    path('appointment/', appointment_view, name='appointment'),
    path('upload_report/', views.upload_report, name='upload_report'),
    path('contact/',contact_view, name='contact'),
] 
if settings.DEBUG:
     urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

  