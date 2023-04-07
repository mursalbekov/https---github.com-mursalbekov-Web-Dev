from django.shortcuts import render
from rest_framework import generics
from api.models import Company, Vacancy
from api.serializer import ApiCompanySerializer
from api.serializer import ApiVacancySerializer

# Create your views here.
class ApiCompanyGetAll(generics.ListAPIView, generics.RetrieveDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = ApiCompanySerializer
    def __str__(self):
        return self.name

class ApiCompanyGetOne(generics.ListAPIView, generics.RetrieveDestroyAPIView):
    queryset = Company.objects.filter(id = 1)
    serializer_class = ApiCompanySerializer
    def __str__(self):
        return self.name

class ApiVacancyByCompany(generics.ListAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all().filter(id = 2).order_by('company')
    serializer_class = ApiCompanySerializer
    def __str__(self):
        return self.name
    
class ApiListOfAllVacancies(generics.ListAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = ApiVacancySerializer
    def __str__(self):
        return self.name
    
class ApiGetOneVacancy(generics.ListAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.filter(id = 1)
    serializer_class = ApiVacancySerializer
    def __str__(self):
        return self.name
    
class ApiSortedVacancies(generics.ListAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all().order_by('-salary')[:5]
    serializer_class = ApiVacancySerializer
    def __str__(self):
        return self.name

    