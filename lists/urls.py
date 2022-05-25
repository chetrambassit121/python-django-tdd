from django.urls import path
from lists.views import home_page, view_list

urlpatterns = [

	path("", home_page, name='home'),
	path("lists/the-only-list-in-the-world/", view_list, name='view_list'),


]













# ........................................
# from django.urls import path
# from lists.views import home_page

# urlpatterns = [

# 	path("", home_page, name='home'),

# ]











# ...........................................
# from django.conf.urls import url
# from lists import views

# urlpatterns = [
#     url(r'^$lists_page/', views.lists_page, name='lists_page'),
# ]