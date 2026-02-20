from flask import Flask, render_template, redirect
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'syncra_tech_x_secret_key_2026')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSeicA4rJH4WCXQ3GjZKxujku99uv9oa12nWIUMMbtlSzPjcEA/viewform")


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
