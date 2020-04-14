from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    ergebnis = None
    if request.method == 'POST' and 'ergebnis' in request.form:
        ergebnis = request.form['ergebnis']
    return render_template('index.html', ergebnis=ergebnis)


if __name__ == '__main__':
    app.run(debug=True)