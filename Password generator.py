import tkinter as tk
import random
import tkinter.ttk as ttk

root = tk.Tk()
#win.geometry("360x400")  

c = tk.Canvas(root , height = 400 , width = 400)
c.pack()


end = ' '
#functions


#Symbols
def symbols():
    ordd = 33
    sym = []

    run = True
    while run:
        add = chr(ordd)
        sym.append(add)
        ordd +=1
        if ordd == 47:
            print(sym)
            break

    

#Numbers
def numbers():
    num = []

    for x in range(10):
        add1 = x
        num.append(add1)
    print(num)

    
def sub_button():
    
    #number selected in password length 
    selected = var.get()
    #print(selected)

    #If Checkbox  selected
    print("\n")
    present_val1 = 0 
    z =  var1.get() 
    present_val = z
    sel1_list = []
    
    if present_val == 1:
        #Selection: Symbols
        range_val = int(selected)
        sym = ['!', '@', '#', '$', '%', '&', "^", '(', ')', '*', '+', ',', '-']
        for x in range(range_val):  #Add Number of Counts 1
            index1 = random.randint(0 , 12)
            sel1 = sym[index1]
            sel1_list.append(sel1)
            #print(sel1 , end = " " )
        print("\n")

    present_val2 = 0
    present_val2 = var2.get()
    sel2_list = []
    
    if present_val2 == 1:
        #Selection: Numbers
        range_val = int(selected)
        num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for x in range(range_val):  #Add Number of Counts 2
            index2 = random.randint(0 , 8)
            sel2 = num[index2]
            sel2_list.append(sel2)
            #print( sel2 , end = " " )
        print("\n")

    present_val3 = 0
    present_val3 = var3.get()
    sel3_list = []

    if present_val3 == 1:
        #Selection: Lowercase letters
        range_val = int(selected)
        low_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                    'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for x in range(range_val):  #Add Number of Counts 3
            index3 = random.randint(0 , 25)
            sel3 = low_case[index3]
            sel3_list.append(sel3)
            #print(sel3 , end = " " )

    present_val4 = 0
    present_val4 = var4.get()
    sel4_list = []
    
    if present_val4 == 1:
        #Selection: Uppercase letters
        range_val = int(selected)
        upp_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                    'H', 'I', 'J', 'K', 'L', 'M','N', 'O',
                    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        for x in range(range_val):  #Add Number of Counts 3
            index4 = random.randint(0 , 25)
            sel4 = upp_case[index4]
            sel4_list.append(sel4)
            #print(sel3 , end = " " )

    
    #print("\n",sel1_list)
    #print(sel2_list)
    #print(sel3_list , "\n")

#Values Selection Acccording to checkbox
            

    for w in range(1):  # Loop for 1 ,2 ,3 and 4 
        if present_val == 1:
            
            if present_val3 == 1 and present_val2 == 0 and present_val4 == 0:
                final = []
                for x in range(16):
                    range_val = int(selected)
                    #len_final = range_val
                    semi_final1 = sel1_list[x] #aa
                    semi_final3 = sel3_list[x]

                    final.append(semi_final1)
                    len_final = len(final)
                    if len_final == range_val:
                        break

                    final.append(semi_final3)
                    len_final = len(final)
                    if len_final == range_val:
                        break
                #print(final)
                result = ''
                for x in range(len(final)):
                    result+= str(final[x])
                #print(result)

                rem_len = len(result)
                text_box.delete(0 , 20)
                text_box.insert(0 , result)
                
                
                break

            if present_val4 == 1 and present_val2 == 0 and present_val3 == 0:          
                final = []
                for x in range(16):
                    range_val = int(selected)
                    #len_final = range_val
                    semi_final1 = sel1_list[x] #aa
                    semi_final4 = sel4_list[x]
                            
                    final.append(semi_final1)
                    len_final = len(final)
                    if len_final == range_val:
                        break

                    final.append(semi_final4)
                    len_final = len(final)
                    if len_final == range_val:
                        break
                #print(final)
                result = ''
                for x in range(len(final)):
                    result+= str(final[x])
                #print(result)

                rem_len = len(result)
                text_box.delete(0 , 20)
                text_box.insert(0 , result)
                
                break


            if present_val2 == 1 and present_val3 == 0 and present_val4 == 0:

                final = []
                for x in range(16):
                    range_val = int(selected)
                    #len_final = range_val
                    semi_final1 = sel1_list[x] #aa
                    semi_final2 = sel2_list[x]

                    final.append(semi_final1)
                    len_final = len(final)
                    if len_final == range_val:
                        break

                    final.append(semi_final2)
                    len_final = len(final)
                    if len_final == range_val:
                        break
                #print(final)
                result = ''
                for x in range(len(final)):
                    result+= str(final[x])
                #print(result)

                rem_len = len(result)
                text_box.delete(0 , 20)
                text_box.insert(0 , result)
                
                break

            if present_val2 == 1:
                
                if present_val4 == 1 and present_val3 == 0:          
                    final = []
                    for x in range(16):
                        range_val = int(selected)
                        #len_final = range_val
                        semi_final1 = sel1_list[x] #aa
                        semi_final2 = sel2_list[x]
                        semi_final4 = sel4_list[x]
                            
                        final.append(semi_final1)
                        len_final = len(final)
                        if len_final == range_val:
                            break

                        final.append(semi_final2)
                        len_final = len(final)
                        if len_final == range_val:
                            break
                        
                        final.append(semi_final4)
                        len_final = len(final)
                        if len_final == range_val:
                            break
                    #print(final)
                    result = ''
                    for x in range(len(final)):
                        result+= str(final[x])
                    #print(result)

                    rem_len = len(result)
                    text_box.delete(0 , 20)
                    text_box.insert(0 , result)
                    break

                if present_val3 == 1 and present_val4 == 0:          
                    final = []
                    for x in range(16):
                        range_val = int(selected)
                        #len_final = range_val
                        semi_final1 = sel1_list[x] #aa
                        semi_final2 = sel2_list[x]
                        semi_final3 = sel3_list[x]
                            
                        final.append(semi_final1)
                        len_final = len(final)
                        if len_final == range_val:
                            break

                        final.append(semi_final2)
                        len_final = len(final)
                        if len_final == range_val:
                            break
                        
                        final.append(semi_final3)
                        len_final = len(final)
                        if len_final == range_val:
                            break
                    #print(final)
                    result = ''
                    for x in range(len(final)):
                        result+= str(final[x])
                    #print(result)

                    rem_len = len(result)
                    text_box.delete(0 , 20)
                    text_box.insert(0 , result)
                
                    break

            
                if present_val3 == 1:
                    
                    if present_val4 == 1:
                        
                        final = []
                        for x in range(16):
                            range_val = int(selected)
                            #len_final = range_val
                            semi_final1 = sel1_list[x] #aa
                            semi_final2 = sel2_list[x]
                            semi_final3 = sel3_list[x]
                            semi_final4 = sel4_list[x]

                            final.append(semi_final1)
                            len_final = len(final)
                            if len_final == range_val:
                                break

                            final.append(semi_final2)
                            len_final = len(final)
                            if len_final == range_val:
                                break

                            final.append(semi_final3)
                            len_final = len(final)
                            if len_final == range_val:
                                break

                            final.append(semi_final4)
                            len_final = len(final)
                            if len_final == range_val:
                                break
                        #print(final)
                        result = ''
                        for x in range(len(final)):
                            result+= str(final[x])
                        #print(result)

                        rem_len = len(result)
                        text_box.delete(0 , 20)
                        text_box.insert(0 , result)
                
                        break

                        
                    final = []
                    for x in range(16):
                        range_val = int(selected)
                        #len_final = range_val
                        semi_final1 = sel1_list[x] #aa
                        semi_final2 = sel2_list[x]
                        semi_final3 = sel3_list[x]

                        final.append(semi_final1)
                        len_final = len(final)
                        if len_final == range_val:
                            break

                        final.append(semi_final2)
                        len_final = len(final)
                        if len_final == range_val:
                            break

                        final.append(semi_final3)
                        len_final = len(final)
                        if len_final == range_val:
                            break
                    #print(final)
                    result = ''
                    for x in range(len(final)):
                        result+= str(final[x])
                    #print(result)

                    rem_len = len(result)
                    text_box.delete(0 , 20)
                    text_box.insert(0 , result)
                
                    break

            if present_val3 == 1 and present_val2 == 0:

                if present_val4 == 1:

                    final = []
                    for x in range(16):
                        range_val = int(selected)
                        #len_final = range_val
                        semi_final1 = sel1_list[x] #aa
                        semi_final4 = sel4_list[x]
                        semi_final3 = sel3_list[x]

                        final.append(semi_final1)
                        len_final = len(final)
                        if len_final == range_val:
                            break

                        final.append(semi_final4)
                        len_final = len(final)
                        if len_final == range_val:
                            break

                        final.append(semi_final3)
                        len_final = len(final)
                        if len_final == range_val:
                            break
                    #print(final)
                    result = ''
                    for x in range(len(final)):
                        result+= str(final[x])
                    #print(result)

                    rem_len = len(result)
                    text_box.delete(0 , 20)
                    text_box.insert(0 , result)
                
                    break

                
            
            if present_val == 1 and present_val2 == 0 and present_val3 == 0 and present_val4 == 0:        
                print (sel1_list)
                result = ''
                for x in range(len(sel1_list)):
                    result+= str(sel1_list[x])
                #print(result)

                #print(range_val)
                rem_len = len(result)
                text_box.delete(0 , 20)
                text_box.insert(0 , result)
                break

# Loop for 2 ,3 and 4 

    for x in range(1):  
        if present_val2 == 1:
            
            if present_val3 == 1 and present_val == 0 and present_val4 == 0:
                final = []
                for x in range(16):
                    range_val = int(selected)
                    #len_final = range_val
                    semi_final2 = sel2_list[x] #aa
                    semi_final3 = sel3_list[x]

                    final.append(semi_final2)
                    len_final = len(final)
                    if len_final == range_val:
                        break

                    final.append(semi_final3)
                    len_final = len(final)
                    if len_final == range_val:
                        break
                #print(final)
                result = ''
                for x in range(len(final)):
                    result+= str(final[x])
                #print(result)
                
                rem_len = len(result)
                text_box.delete(0 , 20)
                text_box.insert(0 , result)
                break

            if present_val4 == 1 and present_val == 0 and present_val3 == 0:          
                final = []
                for x in range(16):
                    range_val = int(selected)
                    #len_final = range_val
                    semi_final2 = sel2_list[x] #aa
                    semi_final4 = sel4_list[x]
                            
                    final.append(semi_final2)
                    len_final = len(final)
                    if len_final == range_val:
                        break

                    final.append(semi_final4)
                    len_final = len(final)
                    if len_final == range_val:
                        break
                #print(final)
                result = ''
                for x in range(len(final)):
                    result+= str(final[x])
                #print(result)

                rem_len = len(result)
                text_box.delete(0 , 20)
                text_box.insert(0 , result)
                
                break


            if present_val3 == 1 and present_val == 0:
                
                if present_val4 == 1:          
                    final = []
                    for x in range(16):
                        range_val = int(selected)
                        #len_final = range_val
                        semi_final2 = sel2_list[x] #aa
                        semi_final3 = sel3_list[x]
                        semi_final4 = sel4_list[x]
                            
                        final.append(semi_final2)
                        len_final = len(final)
                        if len_final == range_val:
                            break

                        final.append(semi_final3)
                        len_final = len(final)
                        if len_final == range_val:
                            break
                        
                        final.append(semi_final4)
                        len_final = len(final)
                        if len_final == range_val:
                            break
                    #print(final)
                    result = ''
                    for x in range(len(final)):
                        result+= str(final[x])
                    #print(result)

                    rem_len = len(result)
                    text_box.delete(0 , 20)
                    text_box.insert(0 , result)
                    break

                
            if present_val2 == 1 and present_val == 0 and present_val3 == 0 and present_val4 == 0:        
                #print (sel2_list)
                result = ''
                for x in range(len(sel2_list)):
                    result+= str(sel2_list[x])
                #print(result)
                
                rem_len = len(result)
                text_box.delete(0 , 20)
                text_box.insert(0 , result)
                
                break
            

    
# Loop for 3 and 4 

    for y in range(1):  
        if present_val3 == 1:
            
            if present_val4 == 1 and present_val == 0 and present_val2 == 0:
                final = []
                for x in range(16):
                    range_val = int(selected)
                    #len_final = range_val
                    semi_final4 = sel4_list[x] #aa
                    semi_final3 = sel3_list[x]

                    final.append(semi_final4)
                    len_final = len(final)
                    if len_final == range_val:
                        break

                    final.append(semi_final3)
                    len_final = len(final)
                    if len_final == range_val:
                        break
                #print(final)
                result = ''
                for x in range(len(final)):
                    result+= str(final[x])
                #print(result)
                rem_len = len(result)
                text_box.delete(0 , 20)
                text_box.insert(0 , result)
                break

                
            if present_val3 == 1 and present_val == 0 and present_val2 == 0 and present_val4 == 0:        
                #print (sel3_list)
                result = ''
                for x in range(len(sel3_list)):
                    result+= str(sel3_list[x])
                #print(result)
                rem_len = len(result)
                text_box.delete(0 , 20)
                text_box.insert(0 , result)
                break

#Loop for number 4

    if present_val4 == 1 and present_val == 0 and present_val2 == 0 and present_val3 == 0:
        #print(sel4_list)
        result = ''
        for x in range(len(sel4_list)):
            result+= str(sel4_list[x])
        #print(result)
        
        #print(range_val)
        rem_len = len(result)
        end = result
        #print(end)
        
        text_box.delete(0 , 20)
        text_box.insert(0 , end)
        
        
 

# Title
title = tk.Label(c , text = "Strong Password Generator" , cursor = '' , font = ("sans serif" , '13' , 'italic') , fg = 'black').place(x = 90 , y = 30) 

                    
# Password length (Option value)
option_stmt = tk.Label(c , text = "Password Length : "  , font = ("times" , '11' , 'italic') )
c.create_window(85 , 92 , window = option_stmt)

var = tk.StringVar(c)
var.set("0") #Initial Value
pass_len = tk.OptionMenu(c , var ,  '4'  , '6' , '8' , '10' , '12' , '14' , '16'  , '20' )
pass_len.config(width = 15 , height = 0 , relief = 'raised'  , font = ('times' , '11') )

pass_len['borderwidth'] = 0.5
pass_len.pack()
c.create_window(291 , 88 , window = pass_len )


# Include Symbols (Normal Text)
s1 = tk.Label(c ,text = "Include Symbols :" , font = ("times" , '11' , 'italic') ).place(x = 20 , y = 116)
c.create_window(200 , 55 , window = s1)

s1_stmt = tk.Label(c ,text = "(eg. @%$#*&) " , font = ("times" , '11' , 'italic') ).place(x = 250, y = 116)
c.create_window(200 , 55 , window = s1_stmt)

var1 = tk.IntVar()
ch1 = tk.Checkbutton( c , variable = var1 )
ch1['borderwidth'] = 0
ch1.pack()
c.create_window(235 , 127 , window = ch1)


# (Normal Text)
s2 = tk.Label(c ,text = "Include Numbers :" , font = ("times" , '11' , 'italic') ).place(x = 20 , y = 150)
c.create_window(200 , 25 , window = s2)

s2_stmt = tk.Label(c ,text = "(eg. 1234) " , font = ("times" , '11' , 'italic') ).place(x = 250, y = 150)
c.create_window(200 , 25 , window = s2_stmt)

var2 = tk.IntVar()
ch2 = tk.Checkbutton( c , variable = var2 )
ch2.pack()
c.create_window(235 , 163 , window = ch2)


# (Normal Text)
s3 = tk.Label(c ,text = "Include Lowercase Letters :" , font = ("times" , '11' , 'italic') ).place(x = 20 , y = 183)
c.create_window(200 , 15 , window = s3)

s3_stmt = tk.Label(c ,text = "(eg. abcdef) " , font = ("times" , '11' , 'italic') ).place(x = 250, y = 183)
c.create_window(200 , 15 , window = s3_stmt)

var3 = tk.IntVar()
ch3 = tk.Checkbutton( c , variable = var3 )
ch3.pack()
c.create_window(235 , 195 , window = ch3)


# (Normal Text)
s4 = tk.Label(c ,text = "Include Uppercase Letters :" , font = ("times" , '11' , 'italic') ).place(x = 20 , y = 215)
c.create_window(250 , 35 , window = s3)

tk.Label(c , text = "(eg." , font = ("times" , '11' , 'italic') ).place(x = 250, y = 215)
s4_stmt = tk.Label(c ,text = " ABCDEF) " , font = ("times" , '10' , 'italic') ).place(x = 275, y = 215)
c.create_window(250 , 35 , window = s3_stmt)

var4 = tk.IntVar()
ch4 = tk.Checkbutton( c , variable = var4  , padx = -10 , pady = -10)
ch4.config(highlightcolor = 'black')
ch4.pack()
c.create_window(235 , 227 , window = ch4)


# Entry Box
text_box = tk.Entry(root , width = 28 , relief = 'groove' , bd = 2)
c.create_window(200 , 315 , window = text_box)

# Button
w = tk.Button( c , text = "Generate Password" , activeforeground = "green" , command =sub_button , fg = 'white' , bg = 'green'  )
c.create_window(200 , 275 , window = w)

# Message
m = tk.Label(c , text = "Note : Remember your password present in the above box" ,  fg = 'red' , font = ("times" , '10' , 'italic') ).place(x = 40 , y = 335)


    
c.mainloop()
