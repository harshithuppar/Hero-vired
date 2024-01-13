
def app():
    
    mylist = []
    mytuple = ()
    myset = {}
    
    while (True):

        print("Welcome to my Application")
        print("Press 1 for list operation")         
        print("Press 2 for tuple operation") 
        print("Press 3 for set operation") 
        print("Press 4 for Exit operation")
        
        num=int(input("please enter number"))
        if num == 1:
            list_operation(mylist)
        elif num == 2:
            tuple_operation(mytuple)
        elif num == 3:
            set_operation(myset)
        elif num==4:
            print("existing the application")
            break

def list_operation(data):

    while(True):
        print("Press 1 for add operation")
        print("Press 2 for remove operation")         
        print(" Press 3 for display operation") 
        print("Press 4 for main menu")     
            
        num1=int(input("please enter number"))

        if num1 == 1:
            element = input("enter the elment that needed to be added")
            data.append(element)
        elif num1 ==2 :
            element = input("enter the element to be removed")
            data.remove(element)
        elif num1 == 3:
            print(data)    
        elif num1 == 4:
            break



def tuple_operation(data1):
    while(True):
        print("Press 1 for add operation")
        print("Press 2 for remove operation")         
        print(" Press 3 for display operation") 
        print("Press 4 for main menu") 
        
        num2=int(input("please enter number"))

        if num2 == 2:
            element = input("enter the elment that needed to be added")
            data1.append(element)
        elif num2 ==2 :
            element = input("enter the element to be removed")
            data1.remove(element)
        elif num2 == 3:
            print(data1)    
        elif num2 == 4:
          break



def set_operation(data2):
     while(True):
        print("Press 1 for add operation")
        print("Press 2 for remove operation")         
        print(" Press 3 for display operation") 
        print("Press 4 for main menu") 
        
        num3=int(input("please enter number"))

        if num3 == 1:
            element = input("enter the elment that needed to be added")
            data2.append(element)
        elif num3 ==2 :
            element = input("enter the element to be removed")
            data2.remove(element)
        elif num3 == 3:
            print(data2)    
        elif num3 == 4:
             break

app()