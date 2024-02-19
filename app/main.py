"""
Created on Sun Feb 18 07:17:50 2024

@author: kosmous
"""
from datetime import datetime
d = datetime.now()
dat=d.strftime('%d/%m/%Y')
import time
import random as r
import csv
from pathlib import Path
import sys 
path = Path('score_tracker.csv')
score_add, score_sub, add_wrong, sub_wrong, score_tab, tab_wrong, score_square, square_wrong, score_cube, cube_wrong, score_recip,recip_wrong =0,0,0,0,0,0,0,0,0,0,0,0
tab=[]
sqr=[]
cube=[]
recip=[]
data=[]
tracker=["Date","Add Score", "Add Attempted", "Sub Score", "Sub Attempted","Table Score","Table Attempted","Squares Score","Squares Attempted","Cubes Score","Cubes Attempted","Reciprocals Score","Reciprocals Attempted"]
svd=0
rapidsc=0
rapidat=0
    
def get_score():
    data=[score_add,score_add+add_wrong,score_sub,sub_wrong+score_sub,score_tab,score_tab+tab_wrong,score_square,score_square+square_wrong,score_cube,score_cube+cube_wrong,score_recip,score_recip+recip_wrong]
    print("\n********Task**********Score********Attempted********\n")
    print("      Addition         "+str(data[0])+"             "+str(data[1]))
    print("      Subtraction      "+str(data[2])+"             "+str(data[3]))
    print("      Table            "+str(data[4])+"             "+str(data[5]))
    print("      Squares          "+str(data[6])+"             "+str(data[7]))
    print("      Cubes            "+str(data[8])+"             "+str(data[9]))
    print("      Reciprocals      "+str(data[10])+"             "+str(data[11]))
    print("\n")
    print("      Total            "+str(sum(data[0:11:2]))+"             "+str(sum(data[1:12:2])))
    

def res_scr():
    global score_add, score_sub, add_wrong, sub_wrong, score_tab, tab_wrong, score_square, square_wrong, score_cube, cube_wrong, score_recip,recip_wrong
    score_add, score_sub, add_wrong, sub_wrong, score_tab, tab_wrong, score_square, square_wrong, score_cube, cube_wrong, score_recip,recip_wrong =0,0,0,0,0,0,0,0,0,0,0,0
    global tab, sqr, cube, recip
    tab=[]
    sqr=[]
    cube=[]
    recip=[]

def int_inp(p):
    try:
        inp=int(input(p))
        return inp
    except ValueError:
        print("That's not an integer! Try again.")
        int_inp(p)

def inp_float(p):
    try:
        inp=float(input(p))
        return inp
    except ValueError:
        print("Not a valid input! Try again.")
        inp_float(p)
    

# Addition challenge    
def add_ch(s):
    global score_add
    global add_wrong
    global svd
    global rapidsc
    global rapidat
    t = time.time() + s
    while time.time() <= t:
        rapidat+=1
        a=r.randint(1000, 9999)
        b=r.randint(1000, 9999)
        c=int_inp("\n"+str(a)+"+"+str(b)+" = ")
        ans=a+b
        if c==ans:
            score_add+=1
            rapidsc+=1
            print("Correct!\n")
        else:
            add_wrong+=1
            print("Wrong!")
            print("Correct answer "+str(ans)+"\n")
    svd=0

#Subtraction challenge
def sub_ch(s):
    global score_sub
    global sub_wrong
    global svd
    global rapidsc
    global rapidat
    t = time.time() + s
    while time.time() <= t:
        rapidat==1
        a=r.randint(1000, 9999)
        b=r.randint(1000, 9999)
        #print("|"+a+"-"+b+"|= ")
        c=int_inp("\n"+"|"+str(a)+"-"+str(b)+"| = ")
        ans=abs(a-b)
        if c==ans:
            score_sub+=1
            rapidsc+=1
            print("Correct!\n")
        else:
            sub_wrong+=1
            print("Wrong!")
            print("Correct answer: "+str(ans)+"\n")
        
    svd=0

#Tables
def tab_ch(s):
    global score_tab
    global tab_wrong
    global tab
    global svd
    global rapidsc
    global rapidat
    t= time.time() + s
    while time.time() <= t:
        rapidat+=1
        a=r.randint(11, 30)
        b=r.randint(2, 10)
        c=int_inp("\n"+str(a)+" times "+str(b)+" = ")
        ans=a*b
        if c==ans:
            score_tab+=1
            rapidsc+=1
            print("Correct!\n")
        else:
            tab_wrong+=1
            tab+=[str(a)]
            print("Wrong!")
            print("Correct answer: "+str(ans)+"\n")    
    svd=0
    
#Squares
def sq_ch(s):
    global square_wrong
    global sqr
    global score_square
    global svd
    global rapidsc
    global rapidat
    i=0
    nums = list(range(5, 25))
    r.shuffle(nums)
    
    t= time.time() + s
    while time.time() <= t and i<len(nums):
        rapidat+=1
        a=nums[i]
        c=int_inp("\n"+str(a)+" squared = ")
        ans=a**2
        if c==ans:
            score_square+=1
            rapidsc+=1
            print("Correct!\n")
        else:
            square_wrong+=1
            sqr+=[str(a)]
            print("Wrong!")
            print("Correct answer: "+str(ans)+"\n")
        i+=1   
    svd=0
    
#Cubes
def cube_ch(s):
    global score_cube
    global cube_wrong
    global cube
    global svd
    global rapidsc
    global rapidat
    i=0
    nums = list(range(4, 15))
    r.shuffle(nums)
    
    t= time.time() + s
    while time.time() <= t and i<len(nums):
        rapidat+=1
        a=nums[i]
        c=int_inp("\n"+str(a)+" cubed = ")
        ans=a**3
        print(ans)
        if c==ans:
            score_cube+=1
            rapidsc+=1
            
            print("Correct!")
        else:
            cube_wrong+=1
            cube+=[str(a)]
            print("Wrong!")
            print("Correct answer: "+str(ans)+"\n")
        i+=1    
    svd=0
    
#Reciprocals

def recip_ch(s):
    global score_recip
    global recip_wrong
    global recip
    global svd
    global rapidsc
    global rapidat
    t= time.time() + s
    while time.time() <= t:
        num=r.randint(1, 11)
        den=r.randint(1, 12)
        if num<den:
            rapidat+=1
            c='%.3f'%inp_float("\n"+str(num)+"/"+str(den)+"% = ")
            c=str(c[:-1])
            ans='%.3f'%(num*100/den)
            ans=str(ans[:-1])
            if str(c)==str(ans):
                score_recip+=1
                rapidsc+=1
                print("Correct!")
            else:
                recip_wrong+=1
                recip+=[str(num)+"/"+str(den)]
                print("Wrong!")
                print("Correct answer: "+str(ans)+"\n")
    
    svd=0
    
#CSV Writer/Updater
def wrt_scrs():
    global svd
    data=[dat,score_add,score_add+add_wrong,score_sub,sub_wrong+score_sub,score_tab,score_tab+tab_wrong,score_square,score_square+square_wrong,score_cube,score_cube+cube_wrong,score_recip,score_recip+recip_wrong]
    try:
        with open("score_tracker.csv", 'r') as scrfl:
            reader = csv.DictReader(scrfl)
            head = reader.fieldnames
    except FileNotFoundError:
        print("\nscores_tracker file not found! Creating new!")
        with open('score_tracker.csv', 'w', newline='') as fl:
            scrdt = csv.writer(fl)
            scrdt.writerow(tracker)
            head=["Date","Add Score", "Add Attempted", "Sub Score", "Sub Attempted","Table Score","Table Attempted","Squares Score","Squares Attempted","Cubes Score","Cubes Attempted","Reciprocals Score","Reciprocals Attempted"]
    if head!=tracker: 
        print("\nEither no score history is present or the file has been modified.\nResetting file contents!")
        with open('score_tracker.csv', 'w', newline='') as fl:
            scrdt = csv.writer(fl)
            scrdt.writerow(tracker)
            #print(head)
    scrfl=open('score_tracker.csv','a', newline='')
    scrdt=csv.writer(scrfl)
    scrdt.writerow(data)
    scrfl.close()
    print("\nScores saved to score_tracker.csv")
    svd=1


def spec_ch():
    global tab
    global sqr
    global cube
    global recip
    tasks="a)   Addition \ns)   Subtraction \nsq)  Squares \nc)   Cubes \nt)   Tables \nr)   Reciprocals \ngg)  Back to main menu"
    t=input("\nAvailable tasks:\n"+tasks+"\n\nPlease enter your option: ")
    if t=="gg":
        start_ch()
    elif t.lower()=="a":
        print("\nFour digit addition [5 mins] ")
        res=input("Press any key to start, gg to skip -> ")
        if res.lower()!="gg":
            add_ch(300)
    elif t.lower()=="s":
        print("\nFour digit subtraction, enter absolute values only. [5 mins]")
        res=input("Press any key to start, gg to skip -> ")
        if res.lower()!="gg":
            sub_ch(300)
    elif t.lower()=="sq":
        print("\nDo you remember the squares upto 30? Let's see! [30 secs]")
        res=input("Press any key to start, gg to skip -> ")
        if res.lower()!="gg":
            sq_ch(30)
            if len(sqr)!=0:
                print("Squares you got wrong:", end=" ")
                print(*sqr, sep=", ")
                sqr=[]
    elif t.lower()=="c":
        print("\nDo you remember the cubes upto 15? Let's see! 15 secs")
        res=input("Press any key to start, gg to skip -> ")
        if res.lower()!="gg":
            cube_ch(15)
            if len(cube)!=0:
                print("Cubes you got wrong:", end=" ")
                print(*cube, sep=", ")
                cube=[]
    elif t.lower()=="t":
        print("\nNow, let's see if you remember the multiplication table upto 30. [1 min]")
        res=input("Press any key to start, gg to skip -> ")
        if res.lower()!="gg":
            tab_ch(60)
            if len(tab)!=0:
                print("Tables you got wrong:", end=" ")
                print(*tab, sep=", ")
                tab=[]
    elif t.lower()=="r":
        print("\nDo you remember your reciprocals? Answer reciprocals as percentage only and upto 2 places of decimal. For example, 1/2 as 50 (no % after your answer). Let's see! [30 secs]")
        res=input("Press any key to start, gg to skip -> ")
        if res.lower()!="gg":
            recip_ch(30)
            if len(recip)!=0:
                print("Reciprocals you got wrong:", end=" ")
                print(*recip, sep=", ")
                recip=[]
    else:
        print("\nEnter a valid option")
        spec_ch()
    print("\nChallenge completed!")
    get_score()
    spec_ch()    
        
        

def start_ch():
    global tab
    global sqr
    global cube
    global recip
    global rapidsc
    global rapidat
    print("\nWould you like to \na)  Go through the complete practice mode  \nb)  Try a specific challenge \nf)  Try challenge mode (10 mins, random problems)\nr)  Reset the score_tracker file, this will erase all the saved scores.  \ns)  Save current scores to the score_tracker file \nv)  View session scores \nd)  Reset session score\ngg) Exit, you can save your scores before exiting as well.")
    f=input("\nEnter your choice: ")
    if f.lower()=="r":
        filename = "score_tracker.csv"
        fl = open(filename, "w+")
        fl.close()
        print("\nFile was reset successfully")
        start_ch()
    elif f=="gg":
        if svd!=1:
            i=input("\nLatest session scores have not been saved, enter any key to save scores to the score_tracker file except for N to discard\n")
            if i.lower()!="n":
                wrt_scrs()
            else:
                print("\nTerminating program without saving scores....")
        else:
            print("\nSession scores have already been saved! Terminating....")
        print("\nProgram terminated!")
        sys.exit(0)
    elif f=='s':
        wrt_scrs()
    elif f.lower()=="a":
        print("\nFour digit addition [5 mins] ")
        res=input("Press any key to start, gg to skip -> ")
        if res.lower()!="gg":
            add_ch(300)
        print("\nFour digit subtraction, enter absolute values only. [5 mins]")
        res=input("Press any key to start, gg to skip -> ")
        if res.lower()!="gg":
            sub_ch(300)
        print("\nNow, let's see if you remember the multiplication table upto 30. [1 min]")
        res=input("Press any key to start, gg to skip -> ")
        if res.lower()!="gg":
            tab_ch(60)
            if len(tab)!=0:
                print("Tables you got wrong:", end=" ")
                print(*tab, sep=", ")
                tab=[]
        print("\nDo you remember the squares upto 30? Let's see! [30 secs]")
        res=input("Press any key to start, gg to skip -> ")
        if res.lower()!="gg":
            sq_ch(30)
            if len(sqr)!=0:
                print("Squares you got wrong:", end=" ")
                print(*sqr, sep=", ")
                sqr=[]
        print("\nDo you remember the cubes upto 15? Let's see! 15 secs")
        res=input("Press any key to start, gg to skip -> ")
        if res.lower()!="gg":
            cube_ch(30)
            if len(cube)!=0:
                print("Cubes you got wrong:", end=" ")
                print(*cube, sep=", ")
                cube=[]
        print("\nDo you remember your reciprocals? Answer reciprocals as percentage only and upto 2 places of decimal. For example, 1/2 as 50 (no % after your answer). Let's see! [30 secs]")
        res=input("Press any key to start, gg to skip -> ")
        if res.lower()!="gg":
            recip_ch(30)
            if len(recip)!=0:
                print("Reciprocals you got wrong:", end=" ")
                print(*recip, sep=", ")
                recip=[]
        print("Challenge completed!\n")
        get_score()
    elif f.lower()=="b":
        spec_ch()
    elif f.lower()=="v":
        get_score()
        start_ch()
    elif f.lower()=="d":
        res_scr()
        print("\nSession scores have been reset!")
        start_ch()
    elif f.lower()=='f':
        rapidsc=0
        rapidat=0
        print("\nWelcome to challenge mode [10 mins]")
        res=input("Press any key to start, gg to go back to main menu -> ")
        if res.lower()!="gg":
            rapid_mode(600)
            print("\nYou scored "+str(rapidsc)+" out of "+str(rapidat)+" problems that you attempted" )
        rapidsc=0
        rapidat=0
    else:
        print("\nWrong input")
        start_ch()
    start_ch()    

def rapid_mode(s):
    global sqr
    global cube
    global recip
    global tab
    t=time.time() + s
    while time.time()<=t:
        c=r.randint(1, 6)
        if c==1:
            add_ch(1)
        elif c==2:
            sub_ch(1)
        elif c==3:
            tab_ch(1)
            tab=[]
        elif c==4:
            recip_ch(1)
            recip=[]
        elif c==5:
            sq_ch(1)
            sqr=[]
        else:
            cube_ch(1)
            cube=[]
        
print("\nWelcome to the speed math challange, each test has some limited time to complete, try to get as much score as possible. \nI advise taking this test (or any other) daily to improve faster. Please don't use calculators and try to use pen as less as possible. You are only cheating with yourself by using a calculator.\n")
start_ch()
        