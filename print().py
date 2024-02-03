import csv


file = [str(x) for x in open('products.csv', encoding='utf-8').readlines()]
data_total = ['total']

for qur_str in file:
    qur_str = qur_str.split(';')
    if qur_str[0] == 'Закуски':
        data_total.append(int(float(qur_str[-1]) * float(qur_str[-2])))

print(sum(data_total[1:]))

with open('products_new.csv', 'w') as new_file:
    writer =csv.writer(new_file, delimiter=' ')
    writer.writerows([str(x) for x in data_total])





