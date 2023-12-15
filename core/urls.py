from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('', Index.as_view()),
     path('lista_produtos/<int:pk>/', Lista.as_view(), name='lista_produtos'),
     path('carrinho/', Carrinho.as_view(), name='carrinho'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
