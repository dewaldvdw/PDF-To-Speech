import PyPDF2
import pyttsx3
import os

# Ask user for file to be converted
path_valid = False
while path_valid == False:
    try:
        path = input(r"What is the path and filename?")
        pdf_file = open(path, 'rb')
        path_valid = True
    except:
        print("Invalid filename or path. Please try again. ")


# filename to save will have .mp3 extension
filename = (path.split("\\")[-1]).replace("pdf", "mp3")

print(path)

# Ask user for reading speed
speed = input("What should the reading speed be? (150 default): ")
if speed == '':
    speed = 150
print(f"speed: {speed}")

# Ask user for voice gender and save input to variable
gender = input("Male or Female voice? (M / F): ")
if gender.startswith("M".lower()):
    gender = 0
    print("Gender is Male")
else:
    gender = 1
    print("Gender is Female")

# pdf_file = open(path, 'rb')

# Initialize the PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Extract text from all the pages
text = ''
for page in pdf_reader.pages:
    text += page.extract_text()

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', int(speed))
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[gender].id)


# Convert text to audio
rate = engine.getProperty('rate')  # getting details of current speaking rate
engine.save_to_file(text, filename)
engine.runAndWait()

print("The output is saved to: " + os.path.dirname(os.path.realpath(__file__)) + "\\" + filename)

# Close PDF file
pdf_file.close()

# C:\Users\PEDION\Downloads\MWS397W.pdf