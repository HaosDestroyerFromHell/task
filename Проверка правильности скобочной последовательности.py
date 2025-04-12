class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def calc(self, tokens):

        for token in tokens:
            if token in ('(', '[', '{'):
                self.stack.append(token)
                
            elif token in (')', ']', '}'):
                if self.is_empty():
                    raise ValueError('Стек пустой или закр. скобок больше открывающих')
                last_symb = self.stack.pop()
                if not ((token == ')' and last_symb == '(') or
                        (token == ']' and last_symb == '[') or
                        (token == '}' and last_symb == '{')):
                    raise ValueError('Неправильная последовательность')
            else:
                raise ValueError('Некорректное значение')
                
        if not self.is_empty(): 
            raise ValueError('Не все скобки закрыты')
        else:
            return 'Првильная скобочная последовательность'

    def size(self):
        return len(self.stack)
    

stack = Stack()
expression = input('Введите скобочную последовательнсоть: ')
result = stack.calc(expression)
print(f"{result}")