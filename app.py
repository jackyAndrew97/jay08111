from flask import Flask, render_template


app = Flask(__name__)


@app.route('/Info')
def main():
    return render_template("InfoIndex.html")


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)