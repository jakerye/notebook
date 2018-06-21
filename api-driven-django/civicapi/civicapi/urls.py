from django.contrib import admin
from django.urls import path

from votes import views as vote_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('votes/', vote_views.VoteList.as_view()),
    path('votes/<int:pk>/', vote_views.VoteDetail.as_view()),
]