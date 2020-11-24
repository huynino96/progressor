from django.http import JsonResponse
from rest_framework.decorators import api_view
from scripts.count_class import count_class
from scripts.count_comment import count_comment
from scripts.count_file_and_folder import count_file_and_folder
from scripts.count_library import count_library
from scripts.count_line_of_code import count_line_of_code
from scripts.count_method import count_method
from scripts.count_testing import count_testing


@api_view(["GET"])
def counter_class(request):
    counter = count_class()
    return JsonResponse(counter, safe=False)


@api_view(["GET"])
def counter_comment(request):
    counter = count_comment()
    return JsonResponse(counter, safe=False)


@api_view(["GET"])
def counter_file_and_folder(request):
    counter = count_file_and_folder()
    return JsonResponse(counter, safe=False)


@api_view(["GET"])
def counter_library(request):
    counter = count_library()
    return JsonResponse(counter, safe=False)


@api_view(["GET"])
def counter_line_of_code(request):
    counter = count_line_of_code()
    return JsonResponse(counter, safe=False)


@api_view(["GET"])
def counter_method(request):
    counter = count_method()
    return JsonResponse(counter, safe=False)


@api_view(["GET"])
def counter_testing(request):
    counter = count_testing()
    return JsonResponse(counter, safe=False)
