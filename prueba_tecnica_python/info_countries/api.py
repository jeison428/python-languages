from multiprocessing import context
from re import I
import requests, time, json

import pandas as pd

from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

class CountryAPI(viewsets.ModelViewSet):
    """
    API que permite crear y consultar los regitros de la entidad Country
    Esta api hace uso del metodo POST y GET.
    PATH: 'api/country/'
    """
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

class LanguageCountryAPI(viewsets.ModelViewSet):
    """
    API que permite crear y consultar los regitros de la entidad LanguageCountry
    Esta api hace uso del metodo POST y GET.
    PATH: 'api/language/'
    """
    serializer_class = LanguageCountrySerializer
    queryset = LanguageCountry.objects.all()

class InfoCountries(APIView):
    """
    API que permite guardar la informacion de todos los paises en https://restcountries.com
    Esta api hace uso del metodo GET.
    PATH: 'api/infoCountryLanguage/'
    """
    def get(self, request, *args, **kwargs):
        URL = 'https://restcountries.com/v3.1/all'
        data = requests.get(URL) 
        data = data.json()
        df = pd.DataFrame(columns=['region','name','language','time'])
        n = 1
        for element in data: 
            start = time.process_time()
            if (element.get('languages') != None):
                for key, value in element['languages'].items():
                    country = {'region':element['region'], 'name':element['name']['common'], 'language':value}
                    end = time.process_time()
                    stimedTime = (end - start)/1000
                    country['time'] = str(stimedTime)+' ms'
                    df1 = pd.DataFrame(country, index={n})
                    df = pd.concat([df, df1], ignore_index=True)
                    n += 1
            else:
                country = {'region':element['region'], 'name':element['name']['common'], 'language':''}
                end = time.process_time()
                stimedTime = (end - start)/1000
                country['time'] = str(stimedTime)+' ms'
                df1 = pd.DataFrame(country, index={n})
                df = pd.concat([df, df1], ignore_index=True)
                n += 1
            del country['language']
            saveCountry = CountrySerializer(data=country, context=country)
            if saveCountry.is_valid():
                saveCountry.save()
            saveCountry = CountrySerializer(Country.objects.get(name=country['name'])).data
            if (element.get('languages') != None):
                for lang, value in element['languages'].items():
                    language = {'_language':value, 'country':saveCountry['id']}
                    saveLanguage = LanguageCountrySerializer(data=language, context=language)
                    if saveLanguage.is_valid():
                        saveLanguage.save()
        newJson = df.to_json()
        
        with open('data.json', 'w') as fp:
            json.dump(newJson, fp)

        with open('data.json', 'r') as fp:
            data = json.load(fp)

        return Response({"Json": data}, status = status.HTTP_200_OK)