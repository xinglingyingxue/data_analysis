from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('bar.html')

@app.route('/pie')
def pie():
    return render_template('pie.html')

@app.route('/funnel')
def funnel():
    return render_template('funnel.html')

@app.route('/guangdong')
def guangdong():
    return render_template('map_guangdong.html')

if __name__ == '__main__':
    app.run()
