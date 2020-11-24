from instance import Token
from classes.helpers import generate_dates_file_and_folder


def count_file_and_folder():
    # Getting data from GitHub API
    repo = Token().repo

    listFile = []
    listDir = []
    contents = repo.get_contents("")
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            listDir.append(file_content)
            contents.extend(repo.get_contents(file_content.path))
        else:
            listFile.append(file_content)

    return generate_dates_file_and_folder(len(listDir), len(listFile))
