#numbers = list(range(9, 101, 2))
#print(numbers)


'''print("\nCounting every odd number")
counter = 9
while counter <= 101:
    print(counter)
    counter += 2'''

counter = 9
for counter in range(9, 101):
    while counter <= 101:
        print(counter)
        counter += 2
        if counter == 103:
            exit()
