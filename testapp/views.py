from django.shortcuts import render
from django.views.generic import View
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import EmployeeSerializer
from .models import Employee
from django.http import HttpResponse
from  django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCRUDCBV(View):
    def get(self, request):
        json_data = request.body  # Receive the data coming from test application
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream) # Converting to python dictionary
        id = pdata.get('id')

        if id is not None:
            #Serialization
            emp = Employee.objects.get(id = id) # Database object
            serializer = EmployeeSerializer(emp) # Converting Database object to python Dictionary
            json_data = JSONRenderer().render(serializer.data) # Converting python Dictionary to json data
            return HttpResponse(json_data, content_type='application/json') # Returning that json data
        #Serialization
        qs = Employee.objects.all()
        serializer = EmployeeSerializer(qs, many = True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type = 'application/json')

    def post(self, request, *args, **kwargs):
        #Deserialization
        json_data = request.body  # Json Object
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)  # Converting json data to python dictionary
        serializer = EmployeeSerializer(data = pdata) # Converting python data to DB supported object

        if serializer.is_valid():
            serializer.save() # Saving the db supported object to Database
            msg = {'msg' : 'Resource Created Successfully'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type = 'application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json', status = 400)

    def put(self, request, *args, **kwargs):
        # Deserialization
        json_data = request.body # Json Object
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream) # Converting json data to python dictionary
        emp = Employee.objects.get(id = pdata.get('id'))
        serializer = EmployeeSerializer(emp, data=pdata, partial = True) # Converting python data to DB supported object
        if serializer.is_valid():
            serializer.save() # Saving the db supported object to Database
            msg = {'msg':'Resource Updated Successfully'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type = 'application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json', status = 400)

    #For delete operation there is no need of serializers concept
    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        emp = Employee.objects.get(id = pdata.get('id'))
        emp.delete()
        msg = {'msg':'Resource deleted successfully'}
        json_data = JSONRenderer().render(msg)
        return  HttpResponse(json_data, content_type = 'application/json')



