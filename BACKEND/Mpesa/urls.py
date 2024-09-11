from django.urls import path, include
from . import views
from .views import home, STKPushView, oauth_success

test_patterns = [
    path('', home, name='home'),
    path('stk-push/', STKPushView.as_view(), name='stk_push'),
    path('oauth-success/', oauth_success, name='oauth_success'),
]


urlpatterns = [
    path('', views.home, name='index'),
    path('tests/', include(test_patterns)),
]