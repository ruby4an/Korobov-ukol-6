def capitals(string):
    return sum(map(str.isupper, string))


correct_array = ['1', '1', '1', '1']
incorrect_array = ['1', '1', '1', '1']
array = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']
print(capitals(array[3]))
for i in range(0, 4):
    if capitals(array[i]) != 2:
        incorrect_array[i] = array[i]
    else:
        correct_array[i] = array[i]
while '1' in correct_array:
    correct_array.remove('1')
while '1' in incorrect_array:
    incorrect_array.remove('1')
print("Correctly written names:", str(correct_array))
print("Incorrectly written names:", str(incorrect_array))
# optional task, since it's short :)
for i in range(0, 4):
    array[i] = array[i].title()
print('All the names fixed:', array)
