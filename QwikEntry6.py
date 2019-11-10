from msvcrt import getch
import sys
import getpass #could use this so that terminal doesn't echo user input as they type sim to input eg = user_input= getpass.getpass("Enter text here and won't be echoed!") will return val but not show user it on IDLE/Terminal 
import pymongo
from pyautogui import press, typewrite, hotkey
def Entrychoice():
        def newEntry():
                def fieldentry(field):
                    
                    print("%s \n Do you wish to Add to this field? (hit ENTER for YES or TAB to skip" % field)
                    foo=ord(getch()); #need ord as otherwise cant' compare the codes python gives for the keys (not sure why!)
                    print("Ordered Code of Key Pressed is " + str(foo))  
                    if foo == 9:  #this is the "ordered" (ord) code for TAB so we are checking IF user entered TAB key
                        print("TAB key pressed")
                    elif foo == 13:
                                #i.e user has hit enter
                        print("ENTER key pressed")
                        newdata=input("Enter New data")
                        print(newdata)
                        return newdata
                    else:
                        print("try again")
                        fieldentry(field)    #reruns function if correct/desired keys not pressed
                newname=fieldentry("NAME")  #initiated func
                newdate=fieldentry("DATES")
                newlodge=fieldentry("LODGE")
                newrole=fieldentry("ROLE")
                newnotes=fieldentry("NOTES")

                return newname,newdate,newlodge,newrole,newnotes
                
                    

        newname,newdate,newlodge,newrole,newnotes=newEntry()
        print(newname,newdate)
        def Createitem(newname, newdate):
            entrylist=[newname, newdate]
            print(entrylist)
        Createitem(newname, newdate)

        myclient=pymongo.MongoClient("mongodb://localhost:27017/")
        mydb=myclient["Britain-pre1789"]
        mycol=mydb["people"]
        post = {"Name": newname,
                      "Dates": newdate,
                        "Lodge":newlodge,
                            "Role":newrole,
                               "Notes":newnotes
                                }
        mycol.insert_one(post)
        def Moreentries():
                runagain=input("Would you like to make any more entries? \n y(es) or n(o)")
                if runagain=="y":
                        Entrychoice()
                elif runagain == "n":
                        pass
                else:
                      print ("Please select either y or n")
                      Moreentries()
        
        #whichway()
        
        #Moreentries()
print("\n \n Welcome to QWIKENTRY! \n \n  ---NOTE: CLOSE AND RE-OPEN GUI TO MAKE SURE YOU SEE ALL CHANGES!-- \n \n")


def Query():
                    checkname=input("Please enter the person you wish to modify to conduct a search:  ")
                    
                    myclient=pymongo.MongoClient("mongodb://localhost:27017/")
                    mydb=myclient["Britain-pre1789"]
                    mycol=mydb["people"]
                    
                    cursor=mydb.people.find({"Name":{"$regex":checkname}}) #like mysql %checkname
                    
                    
                    if (len(list(cursor)))==0:  #i.e if no objects found
                            print("empty")
                    else:
                            print("found!")
                           
                    while True: 
                           print(" \n ### Results that match your searc ### \n ")
                           cursor=mydb.people.find({"Name":{"$regex":checkname}})
                           print(list(cursor))
                           
                           modify=input("Please type in the exact name of the person you want to modify -otherwise type new to add a new user or type quit to exit:")
                           cursor2=mydb.people.find({"Name":modify})
                           #print(list(cursor2))
                           if modify=="quit":
                                   
                                   return
                           elif modify== "new":
                                   Entrychoice()
                           else:
                                   if (len(list(cursor2)))!=0:
                                                   print("found!")
                                                   print(list(cursor2))
                                                   cursor3=mydb.people.find({"Name":modify})
                                                   print("Name below --")
                                                   def newvals(field):
                                                     #      for doc in cursor3:
                                                                   while True:
                                                                           try:
                                                                                   cursor4=mydb.people.find({"Name":modify})
                                                                                   def valgen(field):
                                                                                           
                                                                                           for doc in cursor4:
                                                                                                   
                                                                                                 fielduse=(doc[field])
                                                                                                 return fielduse
                                                                                   fielduse=valgen(field)
                                                                                   print(fielduse)
                                                                                   print("---" + field + "---")
                                                                                   print("###please edit")
                                                                                   typewrite(fielduse)
                                                                                   newenter=input()
                                                                                   return newenter
                                                                           except:
                                                                                   fielduse=(field) #this is used if field doesn't exist for some reason
                                                                                   print("---" + field + "---")
                                                                                   print("###please populate field")
                                                                                   
                                                                                   newenter=input()
                                                                                   return newenter
                                                                                  
                                                   name2=newvals('Name')
                                                   date2=newvals("Dates")
                                                   lodge2=newvals("Lodge")
                                                   role2=newvals("Role")
                                                   notes2=newvals("Notes")
                                                                         
                                                 
                                                                         
                                   
                                                   mycol=mydb["people"]
                                                   myquery={"Name":modify}
                                                   newvalues={"$set":{"Name":name2,"Dates":date2,"Role":role2,"Notes":notes2}}  #add all fields here
                                                   mycol.update_one(myquery,newvalues)
                                                   
                                                   usechoice=input("Would you like to Modify Another? \n type yes for yes, or new to add a new person or anything else to quit!")
                                                   if usechoice=="yes":
                                                           
                                                           Query()
                                                   elif usechoice=="new":
                                                           Entrychoice()
                                                   else:
                                                           return
                          
                                   
                                   elif len(list(cursor2))==0:
                                                   print("No entry found please try again!")
                                                   continue  #continue here basically means RERUN FUNC WITHOUT explicitly Re-calling V USEFUL 
                                   


                            
                   
def whichway():
                while True:
                        firstchoice=input("Do you want to add a new user?\n select y for yes or m to modify an existing user - else type q to quit")
                        print(firstchoice)
                        if firstchoice=="y":
                                
                                Entrychoice()
                        elif firstchoice=="m":
                                Query()
                                
                                
                        elif firstchoice =="q":
                                return
                        else:

                                continue                                      
whichway()                   
#Query()

