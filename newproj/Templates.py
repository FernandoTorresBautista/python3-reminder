from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello():
    str = """
    <html>
    <body>
    <h1>Hello</h1>
    </body>
    </html>
    """
    return str


@app.route('/template')
def index():
    # use template from templates/
    return render_template("hello.html")


@app.route('/sayHello')
def say_hello():
    # use static file from static/
    return render_template("usestatic.html")


# use static file from static/ and use for in table
@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("table.html", result=result)
    else:
        return "No hay form en GET"


if __name__ == '__main__':
    # app.run()
    app.run(debug=True)
