from django.shortcuts import render
from .implementations import UserImplementation
import json
from django.http  import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer

# Create your views here.
user_impl = UserImplementation()

@api_view(['POST'])
def create_user(request):
    ser = UserSerializer(data=request.data)
    ser.is_valid()
    try:
        user_data = {
                    'name': ser.data.get('name'),
                    'display_name': ser.data.get('display_name')
                }
        response = user_impl.create_user(json.dumps(user_data))
        return HttpResponse(response,content_type='application/json')
    except ValueError as e:
        return HttpResponse(json.dumps({'error': str(e)}), status=400, content_type='application/json')
    

@api_view()
def list_users(request):
    users = user_impl.list_users()
    ser = UserSerializer(users,many=True)
    for i in (ser.data) :
        del i['description']
    return Response(ser.data)


@api_view(['POST','GET'])
def describe_user_view(request):
    ser = (request.data)
   
    try:
        user_info = user_impl.describe_user(ser)
        return Response(user_info)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@api_view(['POST','GET']) 
def update_user_view(request):    
    try:
        response = user_impl.update_user(request.data)
        return Response(response)
    except Exception as e:
        return Response({'error': str(e)}, status=400)


@api_view(['POST'])
def get_user_teams_view(request):
    print(request.data)
    try:
        request_data = request.data
        teams = user_impl.get_user_teams(request_data)
        return JsonResponse(teams)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)