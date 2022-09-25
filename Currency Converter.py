from locale import currency
import tkinter as tk

def convert(): #conversion function for US dollars
    jmd = int(curjmd.get()) #collects the value entered in the empty textbox and uses it in this function
    usd = jmd / 155 #jmd to usd formula
    t1.config(state='normal')
    t1.delete('1.0', tk.END)
    t1.insert(tk.END,usd) #prints the answer and places it in this empty textbox
    t1.config(state='disabled') #prevents user from altering the answer placed in textbox

def convert2(): #conversion function for JM dollars
    usd = int(curusd.get()) #collects the value entered in the empty textbox and uses it in this function
    jmd = usd * 155 #usd to jmd formula
    t2.config(state='normal')
    t2.delete('1.0', tk.END)
    t2.insert(tk.END,jmd) #prints the answer and places it in this empty textbox
    t2.config(state='disabled') #prevents user from altering the answer placed in textbox

def exit():
    currency.destroy() #exits the program


currency = tk.Tk()
currency.geometry("900x600")
currency.config(bg="#FFDEAD")
currency.resizable(width=False,height=False)
currency.title('Currency Converter')

bigheader = tk.Label(currency,text="Currency Converter",font=("Arial", 15),fg="black",bg="#FFDEAD") #label 1

#labels for JMD to USD conversion
l1 = tk.Label(currency,text="JMD to USD Currency Converter",font=("Arial", 11),fg="black",bg="#FFDEAD") #label 1
l2= tk.Label(currency,text="Enter currency in JMD: ",font=("Arial", 10,"bold"),fg="black",bg="#FFDEAD")#label 2
l3= tk.Label(currency,text="Dollars in USD is $ : ",font=("Arial", 10,"bold"),fg="black",bg="#FFDEAD")#label 3

#labels for USD to JMD conversion
l1_1 = tk.Label(currency,text="USD to JMD Currency Converter",font=("Arial", 11),fg="black",bg="#FFDEAD") #label 1
l2_2 = tk.Label(currency,text="Enter currency in USD: ",font=("Arial", 10,"bold"),fg="black",bg="#FFDEAD")#label 2
l3_3= tk.Label(currency,text="Dollars in JMD is $ : ",font=("Arial", 10,"bold"),fg="black",bg="#FFDEAD")#label 3


emptybig = tk.Label(currency,bg="#FFDEAD") 

#empty labels/spaces for JMD to USD conversion
empty_l1 = tk.Label(currency,bg="#FFDEAD") 
empty_l2 = tk.Label(currency,bg="#FFDEAD")
empty_l4 = tk.Label(currency,bg="#FFDEAD")
empty_l5 = tk.Label(currency,bg="#FFDEAD")
#creates an empty space between elments. not necessary but makes the gui looker neater

#empty labels/spaces for USD to JMD conversion
empty_l1a = tk.Label(currency,bg="#FFDEAD") 
empty_l2b = tk.Label(currency,bg="#FFDEAD")
empty_l4c = tk.Label(currency,bg="#FFDEAD")
empty_l5d = tk.Label(currency,bg="#FFDEAD")
empty_l6e = tk.Label(currency,bg="#FFDEAD")



curjmd = tk.Entry(currency, font=('Arial', 10)) #collects the jmd entered into window
curusd = tk.Entry(currency, font=('Arial', 10)) #collects the usd entered into window


btn1 = tk.Button(currency,text="Convert to USD",font=("Arial", 10),command=convert) #button connected to the convert function
btn1_usd = tk.Button(currency,text="Convert to USD",font=("Arial", 10),command=convert2) #button connected to the convert2 function
btn2 = tk.Button(currency,text="Exit application",font=("Arial", 10),command=exit) #button connected to the exit function, exits program when clicked


t1=tk.Text(currency,state="disabled",width=15,height=0) #textbox to output usd after conversion
t2=tk.Text(currency,state="disabled",width=15,height=0) #textbox to output jmd after conversion


#jmd to usd converter packing
bigheader.pack()
emptybig.pack()
l1.pack()
empty_l1.pack()
l2.pack()
curjmd.pack()
empty_l2.pack()
l3.pack()
t1.pack()
empty_l5.pack()
btn1.pack()
empty_l4.pack()
empty_l1a.pack()
#ends

#usd to jmd converter packing
l1_1.pack()
empty_l2b.pack()
l2_2.pack()
curusd.pack()
empty_l4c.pack()
l3_3.pack()
t2.pack()
empty_l5d.pack()
btn1_usd.pack()
empty_l6e.pack()
btn2.pack()
#ends

currency.mainloop()