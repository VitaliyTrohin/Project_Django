from mainapp import views
from django.urls import path
from django.views.decorators.cache import cache_page
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('doc_site/', views.DocSiteView.as_view(), name='doc_site'),

    # Courses
    path('courses_list/', cache_page(3600)(views.CoursesListView.as_view()), name='courses_list'),
    path('courses_list/<int:pk>/detail/', views.CourseDetailView.as_view(), name='courses_detail'),
    path('courses/feedback/', views.CourseFeedbackCreateView.as_view(), name='courses_feedback'),

    # News
    path('news_list/', views.NewsListView.as_view(), name='news'),
    path('news_list/add/', views.NewsCreateView.as_view(), name='news_create'),
    path('news_list/<int:pk>/update/', views.NewsUpdateView.as_view(), name='news_update'),
    path('news_list/<int:pk>/detail/', views.NewsDetailView.as_view(), name='news_detail'),
    path('news_list/<int:pk>/delete/', views.NewsDeleteView.as_view(), name='news_delete'),

    # Logs
    path('logs/', views.LogView.as_view(), name='logs_list'),
    path('logs/download/', views.LogDownLoadView.as_view(), name='logs_download'),
]
























