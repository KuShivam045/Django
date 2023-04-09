from rest_framework import serializers
from rest_framework.settings import api_settings

class insertSerializer(serializers.Serializer):
    Title = serializers.CharField(required = True)
    genre = serializers.CharField(required = True)
    cast = serializers.CharField(required = True)
    director = serializers.CharField(required = False,  allow_blank=True, allow_null = True)
    release_year = serializers.CharField(required = True)

    class Meta:
        fields = '__all__'


class employeeSerializer(serializers.Serializer):
    EmployeeID = serializers.IntegerField(required=True)
    FirstName = serializers.CharField(required=True)
    LastName = serializers.CharField(required=True)
    EmployeeProfile = serializers.CharField(required=True)
    DateofJoining = serializers.DateField(required=True)
    CompanyAddress = serializers.CharField(required=True)
    City = serializers.CharField(required=True)
    
    class Meta:
        fields='__all__'


class ViewSerializer(serializers.Serializer):
    ID=serializers.IntegerField(required=True)
    class Meta:
        fields='__all__'


class updateSerializer(serializers.Serializer):
    ID = serializers.IntegerField(required=True)
    EmployeeID = serializers.IntegerField(required=False,max_value=None, min_value=None,allow_null =True)
    FirstName = serializers.CharField(required=False, allow_blank = True, allow_null = True)
    LastName = serializers.CharField(required=False, allow_blank = True, allow_null = True)
    EmployeeProfile = serializers.CharField(required=False, allow_blank = True, allow_null = True)
    DateofJoining = serializers.DateField(required=False, format=api_settings.DATE_FORMAT, input_formats= None,allow_null =True)
    CompanyAddress = serializers.CharField(required=False, allow_blank = True, allow_null = True)
    City = serializers.CharField(required=False, allow_blank = True, allow_null = True)
    
    class Meta:
        fields='__all__'