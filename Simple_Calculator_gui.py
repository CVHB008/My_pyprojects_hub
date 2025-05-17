import tkinter as tk
import tkinter.messagebox as mb

calc = tk.Tk()
calc.title("CALCULATOR")

calc.geometry('320x350')

symbol = tk.StringVar()
symbol.set('Select')


def evaluate(left_op,symbol,right_op):
    
    if symbol == '+':
        result = left_op + right_op
    elif symbol == '-':
        result = left_op - right_op
    elif symbol == '*':
        result = left_op * right_op
    elif symbol == '/':
        result = left_op / right_op
        if abs(int(result)) == abs(float(result)):
            result = int(result)
    else:
        mb.showinfo('ERROR','Some error occured')
        
    ans.delete(0,'end')
    ans.insert(0,f'{result}')
    
def get_input():
    left_op = 0
    right_op = 0
    
    input_error = False
    
    if left.get() != '' and right.get() != '':
        if '.' in left.get():
            left_op = float(left.get())
        else:
            left_op = int(left.get())

        if '.' in right.get():
            right_op = float(right.get())
        else:
            right_op = int(right.get())
    else:
        input_error = True

    symb = symbol.get()
    if symbol.get() == 'Select':
        input_error = True

    if input_error :
        mb.showinfo('ERROR','Please check your inputs.')
    else:
        evaluate(left_op,symb,right_op)


#Defining Labels
labelhead = tk.Label(calc,text= 'CALCULATOR',font=('Ariel',16),fg = 'Green',relief = 'ridge',padx = 5)
left_label = tk.Label(calc,text= 'First number  ',font=('Ariel',9))
right_label = tk.Label(calc,text= 'Second number  ',font=('Ariel',9))
symb_label = tk.Label(calc,text= 'Select Symbol ',font=('Ariel',9))
label = tk.Label(calc,text =f'Answer  = ',font = ('Ariel',12))

#Placing Labels
labelhead.place(x = 90,y = 10)
left_label.place(x = 30,y = 60)
right_label.place(x = 30,y = 120)
symb_label.place(x = 30,y = 180)
label.place(x = 32,y = 280)

#Defining Entries
left = tk.Entry(calc,font=('Ariel',9),borderwidth = 2)
right = tk.Entry(calc,font=('Ariel',9),borderwidth = 2)
ans  = tk.Entry(calc,font = ('Ariel',12))

#Dropdown Menu for Symbols
symb = tk.OptionMenu(calc,symbol,'Select','+','-','*','/')
symb.place(x = 130,y = 176)

#Placing Entries
left.place(x = 130,y = 60)
right.place(x = 130,y = 120)
ans.place(x = 110,y = 280)

#Defining Button and Placing
calculate_bt = tk.Button(calc,text = 'Calculate',fg = 'Blue',command = get_input,padx = 30,pady = 4)
calculate_bt.place(x = 100,y = 230)

calc.mainloop()
