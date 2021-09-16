from django.contrib.auth import get_user_model
from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import General_info, Project, Jobs
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

User = get_user_model()

def home(request):
    projects = Project.objects
    general_info = General_info.objects
    jobs = Jobs.objects

    return render(request, 'projects/home.html',{
        'projects': projects,
        'general_info': general_info,
        'jobs': jobs})

def detail(request, project_id):
    project_detail = get_object_or_404(Project, pk= project_id)
    return render(request, 'projects/detail.html', {'project': project_detail})


# def get_data(request, *args, **kwargs):
#     data = {
#         "sales": 100,
#         "customers": 10,
#     }
#     return JsonResponse(data)

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels = ['Users', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
        default_items = [qs_count, 125, 129, 50, 75, 123]
        data = {
        "labels": labels,
        "default": default_items,
        }
        return Response(data)