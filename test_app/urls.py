from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [

]

router = DefaultRouter()
router.register('test', views.TestView, basename='test')
router.register('second_test', views.SecondTestView, basename='second_test')
urlpatterns += router.urls
