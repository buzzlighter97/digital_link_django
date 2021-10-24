from django.http.response import HttpResponseBadRequest
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .serializers import NumbersSerializer, FoundSerializer
import json
import http
import openpyxl

def generate_response(found):
    found_dict = {"found": found}
    serializer = FoundSerializer(data=found_dict)
    serializer.is_valid(raise_exception=True)
    return Response(serializer.validated_data, status=200)


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        number = request.GET.get('number')
        with open('stoplist.json') as stoplist:
            data = json.loads(stoplist.read())
            for i in range(len(data)):
                if data[i]['number'] == number:
                    return generate_response(1)
                else:
                    return generate_response(0)
    if request.method == 'POST':
        excel_files = request.FILES

        for excel_file_name in excel_files.keys():

            excel_file = excel_files[excel_file_name]

            wb = openpyxl.load_workbook(excel_file)

            worksheet = wb.active

            excel_data = list()
            for row in worksheet.values:
                excel_data.append({"number": str(row[0])})
            
            print()
            print(excel_data)
            print()

            with open("stoplist.json", "r+") as file:
                data = json.load(file)
                for i in range(len(excel_data)):
                    data.append(excel_data[i])
                file.seek(0)
                json.dump(data, file)
            
        return Response(status=200)