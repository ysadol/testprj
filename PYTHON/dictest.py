data = {}

for i in range(ord('a'), ord('z')+1):
    data[chr(i)] = i


for i in data.keys():
    print(f"{i}의 코드값은 {data[i]}")
