from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def show_map():
    return render_template('map.html')


@app.route('/onedot/')
def show_onedot_map():
    return render_template('mapOneDot.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

