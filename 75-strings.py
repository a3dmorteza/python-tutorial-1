a = "Hello, World!"
result = map(lambda x: x.strip(), a.split(","))
print(list(result)) # returns ['Hello', 'World!']