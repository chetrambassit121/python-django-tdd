from django.conf.urls import url
from accounts import views
# from django.contrib.auth import logout
# from django.contrib.auth.views import logout
from django.contrib.auth.views import LogoutView

urlpatterns = [
    url(r'^send_login_email$', views.send_login_email, name='send_login_email'),
    url(r'^login$', views.login, name='login'),
    # url(r'^logout$', logout, {'next_page': '/'}, name='logout'),
    url(r'^logout$', LogoutView.as_view(), name='logout'),
    # url(r'^logout$', logout, name='logout'),

]