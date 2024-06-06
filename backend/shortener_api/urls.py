from django.urls import path
from .views import PostApiView

urlpatterns = [
    path("", PostApiView.as_view()),
    path("<int:key>/", PostApiView.as_view())
]
