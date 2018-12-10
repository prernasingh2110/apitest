from django.urls import path,include
from . import views

urlpatterns = [
    path('post_location/', views.Interviewapi1.as_view(),name='postloc'),
    path('get_using_postgres/', views.Interviewapi2.as_view(),name='getpos'),
    path('get_using_self/', views.Interviewapi2b.as_view(),name='getself'),
    path('get_location/', views.Interviewapi3.as_view(),name='getloc')
]
