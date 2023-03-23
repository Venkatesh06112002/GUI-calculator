import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

    
def evaluate_calculation():
    global calculation
    try:
        calculation=str(eval(calculation))
        
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)

    except:
        clear_field()
        text_result.insert(1.0, "Error")
        

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")
    
    

root=tk.Tk()
root.geometry("300x275")

text_result=tk.Text(root, height=2, width=16, font=("Arial",24))
text_result.grid(columnspan=5)

button1 = tk.Button(root, text="1", command=lambda:add_to_calculation(1), width=5, font = ("Arial", 14))
button1.grid(row=2, column=1)


button2 = tk.Button(root, text="2", command=lambda:add_to_calculation(2), width=5, font = ("Arial", 14))
button2.grid(row=2, column=2)

button3 = tk.Button(root, text="3", command=lambda:add_to_calculation(3), width=5, font = ("Arial", 14))
button3.grid(row=2, column=3)

button4 = tk.Button(root, text="4", command=lambda:add_to_calculation(4), width=5, font = ("Arial", 14))
button4.grid(row=3, column=1)

button5 = tk.Button(root, text="5", command=lambda:add_to_calculation(5), width=5, font = ("Arial", 14))
button5.grid(row=3, column=2)

button6 = tk.Button(root, text="6", command=lambda:add_to_calculation(6), width=5, font = ("Arial", 14))
button6.grid(row=3, column=3)

button7 = tk.Button(root, text="7", command=lambda:add_to_calculation(7), width=5, font = ("Arial", 14))
button7.grid(row=4, column=1)

button8 = tk.Button(root, text="8", command=lambda:add_to_calculation(8), width=5, font = ("Arial", 14))
button8.grid(row=4, column=2)

button9 = tk.Button(root, text="9", command=lambda:add_to_calculation(9), width=5, font = ("Arial", 14))
button9.grid(row=4, column=3)

button0 = tk.Button(root, text="0", command=lambda:add_to_calculation(0), width=5, font = ("Arial", 14))
button0.grid(row=5, column=2)

buttonplus = tk.Button(root, text="+", command=lambda:add_to_calculation("+"), width=5, font = ("Arial", 14))
buttonplus.grid(row=2, column=4)

buttonminus = tk.Button(root, text="-", command=lambda:add_to_calculation("-"), width=5, font = ("Arial", 14))
buttonminus.grid(row=3, column=4)

buttonmul = tk.Button(root, text="*", command=lambda:add_to_calculation("*"), width=5, font = ("Arial", 14))
buttonmul.grid(row=4, column=4)

buttondivide = tk.Button(root, text="/", command=lambda:add_to_calculation("/"), width=5, font = ("Arial", 14))
buttondivide.grid(row=5, column=4)

buttonop = tk.Button(root, text="(", command=lambda:add_to_calculation("("), width=5, font = ("Arial", 14))
buttonop.grid(row=5, column=1)

buttoncp = tk.Button(root, text=")", command=lambda:add_to_calculation(")"), width=5, font = ("Arial", 14))
buttoncp.grid(row=5, column=3)

buttoneq = tk.Button(root, text="=", command=evaluate_calculation, width=11, font = ("Arial", 14))
buttoneq.grid(row=6, column=3,columnspan=2)

buttonclear = tk.Button(root, text="C", command=clear_field, width=11, font = ("Arial", 14))
buttonclear.grid(row=6, column=1,columnspan=2)



root.mainloop()
