# # https://www.obeythetestinggoat.com/book/chapter_unit_test_first_view.html

# from django.test import TestCase

# # Create your tests here.

# class SmokeTest(TestCase):        # this test was made to fail 

#     def test_bad_maths(self):
#         self.assertEqual(1 + 1, 3)





from django.urls import resolve
from django.test import TestCase
from lists.views import home_page  

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, home_page)  








# from django.urls import resolve
# from django.urls import Resolver404, resolve, reverse
# from django.test import TestCase
# from lists.views import lists_page  

# class ListsPageTest(TestCase):

#     def test_root_url_resolves_to_lists_page_view(self):
#         found = resolve('lists_page/')  
#         self.assertEqual(found.func, lists_page)  






# from django.urls import resolve
# from django.urls import Resolver404, resolve, reverse
# from django.test import TestCase
# from lists.views import lists_page 
# from django.http import HttpResponse, HttpRequest

# class ListsPageTests(TestCase):
#     def test_url_exists_at_correct_location(self):
#         response = self.client.get("/lists/home/")
#         self.assertEqual(response.status_code, 200)

#     def test_url_available_by_name(self):  
#         response = self.client.get(reverse("home"))
#         self.assertEqual(response.status_code, 200)

#     def test_template_name_correct(self):  
#         response = self.client.get(reverse("home"))
#         self.assertTemplateUsed(response, "home.html")

#     def test_template_content(self):
#         response = self.client.get(reverse("home"))
#         self.assertContains(response, '<html><title>To-Do lists</title></html>')
#         self.assertNotContains(response, "Not on the page")

#     def test_lists_page_returns_correct_html(self): # another way to test content on lists_page
#         request = HttpRequest()  
#         response = lists_page(request)  
#         html = response.content.decode('utf8')  
#         self.assertTrue(html.startswith("<html>"))
#         self.assertIn('<title>To-Do lists</title>', html)  
#         self.assertTrue(html.endswith('</html>'))  


