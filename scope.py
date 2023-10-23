#global variable
name = "Tristan"

def sayname():
#local variable
    global name; #if we ‌announced name variable as global , the variable was changed as global variable
    name = "Yver"    
    print(name) #Yver
sayname();  

print(name) #Yver
#local variable work in local but if we announced global variable in local, the local variable was changed as global variable and the vale of global value was changed to "Yver"
#global variale is name = "Yver" rn;
def sayname():
    #local variable
    name = "Tristan"
    print(name) #Tristan
sayname();   