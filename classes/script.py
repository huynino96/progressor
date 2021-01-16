from instance import Token
from classes.file import File
from classes.library import Library
import classes.counter


class Script:
    repository_endpoint = ""
    contents = {}
    keyword = {
        'class': 0,
        'comment': 0,
        'library': 0,
        'line_of_code': 0,
        'method': 0,
        'testing': 0
    }
    javascript = keyword
    python = keyword
    java = keyword
    php = keyword
    folder = 0
    file = 0

    def set_repository(self, repository):
        self.repository_endpoint = repository
        return self

    def get_contents(self):
        token = Token()
        token.repository_endpoint = self.repository_endpoint
        repo = token.get_repository()
        contents = repo.get_contents("")
        folders = []
        files = []
        while contents:
            file_content = contents.pop(0)
            if file_content.type == 'dir':
                folders.append(file_content)
                contents.extend(repo.get_contents(file_content.path))
            else:
                files.append(file_content)

        self.contents = {
            'folders': folders,
            'files': files,
        }

        return self

    def programming_counter(self, name, file, content):
        self[name]['class'] += counter.count_class(content)
        self[name]['comment'] += counter.count_comment(content)
        self[name]['line_of_code'] += counter.count_line_of_code(content)
        self[name]['library'] = (counter.count_library(Library(file), content))[name]
        self[name]['method'] += counter.count_method(content)
        self[name]['testing'] += counter.count_testing(content)

    def starting_count(self):
        for content in self.contents['files']:
            fileName = content.name
            file = File(fileName)
            if file.is_python() or file.is_java() or file.is_php() or file.is_javascript():
                decoded_content = content.decoded_content
                inside_content = decoded_content.decode('utf-8')

                # Count keywords
                if file.is_javascript():  # Javascript
                    self.programming_counter('javascript', file, inside_content)
                elif file.is_python():  # Python
                    self.programming_counter('python', file, inside_content)
                elif file.is_java():  # Java
                    self.programming_counter('java', file, inside_content)
                elif file.is_php():  # PHP
                    self.programming_counter('php', file, inside_content)

            return self

    def count_file_and_folder(self):
        self.folder = len(self.contents['folders'])
        self.file = len(self.contents['files'])
        return self
