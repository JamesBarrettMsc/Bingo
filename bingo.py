############################
## Author James
## Date 18.02.22
## V.0.0.1 
############################
import random
import sys
import os
import time

from playsound import playsound # type: ignore
from termcolor import colored


# unused_in_columns indicates  totat numbere of blank square.
# [18-x  blank square]
#This will keep track of the columne total numbers,
#shuch the no one columns has exceeds its number range.
##[1-9, 10-19, 20-29,....,80-90].
unused_in_columns =[8,7,7,7,7,7,7,7,6]


def generation_tickit_alt():
#declare a list to hold a box.
    box=[]

    #Placeing the blank squares in a row
    #Such that on one rew have more 4 blank square in it. 
    for i in range(6):
        
        row = [0]*9 
        row_range =[0,1,2,3,4,5,6,7,8]
        #row_range =[range(0, 9)]
        
        #Removing the position that have been maked a blank square,
        #in the columns.
        for x in range(9):
            if unused_in_columns[x]==-1:
                row_range.remove(x)
        
        #Populationing the rows such no one row has more then four
        #blank square.
        for x in range(4):
            n= (random.choice(row_range))
            row_range.remove(n) # remove used position. 
            row[n]=-1
            unused_in_columns[n] =unused_in_columns[n]-1
            
        box.append(row)

    #print(box)

generation_tickit_alt()


#input("::")

def generation_tickit() ->list:

    #declare a list to hold a box.
    box=[]
    #Placeing the blank squares in a row
    #Such that on one rew have more 4 blank square in it. 
    for i in range(3):
        
        row = [0]*9 
        row_range =[0,1,2,3,4,5,6,7,8]
        #row_range =[range(0, 9)]
        
        #Removing the position that have been maked a blank square,
        #in the columns.
        for x in range(9):
            if unused_in_columns[x]==-1:
                row_range.remove(x)

        #Populationing the rows such no one row has more then four
        #blank square.
        for x in range(4):
            n= (random.choice(row_range))
            row_range.remove(n) # remove used position. 
            row[n]=-1
            unused_in_columns[n] =unused_in_columns[n]-1
            
        box.append(row)

    return box



def greet(*names):
    """ This function greets all
    the person in the names tuple. """
    
    for name in names:
       print("Hello", name)

#greet("Monic","Luke", "Steve", "John")


def generation_sheet() ->list:

    while True:   
        sheet=[]
        try:
            for i in range(6):
                sheet.append(generation_tickit())
        except:
            columns_vel =[8,7,7,7,7,7,7,7,6]
    
            for x in range(9):
                unused_in_columns[x]=columns_vel[x]                    
            #print("oppes")   
            pass
        
        else:
            break
        
    return sheet

def populate_numbers(sheet):

    for z in range(9):
        if z==0:
            columns_val =[1,2,3,4,5,6,7,8,9]
        elif z==8:
            columns_val =[1,2,3,4,5,6,7,8,9,0,"+",]
        else:
            columns_val =[1,2,3,4,5,6,7,8,9,0]
        
        for y in range(6):
            
            for x in range(3):
                
                if sheet[y][x][z] !=-1:
                    n =random.choice(columns_val)
                    columns_val.remove(n)

                    if(n != "+"):
                        sheet[y][x][z]=str(z)+str(n)
                    else:
                        sheet[y][x][z]=90




def save_to_text_file(sheet):
    # the following will demonstrate how to, write text to a file
    #If the file does not exist. It will be created at this point.

    name=input("Players name ::")

    f = open(name+"'s Sheet.txt", "w+")
    
    
    f.write("\n Good Luck "+name+"\n")
    f.write("\n++++++++++++++++++++++++++++++++++++\n")
    
    for x in range(len(sheet)):
        
        for y in range(len(sheet[x])):
            for z in range(len(sheet[x][y])):
                if sheet[x][y][z]==-1:
                    f.write("|--|",)
                else:
                    f.write("|"+str(sheet[x][y][z])+"|")           
            f.write("\n")
            
        f.write("++++++++++++++++++++++++++++++++++++\n")
        
    
def cli_draw_sheet(sheet):
    
    for x in range(len(sheet)):   
        print("\n++++++++++++++++++++++++++++++++++++\n")
        for y in range(len(sheet[x])):
            for z in range(len(sheet[x][y])):
                if sheet[x][y][z]==-1:
                    print("|▓▓|",end="")
                else:
                    print("|"+str(sheet[x][y][z])+"|",end="")            
            print()
            
    
##############################
def caller():
    
    numbers_not_called= []
    numbers_called= []
    borad= []
    
    for x in range(1,91):
        numbers_not_called.append(x)
        
    for x in range(9):
        borad.append([])
        
        for y in range(10):
            borad[x].append(["▓▓"])
            
    while len(numbers_not_called)>0:
        
        os.system('cls')
        
        n =random.choice(numbers_not_called)
        numbers_not_called.remove(n)
        numbers_called.append(n)
        

        ones=n%10
        
        if n >9:
            tens=(n-ones)//10
                   
            if ones !=0:
                borad[tens][ones-1]="['"+str(tens)+str((ones))+"']"
            else:
                borad[tens-1][ones-1]="['"+str(tens)+str((ones))+"']"
            
        else:
            borad[0][n-1]="['0"+str((n))+"']"
            
       

        tensAscii=[]
        if n >9:
            with open('src/numbers/'+str(tens)+'.txt') as f:
                lines = f.readlines()
                
                for x in range(len(lines)):
                    tensAscii.append(lines[x])
        else:
            with open('src/numbers/0.txt') as f:
                lines = f.readlines()
                
                for x in range(len(lines)):
                    tensAscii.append(lines[x])
                    
        with open('src/numbers/'+str(ones)+'.txt') as f:
            
            lines = f.readlines()
            
            for x in range(len(lines)):
                print('\t'+tensAscii[x].replace("\n", ""),lines[x],end="")
      
        print()
        try:
            path ='src\\sounds\\'+str(n)+'_jb.mp3'
            playsound(path)
        except:
            print('missing sounds '+str(n)+'_jb.mp3')
            pass
        
        
        
        for x in range(9):
            print()
            for y in range(10):#
                if  "▓▓" in str(borad[x][y]):
                    print(colored(str(borad[x][y]),'green'),end="")
                else:
                    print( colored(str(borad[x][y]),'red'),end="")
                    
                
    
        input("\n::")
        
        
def txt_to_sheet(sheet):
    pass
    

def check(sheet):
    pass

def faux_animation(animation):
        
    os.system('cls')


    DIR = '/animationz/'+animation
    
    print (len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))
    
    for x in range(len(lines)):
        with open('animation/'+1+'.txt') as f:
            lines = f.readlines()
            
            for x in range(len(lines)):
                print(lines[x])
     
      


    print(
"""
.########.
.##.....##
.##.....##
.########
.##.....##
.##.....##
.########
""",)
    time.sleep(.5)
    
    
    os.system('cls')
    print(
"""
.########..####
.##.....##..##
.##.....##..##
.########...##
.##.....##..##
.##.....##..##
.########..####
""",)
    time.sleep(.5)    
    
    os.system('cls')

    print(
"""
.########..####.##....##
.##.....##..##..###...##
.##.....##..##..####..##
.########...##..##.##.##
.##.....##..##..##..####
.##.....##..##..##...###
.########..####.##....##
""",)
    time.sleep(.5)    
    
    os.system('cls')

    print(
"""
.########..####.##....##..######.
.##.....##..##..###...##.##....##
.##.....##..##..####..##.##......
.########...##..##.##.##.##...####
.##.....##..##..##..####.##....##
.##.....##..##..##...###.##....##
.########..####.##....##..######
""",)
    time.sleep(.5)
    
     
      
    os.system('cls')
    
    print(
"""
.########..####.##....##..######....#######
.##.....##..##..###...##.##....##..##.....##
.##.....##..##..####..##.##........##.....##
.########...##..##.##.##.##...####.##.....##
.##.....##..##..##..####.##....##..##.....##
.##.....##..##..##...###.##....##..##.....##
.########..####.##....##..######....#######
""",)
    time.sleep(.5)
    
    
          
    os.system('cls')
    print(
"""
.########..####.##....##..######....#######..####
.##.....##..##..###...##.##....##..##.....##.####
.##.....##..##..####..##.##........##.....##.####
.########...##..##.##.##.##...####.##.....##..##.
.##.....##..##..##..####.##....##..##.....##.....
.##.....##..##..##...###.##....##..##.....##.####
.########..####.##....##..######....#######..####
""",)
    time.sleep(.5)
    
    
    
def main():
    
    #faux_animation("animation")
    
    while True:
        
        os.system('cls')
        print(
"""
++++++++++++++++++++++++++++++++++
+     Lets binGO already!!!      +
----------------------------------
+                                + 
+    1) Sart a Game              +
+    2) Generation Sheet         +
+                                +
++++++++++++++++++++++++++++++++++
""",end="")
        op= input("::")    

        if "1" in op:
            caller()
            
        elif "2" in op:
            sheet=generation_sheet()
            populate_numbers(sheet)
            save_to_text_file(sheet)
            
    
##Main##    
#######################################################
# Using the special variable 
# __name__
if __name__=="__main__":
    main()

#######################################################        
        
"""
#######################################################
##  TESTING
##
"""

def total_numbers_columns(sheet):
    
   columns_totals =[0,0,0,0,0,0,0,0,0]

   for x in range(len(sheet)):
        print(str(x),end="=")
        
        for y in range(len(sheet[x])):
            individual=0

            for z in range(len(sheet[x][y])):
                if sheet[x][y][z]==-1:
                    columns_totals[z]+=1
            
        print(str(columns_totals))
        


def total_numbers_row(sheet):
    
   total=[]
  
   #boxs
   for x in range(len(sheet)):
        print("boxs "+str(x))
        
        for y in range(len(sheet[x])):
            print("row "+str(y),end=", ")
            row_total=0
            
            for z in range(len(sheet[x][y])):
                
                if sheet[x][y][z]==-1:
                     row_total+=1
                    
            print("=="+str(row_total))
            
            if row_total !=4:
                print(str(y)+"NOT !")


        




