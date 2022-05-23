from django.urls import path
from lists.views import home_page

urlpatterns = [

	path("", home_page, name='home'),

]



# from django.conf.urls import url
# from lists import views

# urlpatterns = [
#     url(r'^$lists_page/', views.lists_page, name='lists_page'),
# ]