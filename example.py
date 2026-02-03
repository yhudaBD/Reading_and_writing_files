def reading_to_file(file_name ):
    with open(file_name , "r") as file:
        for line in file:
          line_content = line.rstrip('\n')# מנקה את השורה מהתו הנסתר  
          length = len(line_content)
          print(f"{length}.**{line_content}**")
reading_to_file("example.txt")