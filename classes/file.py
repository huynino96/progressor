class File:
    def __init__(self, name):
        self.name = name

    def is_python(self):
        return self.name.find('.py') > -1

    def is_java(self):
        return self.name.find('.java') > -1

    def is_php(self):
        return self.name.find('.php') > -1

    def is_javascript(self):
        return self.name.find('.js') > -1
