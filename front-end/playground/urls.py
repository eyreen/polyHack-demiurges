from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.go_to_dashboard),
    path("", views.go_to_dashboard),
    path("accounts/", views.go_to_accounts),
    path("posts/", views.go_to_posts),

]