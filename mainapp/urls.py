from django.conf import settings
from django.conf.urls.static import static
from mainapp import views
from django.urls import path, include
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('courses_list/', views.CoursesListView.as_view(), name='courses_list'),
    path('courses_list/<int:pk>/detail/', views.CourseDetailView.as_view(), name='courses_detail'),
    path('courses/feedback/', views.CourseFeedbackCreateView.as_view(), name='courses_feedback'),
    path('doc_site/', views.DocSiteView.as_view(), name='doc_site'),
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),

    # News
    path('news_list/', views.NewsListView.as_view(), name='news'),
    path('news_list/add/', views.NewsCreateView.as_view(), name='news_create'),
    path('news_list/<int:pk>/update/', views.NewsUpdateView.as_view(), name='news_update'),
    path('news_list/<int:pk>/detail/', views.NewsDetailView.as_view(), name='news_detail'),
    path('news_list/<int:pk>/delete/', views.NewsDeleteView.as_view(), name='news_delete'),
]
