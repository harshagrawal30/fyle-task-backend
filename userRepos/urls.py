from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register('user',views.Userviewlist,basename='userlist')
urlpatterns = [
    # path('', views.Userviewlist.as_view(), name='userlist'),
     path('api/',include(router.urls)),
]