def reading_to_file(file_name , prefix):
    result = []
    with open(file_name , "r") as file:
        for line in file:
          if line.startswith(prefix):
            result.append(line.strip())
    return result
a = reading_to_file("example.txt" , "Hello")
print(a)