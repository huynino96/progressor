from classes.script import Script
from .models import Github, Language, Media


def scheduled_job():
    repositories = [
        'kagkarlsson/db-scheduler',
        'axios/axios',
        'Pylons/deform',
        'sebastianbergmann/php-timer',
    ]

    for repository in repositories:

        # If not exists, then create one
        try:
            github = Github.objects.get(repository=repository)
        except Github.DoesNotExist:
            github = Github(repository=repository)
            github.save()

        # Get data from github
        script = Script()
        script.set_repository(repository)
        script.get_contents()
        classes = script.count_class()
        comments = script.count_comment()
        libraries = count_library()
        line_of_codes = count_line_of_code()
        methods = count_method()
        tests = count_testing()
        files_and_folders = script.count_file_and_folder()

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
            )
            language.save()

        # Save data from files_and_folders into database
        media = Media(github=github, file=files_and_folders['file'], folder=files_and_folders['folder'])
        media.save()
