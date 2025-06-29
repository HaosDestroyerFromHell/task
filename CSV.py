import csv

with open('prices.txt', 'r', encoding='utf-8') as txt_file:
    reader = txt_file.readlines()
    
with open('prices.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    for read in reader:
        row = read.strip().split()
        writer.writerow(row)
        
with open('prices.csv', 'r', encoding='utf-8') as csvfile:
    final_price = 0
    reader = csv.reader(csvfile)

    for read in reader:
        print(read)
        name = read[0]
        quality = int(read[1])
        price = int(read[2])
        final_price += quality * price
            
print(f'Итоговая цена: {final_price}')