from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from rest_framework.decorators import api_view
from scripts.count_class import count_class
from scripts.count_comment import count_comment
from scripts.count_file_and_folder import count_file_and_folder
from scripts.count_library import count_library
from scripts.count_line_of_code import count_line_of_code
from scripts.count_method import count_method
from scripts.count_testing import count_testing
from .models import Language, Media, Comment, Library, LOC, Method, Testing
from .serializers import LanguageSerializer
from classes.crud import create_count_class, create_count_file_and_folder, create_count_comment, create_count_library, create_count_loc, create_count_method, create_count_testing

@api_view(["POST"])
def create_counter_class(request, author, repository):
    counter = count_class(author + '/' + repository)

    for data in counter:
        create_count_class(data, author + '/' + repository)
    
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def create_counter_file_and_folder(request, author, repository):
    counter = count_file_and_folder(author + '/' + repository)
    
    for data in counter:
        create_count_file_and_folder(data, author + '/' + repository)

    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def create_counter_comment(request, author, repository):
    counter = count_comment(author + '/' + repository)
    
    for data in counter:
        create_count_comment(data, author + '/' + repository)

    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def create_counter_library(request, author, repository):
    counter = count_library(author + '/' + repository)
    
    for data in counter:
        create_count_library(data, author + '/' + repository)

    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def create_counter_loc(request, author, repository):
    counter = count_line_of_code(author + '/' + repository)
    
    for data in counter:
        create_count_loc(data, author + '/' + repository)

    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def create_counter_method(request, author, repository):
    counter = count_method(author + '/' + repository)
    
    for data in counter:
        create_count_method(data, author + '/' + repository)

    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def create_counter_testing(request, author, repository):
    counter = count_testing(author + '/' + repository)
    
    for data in counter:
        create_count_testing(data, author + '/' + repository)

    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET"])
def counter_class(request, author, repository):
    counter = Language.objects.all().filter(github=author+'/'+repository).order_by('id').values()

    return Response(counter, status=status.HTTP_200_OK)

@api_view(["GET"])
def counter_file_and_folder(request, author, repository):
    counter = Media.objects.all().filter(github=author + '/' + repository).order_by('id').values()

    return Response(counter, status=status.HTTP_200_OK)

@api_view(["GET"])
def counter_comment(request, author, repository):
    counter = Comment.objects.all().filter(github=author+'/'+repository).order_by('id').values()

    return Response(counter, status=status.HTTP_200_OK)

@api_view(["GET"])
def counter_library(request, author, repository):
    counter = Library.objects.all().filter(github=author+'/'+repository).order_by('id').values()

    return Response(counter, status=status.HTTP_200_OK)

@api_view(["GET"])
def counter_loc(request, author, repository):
    counter = LOC.objects.all().filter(github=author+'/'+repository).order_by('id').values()

    return Response(counter, status=status.HTTP_200_OK)

@api_view(["GET"])
def counter_method(request, author, repository):
    counter = Method.objects.all().filter(github=author+'/'+repository).order_by('id').values()

    return Response(counter, status=status.HTTP_200_OK)

@api_view(["GET"])
def counter_testing(request, author, repository):
    counter = Testing.objects.all().filter(github=author+'/'+repository).order_by('id').values()

    return Response(counter, status=status.HTTP_200_OK)

