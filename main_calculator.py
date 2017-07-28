from tkinter import *

#############################main calculation function###########

def calculation(start_index,main_string):
    try:
        index=start_index
        while main_string[index] != ')':              ###Recursiveness for resolving paranthesis in Expression
            if main_string[index]=='(':
                main_string=calculation(index+1,main_string)
            index+=1

        index=start_index
        while main_string[index]!=')':
            if main_string[index]=='/':                                               ###Division
                a=float(main_string[index-1])/float(main_string[index+1])
                main_string=main_string[0:index-1]+[str(a)]+main_string[index+2:]
                index-=1
            index+=1

        index = start_index
        while main_string[index] != ')':
            if main_string[index] == '*':                                                   #Multiplication
                a = float(main_string[index - 1]) * float(main_string[index + 1])
                main_string = main_string[0:index - 1] + [str(a)] + main_string[index + 2:]
                index -= 1
            index += 1


        index = start_index
        while main_string[index] != ')':
            if main_string[index] == '-':                                                 #Subtraction
                if main_string[index-1]=='(':
                    main_string=main_string[0:index]+['0']+main_string[index:]
                    index+=1
                elif main_string[index-1]==')':
                    main_string=main_string[0:index+1]+['0']+main_string[index+1:]
                a = float(main_string[index - 1]) - float(main_string[index + 1])
                main_string = main_string[0:index - 1] + [str(a)] + main_string[index + 2:]
                index -= 1
            index += 1

        index = start_index
        while main_string[index] != ')':
            if main_string[index] == '+':
                if main_string[index-1]=='(':
                    main_string=main_string[0:index]+['0']+main_string[index:]
                    index+=1
                elif main_string[index-1]==')':
                    main_string=main_string[0:index+1]+['0']+main_string[index+1:]
                a = float(main_string[index - 1]) + float(main_string[index + 1])          #Addition
                main_string = main_string[0:index - 1] + [str(a)] + main_string[index + 2:]
                index -= 1
            index += 1

        main_string = main_string[0:start_index-1]+[main_string[start_index]]+main_string[start_index+2:]
        return main_string
    except ZeroDivisionError:
        main_string = ["Division by Zero is Undefined"]
        return main_string
    except:
        if not main_string == ["Division by Zero is Undefined"]:
            main_string = ["Expreesion invalid"]
        return main_string

###########################Calculator Function that perform changes on main_string ##################


def calculator(main_string):
    main_string = '(' + main_string + ')'
    main_list = []
    for i in range(len(main_string) - 1):
        if main_string[i] in ')1234567890' and main_string[i + 1] in '(':
            main_string = main_string[0:i + 1] + '*' + main_string[i + 1:]
        elif main_string[i] in ')' and main_string[i + 1] in '(0123456789':
            main_string = main_string[0:i + 1] + '*' + main_string[i + 1:]
    breakpoint = ['(', ')', '+', '-', '*', '/']
    flag = 0
    for i in range(len(main_string)):
        if main_string[i] in breakpoint:
            if flag > 0:
                main_list.append(main_string[i - flag:i])

            main_list.append(main_string[i])
            flag = 0
        else:
            flag += 1
    main_string = main_list
    main_string=calculation(1,main_string)
    main_string = "".join(main_string)
    try:
        if int(float(main_string)) == float(main_string) and main_string[-2] == '.':
            ans = str(int(main_string[:-2]))
        else:
            ans = main_string
        return ans
    except:
        if main_string=="Division by Zero is Undefined":
            return main_string
        else:
            return "Expreesion invalid"


#######################################Class button that grid button in GUI and also binding is defined in this function #####################

class button(Button):
    def __init__(self,master_frame,button_title,rowno,column_no,column_span=1,width=1,textbox=None,label=None):
        Button.__init__(self,master_frame,text=button_title,bg="grey",width=width,borderwidth=5)
        self.grid(row=rowno,column=column_no,pady=4,padx=4,sticky=W,columnspan=column_span)
        def insert_text(self):
            textbox.insert(INSERT,button_title)
        def clear_screen(self):
            textbox.delete(0.0, END)
            textbox.insert(0.0, "0\n")
        def calculator_calling(self):
            main_string=textbox.get()
            textbox.delete(0,END)
            label['text']=main_string
            ans=calculator(main_string)
            textbox.insert(INSERT,ans)
        if not button_title in ['C','=']:
            self.bind('<Button-1>',insert_text)
        if  button_title =='C':
            self.bind('<Button-1>',clear_screen)
        if button_title=='=':
            self.bind('<Button-1>',calculator_calling)
        root.bind('<Return>',calculator_calling)


###############################Row class that defines row in window##################

class row():
    def __init__(self,master_frame,rowno,b1,b2,b3,b4,b5=None,Textbox=None,LabelW=None):
        self.button1=button(master_frame,b1,rowno,0,textbox=Textbox,label=LabelW)
        self.button2 = button(master_frame, b2, rowno, 1,textbox=Textbox,label=LabelW)
        self.button3 = button(master_frame, b3, rowno, 2,textbox=Textbox,label=LabelW)
        if b5==None:
             self.button4 = button(master_frame, b4, rowno,3,column_span=2,width=9,textbox=Textbox,label=LabelW)
        else:
             self.button4 = button(master_frame, b4, rowno,3,textbox=Textbox,label=LabelW)
             self.button5 = button(master_frame, b5, rowno,4,textbox=Textbox,label=LabelW)

##################################class Calculator ######################3


class Calculator(Frame):
    def __init__(self,master):
        Frame.__init__(self,master,width=60,height=60)
        self.pack(padx=4,pady=2,fill=X)
        self.create_widget()
    def create_widget(self):
        ############################Expression##########

        self.label=Label(self,font=("Helvatica",15),text="Welcome")
        self.label.grid(row=1, columnspan=2555,sticky=W)

        #########################textbox#############

        self.textbox=Entry(self,width=25,font=("Helvatica",15))
        self.textbox.grid(row=2,columnspan=5)

        ########################################row1####

        row1=row(self,3,"7","8","9","+","C",Textbox=self.textbox,LabelW=self.label)

        ########################################row2####

        row2 = row(self, 4, "4", "5", "6", "-", "(",Textbox=self.textbox,LabelW=self.label)

        ########################################row3####

        row3 = row(self, 5, "1", "2", "3", "*", ")",Textbox=self.textbox,LabelW=self.label)

        ########################################row4####

        row2 = row(self, 6, "0", ".", "/","=",Textbox=self.textbox,LabelW=self.label)

###############Main Function###################

root=Tk()
root.title("Piyush's Calculator")
Calc1=Calculator(root)
root.mainloop()