class MyDict:
    def __init__(self):
        self._keys = []
        self._values = []
    
    def __getitem__(self, key):
        if key in self._keys:
            index = self._keys.index(key)
            return self._values[index]
        return None
    
    def __setitem__(self, key, value):
        if key in self._keys:
            index = self._keys.index(key)
            self._values[index] = value
        else:
            self._keys.append(key)
            self._values.append(value)
    
    def __delitem__(self, key):
        if key in self._keys:
            index = self._keys.index(key)
            del self._keys[index]
            del self._values[index]
    
    def __contains__(self, key):
        return key in self._keys
    
    def keys(self):
        return self._keys
    
    def values(self):
        return self._values
    
    def items(self):
        return list(zip(self._keys, self._values))
    
    def __str__(self):
        items = []
        for key, value in zip(self._keys, self._values):
            items.append(f"{key}: {value}")
        return "{" + ", ".join(items) + "}"
    
    
my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
my_dict['city'] = 'Moscow'
print(my_dict['name'])  # Вернет 'Alice'
print('land' in my_dict)  # Вернет False
del my_dict['age']
print(my_dict.keys())  
print(my_dict.values()) 
print('Строковое представление словаря:', my_dict)
print("Пары ключ, значение:", my_dict.items())

