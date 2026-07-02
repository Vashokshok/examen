from flask import Flask, render_template
from table.database import session
from table.models import Note, Category


app = Flask(__name__)



@app.route('/')
def main():
    dealers = session.query(Category).all()
    return render_template('index.html',dealers=dealers)


if __name__ == '__main__':
    app.run(debug=True)