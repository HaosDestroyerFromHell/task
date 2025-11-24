import datetime

now = datetime.datetime.now()
print(f'Текущая дата/время: ', now.strftime('%m/%d/%y %H:%M:%S'))

week_day = now.strftime('%A')
print(f"Сегодня: {week_day}")

year = int(now.strftime('%Y'))
def sum_day(year):
    start = datetime.date(year, 1,1)
    start_next = datetime.date(year + 1, 1, 1)
    delta = start_next - start
    return delta.days

if sum_day(year) % 365 == 0:
    print(f'{year} год не високосный')
else:
    print(f'{year} год високосный')


request = input('Введите дату в формате гггг-мм-дд: ')
print(request)
try:
    user_date = datetime.datetime.strptime(request, "%Y-%m-%d")
    current_date = now
    
    delta = user_date - current_date

    if user_date < current_date:
        print("Дата уже прошла.")
    else:
        days = delta.days

        seconds = delta.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60

        print(f"До {user_date.date()} осталось {days} дней, {hours} часов, {minutes} минут.")
except ValueError:
    print('Неверный формат даты')