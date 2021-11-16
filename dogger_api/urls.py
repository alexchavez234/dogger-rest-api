from django.urls import path, include
from rest_framework.routers import DefaultRouter

from dogger_api import views

router = DefaultRouter()
router.register(r'hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register(r'profile', views.UserProfileViewSet)

urlpatterns=[
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]