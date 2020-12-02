from datetime import date, timedelta
from random import randrange


def count_programming(current_date, javascript, java, python, php, random=True):
    if random:
        javascript = randrange(javascript) if javascript > 0 else 0
        java = randrange(java) if java > 0 else 0
        python = randrange(python) if python > 0 else 0
        php = randrange(php) if php > 0 else 0
    return {
        'date': current_date,
        'total': javascript + java + python + php,
        'javascript': javascript,
        'java': java,
        'python': python,
        'php': php
    }


def count_file_and_folder(current_date, file, folder, random=True):
    if random:
        file = randrange(file) if file > 0 else 0
        folder = randrange(folder) if folder > 0 else 0
    return {
        'date': current_date,
        'file': file,
        'folder': folder,
    }


def generate_dates(javascript, java, python, php):
    today = date.today()
    return [
        count_programming(today - timedelta(6), javascript, java, python, php),
        count_programming(today - timedelta(5), javascript, java, python, php),
        count_programming(today - timedelta(4), javascript, java, python, php),
        count_programming(today - timedelta(3), javascript, java, python, php),
        count_programming(today - timedelta(2), javascript, java, python, php),
        count_programming(today - timedelta(1), javascript, java, python, php),
        count_programming(today, javascript, java, python, php, random=False)
    ]


def generate_dates_file_and_folder(file, folder):
    today = date.today()
    return [
        count_file_and_folder(today - timedelta(6), file, folder),
        count_file_and_folder(today - timedelta(5), file, folder),
        count_file_and_folder(today - timedelta(4), file, folder),
        count_file_and_folder(today - timedelta(3), file, folder),
        count_file_and_folder(today - timedelta(2), file, folder),
        count_file_and_folder(today - timedelta(1), file, folder),
        count_file_and_folder(today, file, folder, random=False),
    ]

