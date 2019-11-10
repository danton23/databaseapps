import mysql.connector
from mysql.connector import Error
from msvcrt import getch
import sys
import pymongo
from pyautogui import press, typewrite, hotkey


 
 
def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='127.0.0.1',
                                       user='root',
                                       database="freemasonry",
                                       password='5tlashat',
                                       ) 
        if conn.is_connected():

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
                                return fieldentry(field)    #reruns function if correct/desired keys not pressed  #need RETURN here to basically say if on FIRST pass user doesn't enter right key do not take the NULL returned from that as ultimate reulst of FUNk but ONLY the val returned on SUCESSFUL time (i.e user input)
                        newname=fieldentry("NAME")  #initiated func
                        newimportance=fieldentry("Importance")
                        newera=fieldentry("Era of Activity")
                        newmason=fieldentry("Freemason")
                        newlodge=fieldentry("Lodge")
                        newnat=fieldentry("Nationality")
                        newrole=fieldentry("Role")
                        newdates=fieldentry("Dates")
                        newnotes=fieldentry("Notes")

                        return newname,newimportance,newera,newmason,newlodge,newnat,newrole,newdates,newnotes
                        
                def Query():
                    checkname=input("Please enter the person you wish to modify")
                    query_make="""SELECT Name from frenchrev Where Name LIKE '%%%s' """ %(checkname)
                    cursor=conn.cursor()
                    cursor.execute(query_make)
                    result=cursor.fetchall()
                    print(result)
                    print(query_make)
                    print("<<<Results which match your search >>>")
                    for item in result:
                        print(item)
                    print(str(len(result))+"length of result is")
                    if len(result)==0:
                        print("no items match your search")

                        
                        def choicefunc():
                             
                             while True: #Need this to keep asking if user doent enter 1 or 2 (otherwise have probs with Return statement after first pass)
                                 quitchoice=input(" Try again = 1, quit = 2")
        
                                 if quitchoice=="1":
                                       Query()
                                 elif quitchoice=="2":
                                      choicevar=4
                                      print("quitting")
                                      return choicevar
                                 else:
                                     print("sorry incorrect value entered, please try again ")
                                     continue   #this code (with while true above - allows you to avoid func exiting if incorrect val entered which will cause problems with returning correct vals after first pass)
                        choicevar=choicefunc()
                        print("choicereturn is" + str(choicevar))
                        if choicevar==4:   #the 4 here is just random what I am doing is saying IF this condition returned (ie within fun user chose to quit) then return from OUTER function (otherwise is impossible to ahceive this from WITHIN nested func)
                             return
                        else:
                             pass
                    newname=input("Please type in the exact name of the person you wish to access")
                    query_make="""SELECT Name, Role from frenchrev Where Name = '%s' """ %(newname)
                    cursor=conn.cursor()
                    cursor.execute(query_make)
                    result=cursor.fetchall()
                    if result==[]:
                        print("Sorry your search was not recognised please try again")
                        choice=input("try again? hit y for yes or any other key to quit")
                        if choice=="y":
                                   Query()
                        else:
                            return
                    else:
                        print(result)
                        def Modfield(newname):
                            query_make2="""SELECT * from frenchrev Where Name = '%s' """ %(newname)
                            cursor=conn.cursor()
                            cursor.execute(query_make2)
                            result2=cursor.fetchall()
                            print("result2 below")
                            print(result2)
                            
                            colnames=cursor.column_names
                            print(colnames)
                            for item in colnames:
                                if item!="Id":
                                        choice2=input("Do you wish to modify "+item+" field type 'yes' to modify or any other keys to skip")
                                        if choice2 =="yes":
                                            print("Put Modify query here")
                                            print(item+newname+"item and newname")
                                            query_maker="SELECT * from frenchrev Where Name = %(data)s " 
                                            cursor=conn.cursor(dictionary=True) #NEED dictionary=True so can search for specific Column names in the for row in resulty part below
                                            data=(newname)
                                            cursor.execute(query_maker,{'data':data})
                                            resulty=cursor.fetchall()
                                            print("resulty below")
                                            print(resulty)
                                            def getword():
                                               for row in resulty:
                                                      print ("Current Value is: " + row[item])
                                                      print("<<<<Edit Below and Hit Enter to upload or TAB to cancel>>>")
                                                      return (row[item])
                                            golden=getword()
                                            typewrite(golden)
                                            newenter=input()
                                            sql="UPDATE frenchrev SET name = %(name)s WHERE name=%(oldname)s"
                                            cursor=conn.cursor(dictionary=True)
                                            cursor.execute(sql,{'name':newenter,'oldname':newname})
                                            conn.commit()
                                            #adddata="INSERT INTO frenchrev(%(name)s) Values('John')"
                                            #cursor=conn.cursor(dictionary=True)
                                            #cursor.execute(adddata,{'name':newname},)  #"val":newenter
                                            
                                            
                                        else:
                                            pass
                                else:
                                    pass
                            
                        Modfield(newname)        
                    
                def firstChoice(): #lets user choose if wish to add or modify or quit
                      desiredaction=input("#### Welcome to the Python MySQL interactive tool #### \n \n --- please choose from the options below--- \n (1) New Entry \n (2) Modify Existing Entry \n (3) Quit")
                      if desiredaction=="1":
                              
                                newname,newimportance,newera,newmason,newlodge,newnat,newrole,newdates,newnotes=newEntry()
                                print('Connected to MySQL database')
                                boober="Yablokov"
                                    
                                    
                                query_do="""INSERT INTO frenchrev(Name,Importance,Era_of_Activity,freemason,lodge,nationality,Role,Dates,Notes)
                                              VALUES
                                              ('%s','%s','%s','%s','%s','%s','%s','%s','%s') """ %(newname,newimportance,newera,newmason,newlodge,newnat,newrole,newdates,newnotes)
                                cursor = conn.cursor()
                                      
                                result=cursor.execute(query_do)

                                            
                                conn.commit()
                                firstChoice()
                      elif desiredaction =="2":
                          Query()
                          firstChoice()
                      elif desiredaction =="3":
                         pass
                      else:
                          print("Invalid option Please Choose from the options listed")
                          firstChoice()
        firstChoice()
                
    except Error as e:
        print(e)
 
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
    
if __name__ == '__main__':
    connect()

