from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import password_reset, password_reset_done
from django.contrib.auth.views import (password_reset_confirm,
                                       password_reset_complete)


urlpatterns = [
    url('reset-password',
        password_reset,
        {'post_reset_redirect': reverse_lazy('password_reset_done')},
        name='password_reset'
        ),
    url('done/',
        password_reset_done,
        name='password_reset_done'
        ),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',  # token generated for each user
        password_reset_confirm,
        {'post_reset_redirect': reverse_lazy('password_reset_complete')},
        name='password_reset_confirm'
        ),
    url('complete/',
        password_reset_complete,
        name='password_reset_complete'
        ),
    ]
