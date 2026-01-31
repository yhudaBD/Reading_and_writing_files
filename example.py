def write_to_file(file_name , text):
  try:
     with open(file_name , "w") as file:
      file.write(text)
     return True
  except Exception as e:
    print(f"error: {e}")
    return False 

test1 = write_to_file("example.txt" , "hello world")
print(f"Passed successfully: {test1}")

test2 =write_to_file("invalid_folder/test.txt", "This should fail.")
print(f"failed: {test2}")
