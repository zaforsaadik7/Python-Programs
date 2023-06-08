if __name__ == '__main__':
    def num_function(num):
        numbers = []
        for i in range(1, num + 1):
            numbers.append(str(i))
        return "".join(numbers)

n = int(input())
print(num_function(n))
