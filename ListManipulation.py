numbers =[ 1,67,89,566,229,6654]
min= numbers[0]
max= numbers [0]
for i in range( len(numbers)):
    if numbers[i]> max:
        max = numbers [i]
    elif numbers[i]< min:
        min = numbers[i]


print('max ',max)

print('min',min)





