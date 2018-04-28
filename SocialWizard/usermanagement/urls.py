from django.conf.urls import url
from usermanagement import views
from usermanagement import login_views
urlpatterns = [
    url(r'^signup$', views.SignUp.as_view()),
    url(r'^login$', login_views.LoginView.as_view())
]