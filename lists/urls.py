from django.conf.urls import url
from lists import views

urlpatterns = [
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^(\d+)/$', views.view_list, name='view_list'),
    url(r'^(\d+)/add_item$', views.add_item, name='add_item'),
]










# from django.urls import path
# from lists.views import home_page, view_list, new_list, add_item

# urlpatterns = [

# 	path("new", new_list, name='new_list'),
# 	path(r"^(\d+)/add_item$", add_item, name='add_item'),
# 	path(r"^(\d+)/$", view_list, name='view_list'),


# ]














# from django.urls import path
# from lists.views import home_page, view_list

# urlpatterns = [

# 	path("", home_page, name='home'),
# 	path("lists/the-only-list-in-the-world/", view_list, name='view_list'),


# ]













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