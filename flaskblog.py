from flask import Flask

app = Flask(__name__) # __name__ is the module's name


@app.route("/") # the root page
@app.route("/home")
def home():
    return "<h1>Home page</h1>"

@app.route("/about") 
def about():
    return "<h1>About Page2</h1>"


if __name__ == '__main__':
    app.run(debug=True)