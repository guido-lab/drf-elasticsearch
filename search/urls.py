
from django.urls import path

from search.views import SearchArticles, SearchArticlesV2, SearchCategories, SearchUsers

urlpatterns = [
    path('user/<str:query>/', SearchUsers.as_view()),
    path('category/<str:query>/', SearchCategories.as_view()),
    path('article/<str:query>/', SearchArticles.as_view()),
    path('article-custom/', SearchArticlesV2.as_view()),
]
