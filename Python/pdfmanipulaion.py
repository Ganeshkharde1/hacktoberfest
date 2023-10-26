from reportlab.lib.pagesizes import LETTER  
from reportlab.lib.units import inch  
from reportlab.pdfgen.canvas import Canvas  
from reportlab.lib.colors import purple  
# creating the pdf file  
my_canvas = Canvas("textfile.pdf", pagesize = LETTER)  
# setting up the font and the font size  
my_canvas.setFont("Courier", 18)  
# setting up the color of the font as red  
my_canvas.setFillColor(purple)  
# writing this text on the PDF file   
my_canvas.drawString(2 * inch, 8 * inch, "Welcome to Javatpoint for Python Tutorial")  
my_canvas.save()  
