from django.urls import path
from webpem import views, views_api

app_name = 'webpem'
urlpatterns = [
    path('', views.readStudent, name='read-data-student'),
    path('create/', views.createStudent, name='create-data-student'),
    path('update/<str:id>', views.updateStudent, name='update-data-student'),
    path('delete/<str:id>', views.deleteStudent, name='delete-data-student'),

#urls untuk Course
    path('read/course', views.readCourse, name='read-data-course'),
    path('create/course', views.createCourse, name='create-data-course'),
    path('update/course', views.updateCourse, name='update-data-course'),
    path('delete/course', views.deleteCourse, name='delete-data-course'),
#urls untuk API
   path('api/course', views_api.apiCourse, name='api-view-data-course'),
]
