import random

N = int(input("サイコロの面の数は?: "))
M = int(input("何回振りますか?: "))

result = []

for i in range(M):
    result.append(random.randint(1, N))

print(result)
