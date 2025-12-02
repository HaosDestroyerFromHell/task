
from collections import Counter, defaultdict, namedtuple, defaultdict, deque
import random

print(f'\n==================== [Задание 1] =========================\n')

random_nuber = [random.randint(1, 20) for _ in range(45)]
# print(f'\nсписок рандомных чисел: {random_nuber}\n-------------')

counter = defaultdict(int)
for num in random_nuber:
    counter[num] += 1
print(f"Количество уникальных элементов: {len(counter)}")

counter = Counter(random_nuber)
most_common = counter.most_common(3)
for element, count in most_common:
    print(f"Число {element} встречается {count} раз")

print(f'\n==================== [Задание 2] =========================\n')

Book = namedtuple('Book', ['title', 'author', 'genre'])
gp = Book('title1', 'name1', 'genre1')
wk = Book('title2', 'name2', 'genre2')
print(f'Информация по первой книге: {gp.title}, {gp.author}')
print(f'Информация по второй книге: {wk.title}, {wk.author}')

print(f'\n==================== [Задание 3] =========================\n')

dict1 = defaultdict(list)
dict1['value1'].append('земля')
dict1['value1'].append('вода')
dict1['value2'].append('дом')
dict1['value2'].append('город')

for key, values in dict1.items():
    print(f'{key}: {values}')

print(f'\n==================== [Задание 4] =========================\n')

d = deque([1, 2, 3])
d.append(4)
print("добавление 4: ", d)
d.appendleft(0)
print("добавление нуля слева: ", d)
d.pop()
print("удаление последнего элемента: ", d)
d.popleft()
print("удаление крайнего левого элемента: ", d)

print(f'\n==================== [Задание 5] =========================\n')

simple_queue = deque()

def add_queue(element):
    simple_queue.append(element)
    
def del_queue():
    if len(simple_queue) == 0:
        return None
    return simple_queue.popleft()

add_queue('первый элемент')
add_queue('второй элемент')
add_queue('третий элемент')
print("Очередь после добавления элементов:", simple_queue)

del_queue()
print("Очередь поcле удаления элемента:", simple_queue)

