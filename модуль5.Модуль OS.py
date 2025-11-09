import os

direct_path = 'Путь\Управление_файлами'
exists = os.path.exists(direct_path)
print("Существует ли:", exists)

if exists is False:
    os.mkdir('Управление_файлами')

file_names = ['file1.txt', 'file2.txt']
some_text = []

for i in range(2):
    dif_txt = input('какой-то текст: ')
    if dif_txt not in some_text:
        some_text.append(dif_txt)
print(some_text)

for file_name, text in zip(file_names, some_text):
    file_path = os.path.join(direct_path, file_name)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text) 
        
content = os.listdir(direct_path)
print("содержимое директории: ", content)
    
file_remove = os.path.join(direct_path, file_names[1])
os.remove(file_remove)

new_dir = os.path.join(direct_path, 'новая_директория')
if not os.path.exists(new_dir):
    os.mkdir(new_dir)

source_path = 'Путь/Управление_файлами/file1.txt' 
destination_path = 'Путь/Управление_файлами/новая_директория/file1.txt' 
os.rename(source_path, destination_path)

os.remove('Путь/Управление_файлами/новая_директория/file1.txt')
os.rmdir('Путь/Управление_файлами/новая_директория')
os.rmdir('Путь/Управление_файлами')