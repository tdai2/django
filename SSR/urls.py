from django.urls import path, include
from rest_framework import routers
from SSR import views


router = routers.DefaultRouter()
router.register(r'skills', views.SkillViewSet)
router.register(r'accounts', views.AccountViewSet)

urlpatterns = [
    path("", views.home, name="home"),
    # path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
urlpatterns += router.urls