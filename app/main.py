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
        print("That's not an integer! Try again.\n")
        int_inp(p)

def inp_float(p):
    try:
        inp=float(input(p))
        return inp
    except ValueError:
        print("Not a valid input! Try again.\n")
        inp_float(p)
    

# Addition challenge    
def add_ch():
    global score_add
    global add_wrong
    global svd
    print("\nAdd these numbers, 5 mins ")
    res=input("Press any key to start, gg to skip")
    if res.lower()!="gg":
        t = time.time() + 60 * 5
        while time.time() <= t:
            a=r.randint(1000, 9999)
            b=r.randint(1000, 9999)
            c=int_inp(str(a)+"+"+str(b)+"= ")
            ans=a+b
            if c==ans:
                score_add+=1
                print("Correct!")
            else:
                add_wrong+=1
                print("Wrong!")
                print("Correct answer "+str(ans)+"\n")
    svd=0

#Subtraction challenge
def sub_ch():
    global score_sub
    global sub_wrong
    global svd
    print("\nSubtract these numbers, enter absolute values, 5 mins")
    t = time.time() + 60 * 5
    res=input("Press any key to start, gg to skip")
    if res.lower()!="gg":
        while time.time() <= t:
            a=r.randint(1000, 9999)
            b=r.randint(1000, 9999)
            #print("|"+a+"-"+b+"|= ")
            c=int_inp("|"+str(a)+"-"+str(b)+"|= ")
            ans=abs(a-b)
            if c==ans:
                score_sub+=1
                print("Correct!")
            else:
                sub_wrong+=1
                print("Wrong!")
                print("Correct answer: "+str(ans)+"\n")
    svd=0

#Tables
def tab_ch():
    global score_tab
    global tab_wrong
    global tab
    global svd
    print("\nNow, let's see if you remember the multiplication table upto 30, 1 min")
    t= time.time() + 60
    res=input("Press any key to start, gg to skip")
    if res.lower()!="gg":
        while time.time() <= t:
            a=r.randint(11, 30)
            b=r.randint(3, 30)
            c=int_inp(str(a)+" times"+str(b)+"= ")
            ans=a*b
            if c==ans:
                score_tab+=1
                print("Correct!")
            else:
                tab_wrong+=1
                tab+=[str(a)]
                print("Wrong!")
                print("Correct answer: "+str(ans)+"\n")
    svd=0
    if len(tab)!=0:
        print("Tables you got wrong:", end=" ")
        print(*tab, sep=", ")
        tab=[]
#Squares
def sq_ch():
    global square_wrong
    global sqr
    global score_square
    global svd
    i=0
    nums = list(range(5, 25))
    r.shuffle(nums)
    print("\nDo you remember the squares upto 30? Let's see! 30 secs")
    t= time.time() + 30
    res=input("Press any key to start, gg to skip")
    if res.lower()!="gg":
        while time.time() <= t:
            a=nums[i]
            c=int_inp(str(a)+" squared= ")
            ans=a**2
            if c==ans:
                score_square+=1
                print("Correct!")
            else:
                square_wrong+=1
                sqr+=[str(a)]
                print("Wrong!")
                print("Correct answer: "+str(ans)+"\n")
            i+=1
    svd=0
    if len(sqr)!=0:
        print("Squares you got wrong:", end=" ")
        print(*sqr, sep=", ")
        sqr=[]
#Cubes
def cube_ch():
    global score_cube
    global cube_wrong
    global cube
    global svd
    i=0
    nums = list(range(4, 15))
    r.shuffle(nums)
    print("\nDo you remember the cubes upto 15? Let's see! 30 secs")
    t= time.time() + 30
    res=input("Press any key to start, gg to skip")
    if res.lower()!="gg":
        while time.time() <= t:
            a=nums[i]
            c=int_inp(str(a)+" cubed = ")
            ans=a**3
            print(ans)
            if c==ans:
                score_cube+=1
                print("Correct!")
            else:
                cube_wrong+=1
                cube+=[str(a)]
                print("Wrong!")
                print("Correct answer: "+str(ans)+"\n")
            i+=1
    svd=0
    if len(cube)!=0:
        print("Cubes you got wrong:", end=" ")
        print(*cube, sep=", ")
        cube=[]
#Reciprocals

def recip_ch():
    global score_recip
    global recip_wrong
    global recip
    global svd
    print("\nDo you remember your reciprocals? Answer reciprocals as percentage only and upto 2 places of decimal. For example. 1/2 as 50 (no % after your answer). Let's see! 20 secs")
    res=input("Press any key to start, gg to skip")
    if res.lower()!="gg":
        t= time.time() + 20
        while time.time() <= t:
            num=r.randint(1, 11)
            den=r.randint(1, 12)
            if num<den:
                c='%.3f'%inp_float("\n"+str(num)+"/"+str(den)+"% = ")
                c=str(c[:-1])
                ans='%.3f'%(num*100/den)
                ans=str(ans[:-1])
                if str(c)==str(ans):
                    score_recip+=1
                    print("Correct!")
                else:
                    recip_wrong+=1
                    recip+=[str(num)+"/"+str(den)]
                    print("Wrong!")
                    print("Correct answer: "+str(ans)+"\n")        
    svd=0
    if len(recip)!=0:
        print("Reciprocals you got wrong:", end=" ")
        print(*recip, sep=", ")
        recip=[]
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
        with open('score_tracker.csv', 'w') as fl:
            scrdt = csv.writer(fl)
            scrdt.writerow(tracker)
            head=["Date","Add Score", "Add Attempted", "Sub Score", "Sub Attempted","Table Score","Table Attempted","Squares Score","Squares Attempted","Cubes Score","Cubes Attempted","Reciprocals Score","Reciprocals Attempted"]
    if head!=tracker: 
        print("\nEither no score history is present or the file has been modified.\nResetting file contents!")
        with open('score_tracker.csv', 'w') as fl:
            scrdt = csv.writer(fl)
            scrdt.writerow(tracker)
            print(head)
    scrfl=open('score_tracker.csv','a')
    scrdt=csv.writer(scrfl)
    scrdt.writerow(data)
    scrfl.close()
    print("\nScores saved to score_tracker.csv")
    svd=1


def spec_ch():
    tasks="a) Addition, s) Subtraction, sq) Squares, c) Cubes, t) Tables, r) Reciprocals, gg) Back to main menu"
    t=input("\nAvailable tasks: "+tasks+"\nPlease enter your option: ")
    if t=="gg":
        start_ch()
    if t.lower()=="a":
        add_ch()
    if t.lower()=="s":
        sub_ch()
    if t.lower()=="sq":
        sq_ch()
    if t.lower()=="c":
        cube_ch()
    if t.lower()=="t":
        tab_ch()
    if t.lower()=="r":
        recip_ch()  
    print("\nChallenge completed!")
    get_score()
    spec_ch()    
        
        

def start_ch():
    print("\nWould you like to \na)  Go through the complete challenge \nb)  Try a specific challenge? \nr)  Reset the score_tracker file  \ns)  Save current scores to the score_tracker file \nv)  View session scores \nd)  Reset session score\ngg) Exit")
    f=input("Enter your choice: ")
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
        add_ch()
        sub_ch()
        tab_ch()
        sq_ch()
        cube_ch()
        recip_ch()
        print("Challenge completed!\n")
        get_score()
    elif f.lower()=="b":
        spec_ch()
    elif f.lower()=="v":
        get_score()
        start_ch()
    elif f.lower()=="d":
        res_scr()
        print("\nReset complete")
        get_score()
        start_ch()
    else:
        print("\nWrong input")
        start_ch()
    start_ch()    
#get_score()
print("\nWelcome to the speed math challange, each test has some limited time to complete, try to get as much score as possible. \nI advise taking this test (or any other) daily to improve faster. Please don't use calculators and try to use pen as less as possible. You are only cheating yourself by using a calculator.\n")
start_ch()
        