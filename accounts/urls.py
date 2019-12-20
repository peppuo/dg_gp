from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile
# from accounts import url_reset


urlpatterns = [
    url('logout/', logout, name='logout'),
    url('login/', login, name='login'),
    url('register/', registration, name='registration'),
    url('profile/', user_profile, name='profile'),
    # url('password-reset/', include(url_reset)),
    ]
