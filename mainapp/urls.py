from django.urls import path
from . import views


from .views import newsletter_signup, newsletter_unsubscribe

urlpatterns = [
  path('index', views.index, name='index'),
  path('predict/', views.predict, name='predict'),
path('', views.home, name="home"),
path('about', views.about, name="about"),
path('blog', views.blog, name="blog"),
path('faq', views.faq, name="faq"),
path('contact', views.contact, name="contact"),
path('error_404', views.error_404, name="error-404"),

  path('sign_up', views.newsletter_signup, name="newsletter_signup"),
path('unsubscribe', views.newsletter_unsubscribe, name="newsletter_unsubscribe"),

  # path('mguu', views.mguu, name="mguu"),
]


