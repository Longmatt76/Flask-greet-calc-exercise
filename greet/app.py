from flask import Flask

app = Flask(__name__)

"""this function displays the homepage which contains links to the other pages"""
@app.route('/')
def home_page():
        html = """
    <html> 
     <body>
       <h1>Homepage!</h1>
         <p> This is the homepage welcome to my simple app</p>
         <a href='/welcome'>Go to welcome page</a> <br>
         <a href= '/welcome/home'>Go to welcome home page</a><br>
         <a href= '/welcome/back'>Go to welcome back page</a>
     </body> 
     </html>
    """
        return html

"""this displays the welcome page"""
@app.route('/welcome')
def say_welcome():
    return "<h1>Welcome!</h1>"


"""this displays the welcome home page"""
@app.route('/welcome/home')
def say_welcome_home():
    return "<h1>Welcome home!</h1>"


"""this displays the welcome back page"""
@app.route('/welcome/back')
def say_welcome_back():
    return "<h1>Welcome back!</h1>"

