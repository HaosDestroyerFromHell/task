class TaskQueue:
    def __init__(self):
        self.stack = []
    
    def add_task(self, task):
        return self.stack.append(task)
    
    def get_next_task(self):
        if not self.is_empty():
            return self.stack.pop(0)
        else:
            return None
        
    def is_empty(self):
        return len(self.stack) == 0
    
class Task:
    def __init__(self, name):
        self.name = name
        
        
queue = TaskQueue()

task1 = Task("Задача 1")
task2 = Task("Задача 2")
task3 = Task("Задача 3")

queue.add_task(task1)
queue.add_task(task2)
queue.add_task(task3)

next_task = queue.get_next_task()
print(f"Следующая задача: {next_task.name if next_task else 'Нет задач'}")  # Ожидаемый результат: "Задача 1"

queue.get_next_task()  # Извлечь следующую задачу

print(f"Очередь пуста: {queue.is_empty()}")  # Ожидаемый результат: False