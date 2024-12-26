# new_list = list(original_list)
# new_dict = dict(original_dict)
# new_set = set(original_set)

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs) # Shallow copy
print(xs)
print(ys)

xs.append(['new sublist'])
print(xs) 
print(ys) # ys is not affected

xs[1][0] = 'X'
print(xs)
print(ys) # ys is affected