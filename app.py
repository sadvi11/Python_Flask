#from flask import Flask
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    
   
    return "<h2>welcome to cloud computing</h2>"

@app.route('/aboutus')
def aboutus():

    return "<h2>welcome to about us project</h2>"


@app.route('/contactus')
def contactus():
 return "<h2>welcome to contact us project</h2>"

#page for addition of 19 and 29

@app.route('/add')
def add():
   a=19
   b=29
   c=a+b
   return str(c)

#create a page that do 89-49
#create a page that do multiply 89 and 49
# create a page division 2000/3

@app.route('/sub')
def sub():
   a=89
   b=49
   c=a-b
   return str(c)

#multiply
@app.route('/mul')
def mul():
   a=89
   b=49
   c=a*b
   return str(c)

#division
@app.route('/div')
def div():
   a=2000
   b=3
   c=a/b
   return str(c)

# write code that connect homepage to display name and email of directors
@app.route('/directors')
def directors():
    name="Mrs Akinfolaju"
    email="peju@yahoo.com"
    return render_template('homepage.html', name=name,email=email)

@app.route("/maths")
def maths ():
    a = 5
    b = 10
    c = a+b
    return render_template("maths.html", maths_result=c)

@app.route("/multiply")
def multiply ():
    a = 14
    b = 15
    c = 20
    d= a*b*c
    return render_template("multiply.html", multiply_result=d)

#create a page for HR that will show name ,email ,phone number.
# create another webpage HR.html and send it to browser

@app.route('/HR')
def HR():
    name="Mrs Akinfolaju"
    email="peju@yahoo.com"
    phone="78907645"
    return render_template('HR.html', name=name,email=email,phone=phone)

#create career page and career on software engineering,developers,sales,product analyst



@app.route('/career')
def career():

  
   title1="software engineer"
   title2="developers"
   title3="sales"
   title4="product analyst"

   return render_template('career.html', title1=title1,title2=title2,title3=title3,title4=title4)











if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)