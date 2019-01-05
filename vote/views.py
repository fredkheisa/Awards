from django.shortcuts import render, redirect, get_object_or_404
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm, ProfileForm, DesignForm, ContentForm, UsabilityForm
from .models import Project, Profile
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfSerializer, ProjectSerializer
from .permissions import IsAuthenticatedOrReadOnly
from rest_framework import status

# Create your views here.
