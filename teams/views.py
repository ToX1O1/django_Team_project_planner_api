from django.shortcuts import render
from .implementation import TeamImplementation
import json
from django.http  import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .implementation import TeamImplementation
from .serializers import TeamSerializer
from rest_framework.views import APIView

team_impl = TeamImplementation()

@api_view(['POST'])
def create_team(request):
        # Handle POST request for creating a team
        # ser = TeamSerializer(data=request.data)
        # print(ser.is_valid())
        try: 
            response = team_impl.create_team(request.body)
            return Response(response, status=200)
        except ValueError as e:
            return Response({'error': str(e)}, status=400)

@api_view(['GET'])
def list_teams(request):
        # Handle GET request for listing all teams
        try:
            response = team_impl.list_teams()
            return Response(response, status=200)
        except ValueError as e:
            return Response({'error': str(e)}, status=400)


@api_view(['POST'])
def describe_team(request):
    try:
        response = team_impl.describe_team(request.data)
        return Response(response, status=200)
    except ValueError as e:
        return Response({'error': str(e)}, status=400)


@api_view(['POST'])
def update_team(request):
        try:
            response = team_impl.update_team(request.data)
            return Response(response, status=200)
        except ValueError as e:
            return Response({'error': str(e)}, status=400)

@api_view(['POST'])
def add_user(request):
    try:
        response = team_impl.add_users_to_team(request.data)
        return Response(response, status=200)
    except ValueError as e:
        return Response({'error': str(e)}, status=400)

@api_view(['POST'])
def delete_user(request):
    try:
        response = team_impl.remove_users_from_team(request.data)
        return Response(response, status=200)
    except ValueError as e:
        return Response({'error': str(e)}, status=400)


@api_view(['POST'])
def list_team_user(request):
    try:
        response = team_impl.list_team_users(request.data)
        return Response(response, status=200)
    except ValueError as e:
        return Response({'error': str(e)}, status=400)
