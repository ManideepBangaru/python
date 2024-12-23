def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))

print_vector(0, 1, 0)

tuple_vec = (1, 0, 1)
list_vec = [1, 0, 1]

print_vector(tuple_vec[0], tuple_vec[1], tuple_vec[2]) # not pythonic  # ugly
print_vector(*tuple_vec)  # Pythonic  # better
print_vector(*list_vec)  # Pythonic  # better

# ---------------------------------------------------------------------------

gen_expr = (x * x for x in range(3))
print_vector(*gen_expr)  # Pythonic  # better

dict_vec = {'y': 0, 'z': 1, 'x': 1}
print_vector(**dict_vec)  # Pythonic  # better
print_vector(*dict_vec)  # Pythonic  # better