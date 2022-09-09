import os                              # to make a dummy` file and to delete it after use

import time

import pyfiglet

from colorama import *

def pretify(text,color,font=None):

    init()

    if font != None:

        figtext = pyfiglet.figlet_format(text,font = font)

        print(color + figtext)

    else :

        print(color + text)

print("welcome To ")

pretify("Quizer",Fore.RED,"banner3-D")

print("*** What do you want to do choose ***")    

def start():

    

    pretify("1.   P L A Y     Q U I Z ",Fore.BLUE)                                                                                                                                  ### color this 

    pretify("2.   M A K E     Q U I Z ",Fore.GREEN)

    pretify("3.   E X I T",Fore.YELLOW)

    pretify(" E N T E R    Y O U R    C H O I C E ",Fore.CYAN)



    ask1=0

    while ask1 not in [1,2,3]:

        ask1 = int(input(":"))

    if ask1 == 3:

        return



    '''--------function that support playing --------'''

    def play(op):

        marks=0

        while marks not in [1,2]:

            print("Want marks")

            print("1.   YES")

            print("2.   NO")

            marks=int(input("CHOOSE"))

        f=open(op,"r")

        r=f.read()

        ind=r.find("ANSWERS")

        lines=r[:ind].split("\n")

        answers=r[ind:].split("\n")

        options=['a','b','c','d']

        marks=0

        i=0

        q_no=1

        try:

            while i <len(lines):

                for j in range(6):

                    time.sleep(1)

                    pretify(lines[i],Fore.BLUE)

                    i+=1

                choice=input("your ans :")

                while choice not in options:

                    print("Enter valid option from a,b,c,d :")

                    choice=input("Enter :")

                if choice==answers[q_no][3]:

                    print("correct answer")

                    marks+=1

                else:

                    print("wrong answer")

                    q_no+=1

            if ask_mark == 1:

                pretify("Your marks: "+str(marks),Fore.RED)





        except:

            f.close()

        

    ''' --------------function to play an existing quiz------------'''



    def playing():

        time.sleep(1)

        print("Enter complete address of file")

        e=input("Enter")

        play(e)

        pretify("W H A T      N E X T")

        start() 

    

    '''--------------------------------function to make quiz---------------------------------------'''

    def making():

        try :

        

            n=int(input("Enter no. of questions :"))

        except ValueError :

        

            print("Enter a valid number")

            n=int(input(": "))

        

        

        '''DEFINING VARIABLES'''



        write=''

        Q=[]

        O=[]

        A=[]

        options=['a','b','c','d']

        i=0



        print("MAKING QUIZ")                                                                        #highlight this 

        '''TAKING VALUES OR DATA'''

        pretify("E N T E R      Q U E S T I O N S  :",Fore.LIGHTMAGENTA_EX)

        while i<n:

        

        

            q=input("Q{}.".format(i+1))

            a=input("Option a:")

            b=input("Option b:")

            c=input("Option c:")

            d=input("Option d:")

            ans=input("Enter correct option :")



            x=[a,b,c,d]

            while ans not in options:

                print("Enter valid correct option from  a,b,c,d :")

                ans=input("Enter :")



            '''                                        CONFIRMATION                              '''

            print("\nConfrim your question")

            print("Your question is :\n","Q",i+1,q)

            print("Options are :")

            for j in range(len(options)):

                print(options[j],". ",x[j])

            print("\nCorrect option is ",ans)

            print("confirm your question ")

            print("1.   Y E S ")

            print("2.   N O ")

            

            confirm = 0

            while confirm not in [1,2]:

                 confirm = int(input("Your choice :"))

            if confirm == 1:

                A+=ans

                Q.append(q)

                O.append(x)

                i+=1    #updating while loop

                write+=str(i)+". "+q+'\n'+'a. '+a+'\n'+'b. '+b+'\n'+'c. '+c+'\n'+'d. '+d+'\n\n'



        def f_write(f):

            file=open(f,'w+')

            file.write(write)

            file.flush()

            correct_ans=""

            file.write("ANSWERS\n")

            for h in range(n):

                correct_ans+=str(h+1)+". "+A[h]+'\n'

            file.write(correct_ans)

            file.flush()

            file.close()

        #------------------------------------------------#

        time.sleep(1)

        print("1.   PLAY YOUR QUIZ ")

        print("2.   MAKE FILE OF QUIZ")

        print("3.   DO BOTH  ")

        print("4.   EXIT")

        ask2=int(input("your choice :"))

        while ask2 not in (1,2,3,4):

            print("Enter correct choice from 1,2,3,4")

            ask2=int(input("Enter :"))

    

        if ask2 == 2 or ask2 == 3:

            print("Enter complete address of file to be saved with .txt extension")

            file_name=input(": ")

            f_write(file_name)

            pretify("FILE MADE",Fore.BLUE,)                                                                                                                                                                                              ####HIGHLIGHT THIS

            print("A file of your quiz with address",file_name,"is created succesfully\nNote: If given address is not correct file woulld'nt be created")

            dummy="no"

        else:  #making a dummy file

            dummy="yes"

            f = open("D:\\dummy.txt", "w+")

            f.close()

            file_name="D:\\dummy.txt"

            f_write(file_name)

    

        #-----------------------------playing the made quiz-------------------------------#

        if ask2 == 1 or ask2 == 3:

            time.sleep(1)

            pretify("Playing quiz",Fore.GREEN)                                                                                                               #############highlight it 

            time.sleep(1)

            play(file_name)

        

        #-----------------------------removing dummmy file---------------------------------#

       

            if dummy=="yes":

                os.remove(file_name)

        start()

    #-------------------------------------------------

    if ask1 == 1:

        playing()

        

    if ask1 == 2:

        making()

start()

