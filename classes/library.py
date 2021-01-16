class Library:
    def __init__(self, name):
        self.name = name

    def is_python(self):
        return self.name.find('requirements.txt') > -1

    def is_java(self):
        return self.name.find('pon.xml') > -1 or self.name.find('build.gradle') > -1

    def is_php(self):
        return self.name.find('composer.json') > -1

    def is_javascript(self):
        return self.name.find('package.json') > -1
