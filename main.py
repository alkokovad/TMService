from flask import Flask, render_template


app = Flask(__name__)


@app.roote('/main')
def main_page():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')