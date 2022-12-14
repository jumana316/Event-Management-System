"""EMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path  
from Events.views import(
    about_page, contact_page, home_page, landing_page, login, signup ,admin_login, admin_booking
    ) 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_page, name='home'),
    path('about/', about_page, name='about-page'),
    path('contact/', contact_page, name='contact-page'),
    path('', landing_page),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('Events/', include('Events.urls', namespace='Events')),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('admin_login/',admin_login,name='admin-login'),
    path('admin_booking/',admin_booking,name='admin-booking')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  
