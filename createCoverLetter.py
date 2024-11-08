from spire.pdf.common import *
from spire.pdf import *
import datetime




# Create an object of the PdfDocument class
doc = PdfDocument()
# Load a PDF file
doc.LoadFromFile("Cover_letter_master.pdf")

# Get the first page
page = doc.Pages[0]

# Iterate through the pages in the document
for i in range(doc.Pages.Count):
    # Get the current page
    page = doc.Pages[i]    
    # Create an object of the PdfTextReplace class and pass the page to the constructor of the class as a parameter
    replacer = PdfTextReplacer(page)

    # Replace the first instance of a specific text with new text
    date = datetime.datetime.now()

    
    
    replacer.ReplaceText("[Date]", date.strftime("%B %d, %Y"))

# Save the resulting file
doc.SaveToFile("Test.pdf")
doc.Close()