from flask import Flask, render_template
app = Flask(__name__,
            template_folder="templates",
            static_folder="static")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/schedule')
def schedule():
    return render_template("schedule.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)
