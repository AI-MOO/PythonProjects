from tkinter import Tk,Radiobutton,Button,Label,StringVar,IntVar,Entry

class TaxCalculator():
    def __init__(self):         
        window = Tk()
        window.title("Tax Calculator")
        window.configure(background = "#231942")
        window.geometry("550x260")
        window.resizable(width = False, height = False)

        self.products_cost = StringVar()
        self.tax_percent = IntVar()
        self.tax = StringVar()
        self.total_cost = StringVar()

        # Taxs percentages label
        tax_percents = Label(window, text = "Tax Percentages", width = 20, bg="#c12a35", fg = "white")
        tax_percents.grid(column = 0, row = 0, padx = 20 , pady = 10)

        # Taxs percentages options start from 5% up to 30% 
        tax_5 = Radiobutton(window, text = "05%", variable = self.tax_percent, value = 5, bg = "#9f86c0")
        tax_5.grid(column = 0, row = 1) 
        tax_10 = Radiobutton(window, text = "10%", variable = self.tax_percent, value = 10, bg = "#9f86c0")
        tax_10.grid(column = 0, row = 2)
        tax_15 = Radiobutton(window, text = "15%", variable = self.tax_percent, value = 15,  bg = "#9f86c0")
        tax_15.grid(column = 0, row = 3)
        tax_20 = Radiobutton(window, text = "20%", variable = self.tax_percent, value = 20 , bg = "#9f86c0")
        tax_20.grid(column = 0, row = 4)
        tax_25 = Radiobutton(window, text = "25%", variable = self.tax_percent, value = 25, bg = "#9f86c0")
        tax_25.grid(column = 0, row = 5)
        tax_30 = Radiobutton(window, text = "30%", variable = self.tax_percent,  value = 30, bg = "#9f86c0" )
        tax_30.grid(column = 0 , row = 6)

        # Bill Amount label & Entry field
        bill_amount = Label(window,text = "Bill Amount", width = 20, bg="#c12a35", fg = "white")
        bill_amount.grid(column = 1, row = 0, padx = 20, pady = 20)
        bill_amount_entry = Entry(window,textvariable = self.products_cost, width = 20)
        bill_amount_entry.grid(column = 2, row = 0, padx = 20, pady = 20)


        # Tax Amount label & Entry field
        Tax_amount_lbl = Label(window, text = "Tax Amount",width = 20, bg = "#c12a35", fg = "white")
        Tax_amount_lbl.grid(column = 1, row = 2)
        Tax_amount_entry = Entry(window,textvariable = self.tax, width = 20)
        Tax_amount_entry.grid(column = 2, row = 2)
        
        
        #Total Cost label & Entry field
        bill_total_lbl = Label(window, text = "Total Cost",width = 20, bg = "#c12a35", fg = "white")
        bill_total_lbl.grid(column = 1, row = 4)
        bill_total_entry = Entry(window,textvariable = self.total_cost, width = 20)
        bill_total_entry.grid(column = 2, row = 4)
        
        # Calculate Button
        calculate_btn = Button(window, text = "Calculate",width = 15, bg = "#660033", fg = "white", command = self.calculate)
        calculate_btn.grid(column = 2 , row = 6)

        # Clear Button       
        clear_btn = Button(window, text = "Clear", width = 20, bg = "#660033", fg = "white", command = self.clear)
        clear_btn.grid(column = 1 , row = 6 )
    

        window.mainloop()

    # Tax Calcultor Function 
    def calculate(self):
        pre_tax = float(self.products_cost.get())
        percentage = self.tax_percent.get() / 100 
        tax_amount_in = pre_tax * percentage
        self.tax.set(tax_amount_in)

        final_bill = pre_tax + tax_amount_in
        self.total_cost.set(final_bill)
    
    # Clear Fields Function 
    def clear(self):
        self.total_cost.set("")
        self.products_cost.set("")
        self.tax.set("")
        

        
TaxCalculator()




         
