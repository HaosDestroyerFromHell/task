# Задание 1: Работа с JSON файлом

import json

with open('students.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    
print(f'Общее количество студентов в файле: {len(data)}\n')

max_student = max(data, key=lambda i: i.get("возраст", -1)) 
print(f"Студент с максимальным возрастом: {max_student['имя']}\n{max_student}\n") 

subject_of_study = []
serch = input('Определите необходимый для подсчета предмет: ').casefold()

for student in data:
    subject_lower = [subj.casefold() for subj in student['предметы']]
    if serch in subject_lower:
        subject_of_study.append(student)
        
print(f'Студентов изучающих {serch}: {len(subject_of_study)}\n\n\
Задание №2  -----------------------------------------------------------\n')


# Задание 2: Работа с CSV файлом

import csv
with open('sales.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    final_price = 0
    sales_by_product = {}
    data_by_month = {}
    
    for read in reader:
        # print(read)
        if read != ['Дата', 'Продукт', 'Сумма']:   
            data = read[0]
            name = read[1]
            price = int(read[2])
            final_price += price
            
            if name in sales_by_product:
                sales_by_product[name] += price
            else:
                sales_by_product[name] = price

            month = data[5:7]            
            if month in data_by_month:
                data_by_month[month] += price
            else:
                data_by_month[month] = price
            # print(f'---------------------{data_by_month}')
                
print(f'\nИтоговая цена: {final_price}') 

max_product = max(sales_by_product, key=sales_by_product.get)
max_sales = sales_by_product[max_product]
print(f'Продукт с самым высоким объёмом продаж: {max_product} — {max_sales}\n')

for month, total in sorted(data_by_month.items()):
    print(f'Месяц - {month}, Сумма - {total}')
print('\nЗадание №3  -----------------------------------------------------------\n')


# Задание 3: Комбинированная работа с JSON и CSV

import json
import csv

with open('employees.json', 'r', encoding='utf-8') as f:
    employees = json.load(f)

performance_data = {}
with open('performance.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for read in reader:
        employee_id = int(read['employee_id'])
        performance = float(read['performance'])
        performance_data[employee_id] = performance

for emp in employees:
    emp_id = emp['id']
    emp['performance'] = performance_data.get(emp_id)

total_performance = sum(emp['performance'] for emp in employees)
average_performance = total_performance / len(employees)
print(f"\nСредняя производительность: {average_performance:.2f}")

top_employee = max(employees, key=lambda i: i['performance'])
print(f"Сотрудник с наивысшей производительностью: {top_employee['имя']}\n\
Показатель производительности: {top_employee['performance']}")

