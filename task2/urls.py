from django.urls import path

from task2.views import ReviewEmailView

app_name = "task2"

urlpatterns = [
    path("review/", ReviewEmailView.as_view(), name="reviews"),
]
