import re
from instance import Token
from classes.file import File

repo = Token().repo
contents = repo.get_contents("")

# Counter
total = 0
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
        file = File(fileName)
        if file.is_python() or file.is_java() or file.is_php() or file.is_javascript():
            decoded_content = file_content.decoded_content
            inside_content = decoded_content.decode('utf-8')
            length = len(re.findall(r'(@GetMapping|@PostMapping|@PutMapping|@DeleteMapping|.get|.post|.put|.delete|::get|::post|::put|::delete|.route)', inside_content))
            total += length

            if file.is_javascript():  # Javascript
                javascript += length
            elif file.is_python():  # Python
                python += length
            elif file.is_java():  # Java
                java += length
            elif file.is_php():  # PHP
                php += length

print('Total API: ' + str(total))
print('Javascript API: ' + str(javascript))
print('Python API: ' + str(python))
print('Java API: ' + str(java))
print('PHP API: ' + str(php))
