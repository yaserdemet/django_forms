"""forms URL Configuration

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
from django.contrib import admin
from django.urls import path,include

##? ADMIN PANELDE EKLENEN STATIC LERİ GÖRMEK İÇİN BUNLARI EKLE.
from django.conf import settings
from django.conf.urls.static import static

from student.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'), 
    
    ## ? => ana urle geldiğinde path yoksa index viewe gitsin ve orada index.html i render etsin
    
    path('student/', include('student.urls')),
    ## * => student urlsi geldiği zamana beni student.urls e yönlendirsin
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)





