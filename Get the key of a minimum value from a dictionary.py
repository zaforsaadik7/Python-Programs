dict = {1: 10, 2: 20, 3: 30, 4: 40}
minimum=min(dict.values())
for key,value in dict.items():
    if value==minimum:
        print(key)
