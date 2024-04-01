from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json
from .implementation import ProjectBoardImplementation
from rest_framework.decorators import api_view
from rest_framework.response import Response

project_board_impl = ProjectBoardImplementation()

@api_view(['POST'])
def create_board(request):
    data = request.body
    try:
        response = project_board_impl.create_board(data)
    except ValueError as e:
            return Response({'error': str(e)}, status=400)

    return Response(response)

@api_view(['POST'])
def close_board(request):
        data = request.body
        response = project_board_impl.close_board(data)
        return Response({"message": response})

@api_view(['POST'])
def add_task(request):
    data = request.body
    response = project_board_impl.add_task(data)
    return Response(response)

@api_view(['POST'])
def update_task(request):
        data = request.body
        response = project_board_impl.update_task_status(data)
        return Response({"message": response})

@api_view(['POST'])
def list_boards(request):
        data = request.body
        response = project_board_impl.list_boards(data)
        return Response(response)

@api_view(['POST'])
def export_board(request):
        data = request.body
        response = project_board_impl.export_board(data)
        return Response(response)
