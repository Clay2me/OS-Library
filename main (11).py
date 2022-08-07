
import os


nameOfDirctry = input("Directory to store the new file: ")

nameOfFileToBeMade = input("Please enter the name of file to be created: ")

inputName = input("Please enter your full name: ")

inputAddr = input("Please enter your full address: ")

inputContactNum = input("Please enter your phone no.: ")


if os.path.isdir(nameOfDirctry):


    fileToBeWrittenTo = open(os.path.join(nameOfDirctry, nameOfFileToBeMade), "w")


    fileToBeWrittenTo.write(inputName + str(",") + inputAddr + str(",") + inputContactNum)

    fileToBeWrittenTo.close()

  
    print("The data in file is: ")


    fileToBeScanned = open(os.path.join(nameOfDirctry, nameOfFileToBeMade), "r")

    print(fileToBeScanned.read())

    fileToBeScanned.close()

else:
   
    print("The directory mentioned is non-existent, please try again!")