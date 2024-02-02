##folder and file handling project
from pathlib import Path
import os

def creatingfolder():
    try:
        name = input("Tell your folder name")
        path = Path(name)
        path.mkdir()
        print(f"folder name {name} has been created successfully")
    except Exception as err:
        print("folder already exist")

def readfileandfolder():
    path = Path("")
    items = list(path.rglob("*"))
    for i,v in enumerate(items):
        print(f"{i+1}) {v}")

def updatefolder():
    try:
        readfileandfolder()
        oldname = input("Tell which folder you want to update")
        path = Path(oldname)
        if path.exists() and path.is_dir():
            newname = input("Enter new name for that folder")
            newpath = Path(newname)
            path.rename(newpath)
            print(f"Folder {oldname} is updated with the name of {newname} successfully")
        else:
            print("Error folder doesn't exist")
    except Exception as err:
        print(f"An error occured as {err}")

def deletefolder():
    try:
        readfileandfolder()
        name = input("Tell ur folder name that u want to delete")
        path = Path(name)
        if path.exists() and path.is_dir():
            path.rmdir()
            print(f"The folder named {name} has been deleted successfully")
        else:
            print("Error Folder does not exists.")
    except Exception as err:
        print(f"Error as {err}")

def createfile():
    try:
        readfileandfolder()
        name = input("tell ur filename with extension")
        path = Path(name)
        if not path.exists():
            with open(name,"w") as file:
                data = input("please tell ur data u want to input")
                file.write(data)
            print("File created successfully")
        else:
            print("File name already exist")

    except Exception as err:
        print(f"An error occured as {err}")

def updatefile():
    try:
        readfileandfolder()
        name = input("which file u want to update")
        path = Path(name)
        if path.exists() and path.is_file():
            print("operations")
            print("press 1 for renaming a file")
            print("press 2 for overwriting a file")
            print("press 3 for appending the content in a file")
            choice = input("please tell your choice")
            if choice =='1':
                newname = input("tell ur new file name")
                newpath = Path(newname)
                path.rename(newpath)
                if not newpath.exists():
                    path.rename(newpath)
                    print(f"file name {name} changed to {newname} successfully")
                else:
                    print(f"error filename{newname} already exist")
            if choice =='2':
                with open(name,"w") as file:
                    data = input("tell ur data u want to overwrite")
                    file.write(data)
                print("overwritten successful")
            if choice =='3':
                with open(name,"a") as file:
                    data = input("tell ur data u want to append")
                    file.write(" "+data)
                print("appended successfully")
            else:
                print("file does not exist")
    except Exception as err:
        print(f"an error occurred as {err}")

def readfile():
    try:
        readfileandfolder()
        name = input("tell ur filename u want to read")
        path = Path(name)
        if path.exists():
            with open(name,"r") as file:
                print(file.read())
        else:
            print("File doesn't exist")
    except Exception as err:
        print(f"an error occured as {err}")

def deletefile():
    try:
        readfileandfolder()
        name = input("tell ur filename u want to read")
        path = Path(name)
        if path.exists():
            path.unlink()
            print("file deleted successfully")
        else:
            print("file doesn't exist")
    except Exception as err:
        print(f" An error occured as {err}")

while True:
    print("press 1 for creating a folder")
    print("press 2 for reading all folder items")
    print("press 3 for updating a folder")
    print("press 4 for deleting a folder")
    print("Press 5 for creating a file")
    print("Press 6 for updating a file")
    print("Press 7 for reading a file")
    print("press 8 for deleting of a file")
    a = input("Tell your input")
    if a =='0':
        exit(0)
    if a == '1':
        creatingfolder()
    if a =='2':
        readfileandfolder()
    if a =='3':
        updatefolder()
    if a =='4':
        deletefolder()
    if a =='5':
        createfile()
    if a =='6':
        updatefile()
    if a =='7':
        readfile()
    if a =='8':
        deletefile()