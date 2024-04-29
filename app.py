# invoice 
# shop name
# invoice header
# date and time
# invoice number
# item list - name, quantity, price
# total amount
# sign
import random

shop_name = str(input("Enter the shop name: "))
# invoice_number = int(input("Enter the invoice number: "))
invoice_number = random.randint(1000, 9999)
# date = input("Enter the date: ")
# time = input("Enter the time: ")
item1_name = str(input("Enter the item1 name: "))
item1_price = float(input("Enter the item1 price: ")) 
item2_name = str(input("Enter the item2 name: "))
item2_price = float(input("Enter the item2 price: "))
item3_name = str(input("Enter the item3 name: "))
item3_price= float(input("Enter the item3 price: "))
# total_amount = float(input("Enter the total amount: "))

print("Invoice")
print("Shop Name: ", shop_name)
print("Invoice Number: ", invoice_number)
# print("Date: ", date)
# print("Time: ", time)
print("Item1 Name: ", item1_name)
print("Item1 Price: ", item1_price)
print("Item2 Name: ", item2_name)
print("Item2 Price: ", item2_price)
print("Item3 Name: ", item3_name)
print("Item3 Price: ", item3_price)
total_amount = item1_price + item2_price + item3_price
print("Total Amount: ", total_amount) 
# for opting out the element from the item list


# creating pdf

from fpdf import FPDF

class InvoicePdf(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(80)
        self.cell(30, 10, 'Invoice', 0, 0, 'C')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def invoice_info(self, shop_name, invoice_number, date, time):
        self.set_font('Arial', '', 12)
        self.cell(0, 10, 'Shop Name: ', 0, 0)
        self.cell(50, 10, shop_name, 0, 1)
        self.cell(0, 10, 'Invoice Number: ', 0, 0)
        self.cell(50, 10, str(invoice_number), 0, 1)
        self.cell(0, 10, 'Date: ', 0, 0)
        self.cell(50, 10, date, 0, 1)
        self.cell(0, 10, 'Time: ', 0, 0)
        self.cell(50, 10, time, 0, 1)
        self.ln(10)

    def item_list(self, item1_name, item1_price, item2_name, item2_price, item3_name, item3_price):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Item List: ', 0, 1)
        self.set_font('Arial', '', 12)
        self.cell(15, 10, 'Name', 1, 0)
        self.cell(25, 10, 'Price', 1, 0, 'R')
        self.ln()
        self.cell(15, 10, item1_name, 1, 0)
        self.cell(25, 10, str(item1_price), 1, 0, 'R')
        self.ln()
        self.cell(15, 10, item2_name, 1, 0)
        self.cell(25, 10, str(item2_price), 1, 0, 'R')
        self.ln()
        self.cell(15, 10, item3_name, 1, 0)
        self.cell(25, 10, str(item3_price), 1, 0, 'R')
        self.ln(10)

    def total_amount(self, total_amount):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Total Amount: ', 0, 0)
        self.cell(50, 10, str(total_amount), 0, 1, 'R')
        self.ln(20)

    def sign(self):
        self.set_font('Arial', '', 12)
        self.cell(0, 10, 'Signature: ______________________________', 0, 1)

pdf = InvoicePdf()
pdf.add_page()
pdf.header()
date = "27 Apr"
time = "10:30"
pdf.invoice_info(shop_name, invoice_number, date, time)
pdf.item_list(item1_name, item1_price, item2_name, item2_price, item3_name, item3_price)
pdf.total_amount(total_amount)
pdf.sign()
pdf.output('Invoice.pdf', 'F')