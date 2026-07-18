from pathlib import Path
import os

def readfileandfolder():
    path = Path()
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1} : {items} ")




def createfile():
    try: 
        readfileandfolder()
        name = input("Enter your file name:-")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as fs:
                data = input("What you want to write in this file:-")
                fs.write(data)


            print(F" FILE CREATED SUCCESFULLY ")
        
        else:
            print(f" This file already exist")

    
    
    except Exception as err:
        print(f" An error occured as {err}") 




def reaffile():
    try:
           
        readfileandfolder()
        name = input("Which file you want to read")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)


            print("READED SUCCESSFULLY")

        else:
            print("the file does not exists")



    except Exception as err:
        print(F" an error occured as {err}")  




def updatefile():
    try:
        readfileandfolder()
        name = input(" enter which file you want to update")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of youe file")
            print("press 2 for overwriting data in your file ")
            print("press 3 for appending some content in your file")

            res = int(input(" TELL YOUR RESPONSE:-"))

            if res == 1:
                name2 = input(" Tell your new file name:-")
                p2 = Path(name2)
                p.rename(p2)



            if res == 2:
                with open(p, 'w' ) as fs:
                   data = input("Tell what you want to write this is overwrite the data:-")
                   fs.write(data)    



            if res == 3:
                with open(p, 'a') as fs:
                    data = input("Tell what you want to append:-")
                    fs.write(" " +data) 



    except Exception as err:
        print(F" an error occured as {err}")   
               
def deletefile():
    try: 

        
        readfileandfolder()
        name = input("Which file you want to delete:-")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(p)

            print("FILE REMOVES SUCCESSFULLY")

        else:
            print("No such file exists")

    except Exception as err:
        print(F" an error occured as {err}")   

   
print(" Press 1 for creating a file")
print(" Press 2 for reading a file")
print(" Press 3 for updating a file")
print(" Press 4 for deletion a file")

check = int(input("Enter your response:-"))

if check == 1:
    createfile()

if check == 2:
    createfile()

if check == 3:
    updatefile()    

if check == 4:
    deletefile()    
