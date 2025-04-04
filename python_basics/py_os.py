import os
import json
import csv
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
# for x in range (100000000):
    # bye_bye_desktop_data = "Be sure to not open unknown apps on your pc!"
    # bye_bye_desktop_path = "/home/danbar/Desktop/test_folder/thats_a_prank_bro" + f"{x}"
    # with open(bye_bye_desktop_path, "w") as file:
        # file.write(bye_bye_desktop_data)
        # print(f"txt file Nr {x} has been created")
############################# writing files
############################# writing files
students = ["Jake", "Paul", "Eugene", "Alex"]
try:
    with open(file_path_output, "w") as file: # "w" write file if that exist | "x" if file doesnt exist, that will create it another way = error 
        for student in students:
            file.write(student + "\n")                  # "a" to append file | "r" to read
        print(f"txt file '{file_path_output}' was created")
except FileExistsError:
    print("File already exists!")
############################# writing files
############################# json files
employee = {
    "name": "Aleksejs",
    "age": 17,
    "job": "Student"
}
try:
    with open(file_path_output, "w") as file: # "w" write file if that exist | "x" if file doesnt exist, that will create it another way = error 
        json.dump(employee, file)                  # "a" to append file | "r" to read
        print(f"json file '{file_path_output}' was created")
except FileExistsError:
    print("File already exists!")
############################# json files
############################# csv files
employees = [
    ["Name", "Age", "Job"],
    ["Spongebob", 30, "Cook"],
    ["Patrick", 37, "Unemployed"],
    ["Sandy", 27, "Scientist"]]

file_path_csv = "/home/danbar/Desktop/project_x/output.csv"
try:
    with open(file_path_csv, "w", newline = "") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file {file_path_csv} was created")
except FileExistsError:
    print("File already exists!")
############################# csv files
############################# read files/$bash: cat
try:
    with open(file_path_csv, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[0])
        print(content)
except FileNotFoundError:
    print(f"There is no such file at {file_path_csv} path")
except PermissionError:
    print("You dont have permission to read that file without super user")
############################# read files

