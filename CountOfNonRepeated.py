Str = input('Enter a string: ')

for i in Str:

    count = 0

    for j in Str:

        if i == j:

            count+=1

        if count > 1:

            break

    if count == 1:

        print(i,end = " ")
        print(len(i))