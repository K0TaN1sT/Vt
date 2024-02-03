def quick_sort(lst):
    base = lst[0]
    left = list(filter(lambda x: x < base, lst))
    center = list(filter(lambda x: x == base, lst))
    right = list(filter(lambda x: x > base, lst))
    return quick_sort(left) + center + quick_sort(right)


# def search(lst, val):
#     l = 0
#     h = len(lst) - 1
#     res = []
#     while l != h and not res:
#         m = (l + h) // 2
#         if lst[m] == val:
#             res.append([val, lst[1], lst[-1]])
#             return res
#         elif lst[m] < val:

file = [str(x) for x in open('products.csv', encoding='utf-8').readlines()]
file = [x.split(';') for x in file]
qur = input()

print(file)



