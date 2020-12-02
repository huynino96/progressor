from instance import Token
from classes.helpers import generate_dates
from classes.library import Library
import json


def count_library(repository_endpoint):
    token = Token()
    token.repository_endpoint = repository_endpoint
    repo = token.get_repository()
    contents = repo.get_contents("")

    # Counter
    javascript = 0
    python = 0
    java = 0
    php = 0

    while contents:
        file_content = contents.pop(0)
        if file_content.type == 'dir':
            contents.extend(repo.get_contents(file_content.path))
        else:
            fileName = file_content.name
            library = Library(fileName)
            if library.is_python() or library.is_java() or library.is_php() or library.is_javascript():
                decoded_content = file_content.decoded_content
                inside_content = decoded_content.decode('utf-8')

                if library.is_python():
                    python = len(inside_content.split('\n'))
                elif library.is_javascript():
                    contentDict = json.loads(inside_content)
                    javascript = len(contentDict["devDependencies"]) + len(contentDict["dependencies"])
                elif library.is_java():
                    contentDict = inside_content.split()
                    java = contentDict.count('<dependency>')
                elif library.is_php():
                    contentDict = json.loads(inside_content)
                    php = len(contentDict["require"]) + len(contentDict["require-dev"])

    return generate_dates(javascript, java, python, php)