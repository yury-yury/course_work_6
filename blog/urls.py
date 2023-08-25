from django.urls import path
from django.views.decorators.cache import never_cache

from blog.apps import BlogConfig
from blog.views import BlogEntryCreateView, BlogEntryListView, BlogEntryDetailView, BlogEntryUpdateView
from blog.views import BlogEntryDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', never_cache(BlogEntryCreateView.as_view()), name='create'),
    path('list/', BlogEntryListView.as_view(), name='list'),
    path('detail/<int:pk>', never_cache(BlogEntryDetailView.as_view()), name='detail'),
    path('update/<int:pk>', never_cache(BlogEntryUpdateView.as_view()), name='update'),
    path('delete/<int:pk>', never_cache(BlogEntryDeleteView.as_view()), name='delete'),
]