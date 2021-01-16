import re
import json


def count_class(content):
    return 1 if content.find('class') > -1 else 0


def count_comment(content):
    return 1 if (len(re.findall(r'/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/', content))) > 0 else 0


def count_line_of_code(content):
    rows = content.split('\n')
    totalRows = 0
    for _ in rows:
        totalRows += 1

    return totalRows


def count_testing(content):
    return 1 if content.find('org.junit.jupiter.api.Test') > -1 or content.find(
        'import unittest') > -1 or content.find('assert') > -1 else 0


def count_method(content):
    return 1 if content.find('function') > -1 or content.find('def') > -1 else 0


def count_library(library, content):
    programming = {
        'python': 0,
        'javascript': 0,
        'java': 0,
        'php': 0,
    }
    if library.is_python():
        programming['python'] = len(content.split('\n'))
    elif library.is_javascript():
        contentDict = json.loads(content)
        programming['javascript'] = len(contentDict["devDependencies"]) + len(contentDict["dependencies"])
    elif library.is_java():
        contentDict = content.split()
        programming['python'] = contentDict.count('<dependency>')
    elif library.is_php():
        contentDict = json.loads(content)
        programming['php'] = len(contentDict["require"]) + len(contentDict["require-dev"])
    return programming
