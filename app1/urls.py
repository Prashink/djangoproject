from django.urls import path
from .import views
app_name='app1'
urlpatterns=[
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('home/<int:id>',views.home,name='home'),
    path('gallery',views.gallery,name='gallery'),
    path('details/<int:id>',views.details,name='details'),
    path('update/<int:id>',views.update,name='update'),
    path('changepassword/<int:id>',views.changepassword,name='changepassword'),
    path('logouts',views.logouts,name='logouts'),
]