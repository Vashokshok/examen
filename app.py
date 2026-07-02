from flask import Flask, render_template
from table.database import session
from table.models import Category
from rotess.routes import categor_bp


app = Flask(__name__)

app.register_blueprint(categor_bp, url_prefix='/category')

@app.route('/')
def main():
    categor = session.query(Category).all()
    return render_template('index.html', categor=categor)

if __name__ == '__main__':
    app.run(debug=True)