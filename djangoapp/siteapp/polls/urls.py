from django.urls import path
from . import views

urlpatterns = [
    path("raw", views.raw_index, name="index"),
    path("profile", views.profile, name="profile"),
    path("contact", views.contact, name="contact"),
    path("", views.html_index, name="html_index"),
    path("html", views.html_version, name="html_version"),
    path("other", views.index_other, name="index_other"),
    path('submit/<int:question_id>/', views.submit_vote, name='submit_vote'),
    path("address", views.address, name="address"),
    path("phone", views.phone, name="phone"),
]