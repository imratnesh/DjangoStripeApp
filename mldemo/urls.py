# api/urls.py
from django.urls import include, path
from .views import Predict
app_name = 'ml'

urlpatterns = [
    # path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('predict/', Predict.as_view(), name='predict')
    path('predictSentiment/', Predict.as_view(), name='predict')
]
