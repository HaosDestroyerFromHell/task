from collections import Counter

f = open('hello.txt', 'w', encoding='utf8')

f.write("яблоко, книга, солнце, кошка, стол,\
 яблоко, вода, дом, книга, ветер,\
 кошка, лампа, окно, яблоко, стол,\
 ручка, ночь, дом, книга, ветер")

f.close()

f = open('hello.txt', 'r', encoding='utf8')
for line in f:
    
    words = (line.split(" "))
    word_count = Counter(words)
    
    print(f"Кол-во слов: {len(words)}")
    print(f"Кол-во уникальных слов: {len(word_count)}")
    print("Все использованные слова: ")
    for word, count in word_count.items():
        print(f"{word}: {count}")

f.close()

