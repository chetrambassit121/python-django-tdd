from django.urls import resolve
from django.test import TestCase
from lists.views import home_page  

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, home_page)  

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')  

        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'home.html')  
        # self.assertTemplateUsed(response, 'wrong.html')






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


