import random

n = int(input("サイコロの面の数は?: "))
m = int(input("何回振りますか?: "))

result = []

for i in range(m):
    result.append(random.randint(1, n))

print(result)
