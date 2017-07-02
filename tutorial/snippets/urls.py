from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from snippets import views
from django.conf.urls import include



# 라우터를 생성하고 뷰셋을 등록합니다
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
