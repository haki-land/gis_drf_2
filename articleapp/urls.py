from django.urls import path
from articleapp.views import ArticleCreateAPIView, ArticleTemplateView, ArticleRUDAPIView

app_name = 'articleapp'

urlpatterns = [
    path('create_template/', ArticleTemplateView.as_view(), name='create_template'),
    path('', ArticleCreateAPIView.as_view(), name='create'),
    path('<int:pk>', ArticleRUDAPIView.as_view(), name='RUD'),
]