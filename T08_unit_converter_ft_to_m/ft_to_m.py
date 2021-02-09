#Tk = create the app window, DoubleVar = floating point nums
from tkinter import Tk, Button, Label, DoubleVar, Entry   

window = Tk()
window.title("Feet to Meter Conversion App")
# Background color of the applicaiton
window.configure(background = "light blue")
# Application dimensions size  
window.geometry("680x220")
# prevent the user from changing the size of app window
window.resizable(width = False , height = False)

# convert from feet to meter ! 
def convert_to_m():
    value = float(ft_entry_in.get())
    meter = value * 0.3048
    m_value_out.set("%0.4f" % meter)

# convert from meter to feet ! 
def convert_to_ft():
    value2 = float(m_entry_in.get())
    feet = value2 * 3.2808 
    ft_value_out.set("%0.4f" % feet)


# clear the entry fields 
def clear1():
    ft_value_in.set("")
    m_value_out.set("")
def clear2():
    m_value_in.set("")
    ft_value_out.set("")



# Left-hand Feet text labels 
ft_lbl = Label(window, text = "Feet", bg = "brown", fg = "white", width = 20)
ft_lbl.grid(column = 0, row = 0, padx = 20, pady = 20)
# Left-hand Feet entry field: "we use it in convert_to_m() function as input"
ft_value_in = DoubleVar()  
ft_entry_in = Entry(window,textvariable = ft_value_in, width = 20)                   
ft_entry_in.grid(column = 1, row = 0)
ft_entry_in.delete(0,'end')

# Right-hand Feet text labels 
ft_lbl = Label(window, text = "Feet", bg = "brown", fg = "white", width = 20)
ft_lbl.grid(column = 2, row = 1, padx = 20, pady = 20)
# Right-hand Feet entry field: output field
ft_value_out = DoubleVar()  
ft_entry_out = Entry(window,textvariable = ft_value_out, width = 20)
ft_entry_out.grid(column = 3, row = 1)
ft_entry_out.delete(0,'end')

# Left-hand Meter text label 
m_lbl = Label(window, text = "Meter", bg = "green", fg = "white", width = 20)
m_lbl.grid(column = 0, row = 1, padx = 20, pady = 20)
# Left-hand Meter entry field: output field
m_value_out = DoubleVar()  
m_entry_out = Entry(window,textvariable = m_value_out, width = 20)
m_entry_out.grid(column = 1, row = 1)
m_entry_out.delete(0,'end')

# Right-hand Meter text label 
m_lbl = Label(window, text = "Meter", bg = "green", fg = "white", width = 20)
m_lbl.grid(column = 2, row = 0, padx = 20, pady = 20)
# Right-hand Meter entry field: "we use it in convert_to_ft() function as input"
m_value_in = DoubleVar()  
m_entry_in = Entry(window,textvariable = m_value_in, width = 20)
m_entry_in.grid(column = 3, row = 0)
m_entry_in.delete(0,'end')


# Convert Button for convert_to_m()
convert_btn = Button(window, text = "Convert", bg = "orange", fg = "white", width =15, command = convert_to_m)
convert_btn.grid(column = 1 , row = 3, padx = 15, pady = 15)

# Convert Button for convert_to_ft() 
convert_btn = Button(window, text = "Convert", bg = "orange", fg = "white", width =15, command = convert_to_ft)
convert_btn.grid(column = 3 , row = 3, padx = 15, pady = 15)

# Clear Button 1  
clear_btn = Button(window, text = "Clear" , bg = 'Black', fg = "white", width = 10 , command = clear1)   
clear_btn.grid(column = 0 , row = 3, padx = 15, pady = 15 )

# Clear Button 2  
clear_btn = Button(window, text = "Clear" , bg = 'Black', fg = "white", width = 10 , command = clear2)   
clear_btn.grid(column = 2 , row = 3, padx = 15, pady = 15 )


# Keep the application window running until the user close it
window.mainloop()