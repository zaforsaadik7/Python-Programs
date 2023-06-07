nums=[1,2,3,4,5,6,2343,12345,52,2435,234]
for num in nums:
    if num == 6:
        print('found!')
        break

for num in nums:
    if num==2343:
        continue
    print(num)
