from api.models import Language
from api.serializers import LanguageSerializer, MediaSerializer, LibrarySerializer, CommentSerializer, LocSerializer, MethodSerializer, TestingSerializer

def create_count_class(data, github):
    result = {
        'github': github,
        'java': data["java"],
        'python': data["python"],
        'javascript': data["javascript"],
        'php': data["php"],
        'date': data["date"].strftime("%d-%b-%Y")
    }

    serializer = LanguageSerializer(data=result)

    if serializer.is_valid():
        serializer.save()

    return serializer.data


def create_count_comment(data, github):
    result = {
        'github': github,
        'java': data["java"],
        'python': data["python"],
        'javascript': data["javascript"],
        'php': data["php"],
        'date': data["date"].strftime("%d-%b-%Y")
    }

    serializer = CommentSerializer(data=result)

    if serializer.is_valid():
        serializer.save()

    return serializer.data

def create_count_library(data, github):
    result = {
        'github': github,
        'java': data["java"],
        'python': data["python"],
        'javascript': data["javascript"],
        'php': data["php"],
        'date': data["date"].strftime("%d-%b-%Y")
    }

    serializer = LibrarySerializer(data=result)

    if serializer.is_valid():
        serializer.save()

    return serializer.data

def create_count_loc(data, github):
    result = {
        'github': github,
        'java': data["java"],
        'python': data["python"],
        'javascript': data["javascript"],
        'php': data["php"],
        'date': data["date"].strftime("%d-%b-%Y")
    }

    serializer = LocSerializer(data=result)

    if serializer.is_valid():
        serializer.save()

    return serializer.data

def create_count_method(data, github):
    result = {
        'github': github,
        'java': data["java"],
        'python': data["python"],
        'javascript': data["javascript"],
        'php': data["php"],
        'date': data["date"].strftime("%d-%b-%Y")
    }

    serializer = MethodSerializer(data=result)

    if serializer.is_valid():
        serializer.save()

    return serializer.data


def create_count_testing(data, github):
    result = {
        'github': github,
        'java': data["java"],
        'python': data["python"],
        'javascript': data["javascript"],
        'php': data["php"],
        'date': data["date"].strftime("%d-%b-%Y")
    }

    serializer = TestingSerializer(data=result)

    if serializer.is_valid():
        serializer.save()

    return serializer.data
    
def create_count_file_and_folder(data, github):
    result = {
        'github': github,
        'file': data["file"],
        'folder': data["folder"],
        'date': data["date"].strftime("%d-%b-%Y")
    }

    serializer = MediaSerializer(data=result)

    if serializer.is_valid():
        serializer.save()

    return serializer.data