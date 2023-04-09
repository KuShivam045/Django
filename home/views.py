from django.shortcuts import render
from .serializers import *
from .queries import *
from rest_framework import status as stus
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view , authentication_classes , permission_classes

# Create your views here.

###########################################Movies_Insert#######################################################

@api_view(["POST"])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def insert1(request):
    try:
        serializer = insertSerializer(data= request.data)

        # print('111111111111111')
        if serializer.is_valid():
            Title = serializer.data["Title"] 
            genre = serializer.data["genre"]
            cast = serializer.data["cast"]
            director = serializer.data["director"] 
            release_year = serializer.data["release_year"]


            # print(release_year)
            # print('2222222222222222')
            data = {
                'Title' : Title,
                'genre' : genre,
                'cast' : cast,
                'director' : director,
                'release_year' : release_year
            }

            # print(data.values())
            insert = insert_q(data.values())

            # print(insert,'ncdhxfh')
            if insert:
                json_data = {
                    "status code" : 200,
                    "status" : "Succes",
                    "message" : "Data Inserted Successfully"
                }
                return Response(json_data)
            else:
                json_data = {
                    "status code" : 400,
                    "status" : "Succes",
                    "message" : "Data Insertion Failed!"
                }
                return Response(json_data)

        else:
            json_data = {
                "status code" : False,
                "status" : "Succes",
                "message" : serializer.errors
                }
            return Response(json_data)
    except Exception as e:

        print("Error ..................")

        json_data = {
            "status code" : 400,
            "status" : "Fail",
            "Reason" : e,
            "message" :"Landed in Exception"
            }
        return Response(json_data)

#########################################Employee_Data_Insert##################################################

@api_view(["POST"])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def employee(request):
    try:
        serializer = employeeSerializer(data=request.data)
        if serializer.is_valid():
            EmployeeID =serializer.data["EmployeeID"]
            FirstName = serializer.data["FirstName"]
            LastName = serializer.data["LastName"]
            EmployeeProfile = serializer.data["EmployeeProfile"]
            DateofJoining = serializer.data["DateofJoining"]
            CompanyAddress = serializer.data["CompanyAddress"]
            City = serializer.data["City"]

            data = {
                'EmployeeID': EmployeeID,
                'FirstName' : FirstName,
                'LastName' : LastName,
                'EmployeeProfile' : EmployeeProfile,
                'DateofJoining' : DateofJoining,
                'CompanyAddress' : CompanyAddress,
                'City' : City
            }

            insert = insert_r(data.values())
            if insert:
                json_data  = {
                    'status code' : 200,
                    'status' : 'success',
                    'message' : "Data Inserted Successfully"
                }
                return Response(json_data)
            else:
                json_data = {
                    'status code' : 400,
                    'status' : 'failed',
                    'message' : "Data Insertion failed"
                }
                return Response(json_data)
        else:
            json_data = {
            'status' : False,
            'message' : "Invalid request",
            'data' : serializer.errors
            }
            return Response(json_data)
    except Exception as e:

        print("Error...........", e)
        json_data = {
            'status code' : 400,
            'status' : 'Fail',
            'reason': e,
            'remark': 'Landed in exception' 
        }
        return Response(json_data)
        




############################################Read_Data#########################################################



@api_view(["POST"])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def view_data(request):
    try:
        # print('111111111111111111')
        serializer = ViewSerializer(data= request.data)
        if serializer.is_valid():
            # print('222222222')
            name = serializer.data['ID']
            # print(name)
            # print("4654689879879853464987")
            fetchedData = readData(name)

            if fetchedData:
                json_data = {
                    'status' : 'Pass',
                    'data' : fetchedData
                }
                return Response(json_data)
            else:
                json_data = {
                    'status' : 'Pass',
                    'message' : "No data found with specific key"
                }
                return Response(json_data)
        else:
            json_data = {
                'status code' : False,
                'status' : 'Bad REquest',
                'message' : serializer.errors 
            }
            return Response(json_data)
    except Exception as e:
        json_data = {
            "status" : "Failed",
            'reason' : e,
            'remark' : "Landed in Exception"

        }
        return Response(json_data)
    



######################################Update_Employee_Table_Data###############################################




@api_view(["POST"])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def update_(request):
    try:
        serializer = updateSerializer(data = request.data)
        if serializer.is_valid():
            ID_ = serializer.data['ID']
            # print("11111111111111")
            old_data = readData(ID_)
            # print(old_data)
            # print(old_data["DateofJoining"])
            # print(serializer.data["DateofJoining"])
            # print(serializer.data["EmployeeID"])
            # print(serializer.data["FirstName"])
            # print(serializer.data["LastName"])
            # print(serializer.data["EmployeeProfile"])
   
            data = {
                'EmployeeID': serializer.data["EmployeeID"] if serializer.data["EmployeeID"] else old_data["EmployeeID"],
                'FirstName' : serializer.data["FirstName"] if serializer.data["FirstName"] else old_data["FirstName"],
                'LastName' : serializer.data["LastName"] if serializer.data["LastName"] else old_data["LastName"],
                'EmployeeProfile' : serializer.data["EmployeeProfile"] if serializer.data["EmployeeProfile"] else old_data["EmployeeProfile"],
                'DateofJoining' : serializer.data["DateofJoining"] if serializer.data["DateofJoining"] else old_data["DateofJoining"],
                'CompanyAddress' : serializer.data["CompanyAddress"] if serializer.data["CompanyAddress"] else old_data["CompanyAddress"],
                'City' : serializer.data["City"] if serializer.data["City"] else old_data["City"],
                'ID':ID_
            }
            # print("222222222222222222222")
            print(data)
            update = updateData(data.values())
            # print("333333333333333")
            # print(update)
            if update:
                json_data  = {
                    'status code' : 200,
                    'status' : 'success',
                    'message' : "Data updated Successfully"
                }
                return Response(json_data)
            else:
                json_data  = {
                        'status code' : 400,
                        'status' : 'success',
                        'message' : "Cannot update Data "
                    }
                return Response(json_data)
          
        else:
            json_data = {
                'status code' : False,
                'status' : 'Bad REquest',
                'message' : serializer.errors 
            }
            return Response(json_data )
    except:
        pass


