from instance import Token
from classes.helpers import generate_dates_library
import json


def count_library():
    repo = Token().repo
    content = repo.get_contents("package.json").decoded_content
    byteToString = content.decode('utf-8')
    contentDict = json.loads(byteToString)
    dependencies = contentDict["devDependencies"]
    dependencies1 = contentDict["dependencies"]
    totalDependencies = len(dependencies) + len(dependencies1)
    numLibrary = str(totalDependencies)
    return generate_dates_library(numLibrary)
