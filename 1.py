import csv


file = [str(x) for x in open('products.csv', encoding='utf-8').readlines()] # инициализирую файл
data_total = ['total']

for qur_str in file: # перебор строк в файле
    qur_str = qur_str.split(';')
    if qur_str[0] == 'Закуски': # проверка является ли строка информацией о закусках
        data_total.append(int(float(qur_str[-1]) * float(qur_str[-2])))

print(sum(data_total[1:])) # вывод итоговой суммы

with open('products_new.csv', 'w') as new_file: # создается таблица и в нее записываются подсуммы
    writer =csv.writer(new_file, delimiter=' ')
    writer.writerows([str(x) for x in data_total])





