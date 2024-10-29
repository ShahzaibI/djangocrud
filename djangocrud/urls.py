"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('register/', register, name='register'),

    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),

    path('receipe/create/', create, name='createReceipe'),
    path('receipe/delete/<id>/', delete, name='deleteReceipe'),
    path('receipe/update/<id>/', update, name='updateReceipe'),
    path('students/', get_students, name='getStudent'),
    path('student/marks/<student_id>', see_marks, name='studentMarks'),
]
# For image
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
