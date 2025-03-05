from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse
# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"

# def home_page_view(request: HttpRequest) -> HttpResponse:
#     context = {
#         "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
#         "greeting": "Thank you for visiting."
#     }
#     return render(request, "home.html", context)

# # def about_page_view(request: HttpRequest) -> HttpResponse:
# #     context = {
# #         "name": "Miguel",
# #         "age": 32
# #     }
    
# #     return render(request, "pages/about.html", context)

# class AboutPageView(TemplateView): 
#     template_name = "about.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["contact_address"] = "123 Main Street"
#         context["phone_number"] = "555-555-5555"
#         return context