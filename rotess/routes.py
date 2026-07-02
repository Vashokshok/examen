from flask import Blueprint, request, redirect, url_for, render_template
from table.models import Category, Note
from table.database import session

categor_bp = Blueprint('category', __name__, template_folder='templates')


@categor_bp.route('/')
def index():
    categories = Category.query.all()
    return render_template('index.html', categories=categories)

@categor_bp.route('/add_note', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        cont = Note(title=title, content=content)
        session.add(cont)
        session.commit()
        return redirect(url_for('main'))
    return render_template('index.html')


@categor_bp.route('/note/<int:note_id>/delete', methods=['POST'])
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    session.delete(note)
    session.commit()
    return redirect(url_for('category.index'))