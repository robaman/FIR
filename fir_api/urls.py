from django.conf.urls import include, url
from rest_framework import routers
from rest_framework.authtoken import views as token_views

from fir_api import views

# automatic URL routing for API
# include login URLs for the browsable API.
router = routers.DefaultRouter(trailing_slash=False)

router.register(r'users', views.UserViewSet, base_name='users')
router.register(r'incidents', views.IncidentViewSet, base_name='incidents')
router.register(r'artifacts', views.ArtifactViewSet, base_name='artifacts')
router.register(r'files', views.FileViewSet, base_name='files')
router.register(r'comments', views.CommentViewSet, base_name='comments')
router.register(r'labels', views.LabelViewSet, base_name='labels')

# urls for core FIR components
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^token/', token_views.obtain_auth_token),
]
