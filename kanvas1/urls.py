from django.urls import path 
from .views import UserView, LoginView, CourseView

urlpatterns = [
    path('accounts/', UserView.as_view()),
    path('login/', LoginView.as_view()),
    path('courses/', CourseView.as_view()),
    path('courses/<int:course_id>/registrations/', CourseView.as_view())
    
]