# from crypt import methods
# import mimetypes
# from asyncore import file_dispatcher
# from statistics import mode
from flask import Flask, render_template, redirect, request
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def my_portfolio():
    return render_template("index.html")

########################################
# more dyanamic way to target all pages 
########################################

@app.route('/<string:page_name>')
def htmlpages(page_name):
    return render_template(page_name)

# ------------------------------------------

########################################
# manual targeting of the pages 
########################################

# @app.route('/index.html')
# def home():
#     return render_template("index.html")

# @app.route('/works.html')
# def works():
#     return render_template("works.html")

# @app.route('/about.html')
# def about():
#     return render_template("about.html")

# @app.route('/contact.html')
# def contact():
#     return render_template("contact.html")

# @app.route('/components.html')
# def components():
#     return render_template("components.html")

# # running html file   
# @app.route('/about')
# def about():
#     return render_template("index.html")

# --------------------------------------------------

##########################################
# Submit button action in form 
##########################################

@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
    if request.method=="POST":
        try:
            data=request.form.to_dict()   #to_dict will save the form data to a variable named data in memory which may lost if server restarted
            write_to_csv(data) #calling the below function here to write these data | here we can call the function to atrget .txt or .csv
            return redirect("/thankyou.html") # redirecting to thankyou page post submit
        except:
            return "Data did not save to Database"
    else:
        return "Oops! Something went wrong. Try again..."
    
# -------------------------------------------------

# $$$$$$$$$$$ Data Storing in .txt file $$$$$$$$$$$$
##############################################
# Saving the form data in database.txt file which was saved above in memory in variable data
##############################################

def write_to_file(data):
    with open("database.txt",mode="a") as database:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        file=database.write(f"\n{email},{subject},{message}")

# ----------------------------------------------
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ________________________________________________________

# $$$$$$$$$$$$ Data storing in csv file $$$$$$$$$$$$$
def write_to_csv(data):
    with open("database.csv",mode="a") as database2:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_writer=csv.writer(database2, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

