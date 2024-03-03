my_list = [1, 'hello', 3, 'world', 5]

result = list(map(lambda x: isinstance(x, (int, str)), my_list))

print(result)
