from .  import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    # path('trial/',views.trial,name='trial'),
    # path('add/', views.result, name='result'),
    # path('mul/',views.result2,name='mul'),
    # path('div/',views.result3,name='div'),
    # path('sub/',views.result4,name='sub'),
    # path('about/',views.about,name='about'),
    # path('contact/',views.contact,name='contact'),
    # path('detail/',views.detail,name='detail'),
    # path('thank/',views.thank,name='thank'),
    # path('',views.operation,name='operations')

]