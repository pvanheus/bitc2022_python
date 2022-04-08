my_file = open("out.txt", "w")
my_file.write("Hello World\n")
my_file.close()

# Ctrl-/ to comment or uncomment code
my_file = open("out.txt")
my_file_contents = my_file.read()
print(my_file_contents)
