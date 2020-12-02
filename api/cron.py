from scripts.count_class import count_class
from scripts.count_comment import count_comment
from scripts.count_file_and_folder import count_file_and_folder
from scripts.count_library import count_library
from scripts.count_line_of_code import count_line_of_code
from scripts.count_method import count_method
from scripts.count_testing import count_testing
from .models import Github, Language, Media


def scheduled_job():
    repositories = [
        'kagkarlsson/db-scheduler',
        'axios/axios',
        'Pylons/deform',
        'sebastianbergmann/php-timer',
    ]

    for repository in repositories:
        classes = count_class(repository)
        comments = count_comment(repository)
        files_and_folders = count_file_and_folder(repository)
        libraries = count_library(repository)
        line_of_codes = count_line_of_code(repository)
        methods = count_method(repository)
        tests = count_testing(repository)
        