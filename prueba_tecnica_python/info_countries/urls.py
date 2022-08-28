from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api import *

router = DefaultRouter()

router.register('country', CountryAPI)
router.register('language', LanguageCountryAPI)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/1.0/infoCountryLanguage/', InfoCountries.as_view())
]