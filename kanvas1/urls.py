from django.urls import path 
from .views import UserView, LoginView, CourseView, ActivitiesView, StudentActivitiesView, EditaNotaView
urlpatterns = [


    # post get instrutor ou facilitador
    path('activities/', ActivitiesView.as_view()),

    # post estudante
    path('activities/<int:activitie_id>/submissions/', StudentActivitiesView.as_view()),


    # PUT estudante
    path('submissions/<int:submission_id>/', EditaNotaView.as_view()),

    # GET estudante
    

    #


    # POST PUT DELETE INSTRUTOR, GET QUAL QUER UM ATÈ SEM TOKEN
    path('courses/', CourseView.as_view()),
    path('courses/<int:course_id>/', CourseView.as_view()),
    path('accounts/', UserView.as_view()),
    path('courses/<int:course_id>/registrations/', CourseView.as_view()),  
      
    # path('courses/', LivreView.as_view()),
    # path('courses/<int:course_id>/', LivreView.as_view()),
    # path('accounts/', LoginView.as_view()),
    # path('courses/<int:course_id>/registrations/', LivreView.as_view()),   


    path('login/', LoginView.as_view()),


    path('submissions/', StudentActivitiesView.as_view())

]

