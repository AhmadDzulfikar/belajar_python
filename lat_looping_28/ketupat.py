triangle = int(input('masukkan sisi segitiga yang anda inginkan = '))

if triangle % 2:
    triangle = triangle
else:
    triangle -= 1

count = 1 

while count < triangle:
    print(('*'*count).center(triangle))
    count += 2

while count > 0:
    print(('*'*count).center(triangle))
    count -= 2