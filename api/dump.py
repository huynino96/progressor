from classes.script import Script
from random import randrange
from .models import Github, Language, Media
from datetime import timedelta, date


def random_language(start, stop, type, lang):
    return {
        'javascript': randrange(start, stop) if lang['javascript'] is True else 0,
        'java': randrange(start, stop) if lang['java'] is True else 0,
        'python': randrange(start, stop) if lang['python'] is True else 0,
        'php': randrange(start, stop) if lang['php'] is True else 0,
        'type': type,
    }


def dump_data():
    elements = [
        {
            'repository': 'kagkarlsson/db-scheduler',
            'javascript': False,
            'java': True,
            'php': False,
            'python': False,
        },
        {
            'repository': 'axios/axios',
            'javascript': True,
            'java': False,
            'php': False,
            'python': False,
        },
        {
            'repository': 'Pylons/deform',
            'javascript': True,
            'python': True,
            'java': False,
            'php': False,
        },
        {
            'repository': 'sebastianbergmann/php-timer',
            'php': True,
            'java': False,
            'javascript': True,
            'python': False,
        },
    ]

    for element in elements:

        repository = element['repository']

        # If not exists, then create one
        try:
            github = Github.objects.get(repository=repository)
        except Github.DoesNotExist:
            github = Github(repository=repository)
            github.save()

        start_date = date(2018, 1, 1)
        end_date = date(2021, 1, 6)
        delta = timedelta(days=1)

        while start_date <= end_date:
            classes = random_language(10, 99, 'class', element)
            comments = random_language(20, 999, 'comment', element)
            libraries = random_language(15, 99, 'library', element)
            line_of_codes = random_language(30, 99999, 'line_of_code', element)
            methods = random_language(29, 299, 'method', element)
            tests = random_language(12, 99, 'test', element)
            folders = randrange(6, 29)
            files_and_folders = {
                'folder': folders,
                'file': randrange(folders + 20, 999),
            }

            # Save data from github into database
            languages = [
                classes,
                comments,
                libraries,
                line_of_codes,
                methods,
                tests
            ]

            for item in languages:
                language = Language(
                    github=github,
                    javascript=item['javascript'],
                    java=item['java'],
                    python=item['python'],
                    php=item['php'],
                    type=item['type'],
                    date=start_date
                )
                language.save()

            # Save data from files_and_folders into database
            media = Media(
                github=github,
                file=files_and_folders['file'],
                folder=files_and_folders['folder'],
                date=start_date
            )
            media.save()
            start_date += delta
            print(start_date)
