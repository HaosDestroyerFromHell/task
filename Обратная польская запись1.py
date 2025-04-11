
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def calc(self, item):
        tokens = item.split()
        
        for token in tokens:
            if token.isdigit():
                self.stack.append(int(token))
            else:
                try:
                    token2 = self.stack.pop()
                    token1 = self.stack.pop()
                    
                    if token == '+':
                        self.stack.append(token1 + token2)
                    
                    elif token == '-':
                        self.stack.append(token2 - token1)
                    
                    elif token == '*':
                        self.stack.append(token1 * token2)
                        
                    elif token == '/':
                        self.stack.append(token1 / token2)
                    
                    elif token == '^':
                        self.stack.append(token1 ** token2)
                    
                    else:
                        raise ValueError('Ошибка ввода')

                except IndexError:
                    raise IndexError('некорректное значение')
                
        if not self.is_empty(): 
            return self.stack.pop()
        else:
            raise ValueError('Стек пустой')


    def size(self):
        return len(self.stack)
    

stack = Stack()
expression = "3 4 2 * +"
result = stack.calc(expression)
print(f"Результат вычисления: {result}")