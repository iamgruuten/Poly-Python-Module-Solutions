
#Searching for name if existing in the list
'''
If name in list then
output element
else
display name not found

'''

def searchname(nameList, name):
    
    if(name in nameList): #Look if the name is in the namelist
        #If name found, the index will be output
        nameIndex = nameList.index(name)
        print(f"There are {len(nameIndex)} in the list")
        print(f"Name {0} is found in position {1} in the name list.".format(name, position))
        
    else:
        #If name is not found, output name not found
        print("Name not found")
        print('I am adding the name into the list')
        position = input("Which position in the list? : ")
        nameList.insert(int(position), name)
        print(nameList)

nameList = ["Tom", "Joe", "Mary", "John", "Bob","Jane"] #nameList
name = input("Enter name to search : ") #Name that is used to look in the list
searchname(nameList, name) #calling function searchname  

