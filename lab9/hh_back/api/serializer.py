from rest_framework import serializers
from api.models import Company
from api.models import Vacancy

class ApiCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'name', 'description', 'city', 'address'
        )

class ApiVacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = (
            'name', 'description', 'salary', 'company'
        )

