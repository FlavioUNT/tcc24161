from flask import Flask, render_template, redirect, request, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Frase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
    image_url = db.Column(db.String(200))
    comments = db.relationship('Comment', backref='frase', lazy='dynamic', cascade='all, delete-orphan')

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    frase_id = db.Column(db.Integer, db.ForeignKey('frase.id'), nullable=False)

@app.route('/')
def index():
    new_frase = Frase.query.all()
    return render_template('index.html', new_frase=new_frase)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    image_url = request.form.get('image_url')
    new_frase = Frase(title=title, complete=False, image_url=image_url)
    db.session.add(new_frase)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:frase_id>')
def update(frase_id):
    frase = Frase.query.get_or_404(frase_id)
    frase.complete = not frase.complete
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/delete/<int:frase_id>')
def delete(frase_id):
    frase = Frase.query.get_or_404(frase_id)
    db.session.delete(frase)
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/add_comment/<int:frase_id>', methods=['POST'])
def add_comment(frase_id):
    frase = Frase.query.get_or_404(frase_id)
    user_name = request.form.get('user_name')
    content = request.form.get('content')
    new_comment = Comment(user_name=user_name, content=content, frase=frase)
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({
        'success': True, 
        'id': new_comment.id, 
        'user_name': new_comment.user_name,
        'content': new_comment.content, 
        'created_at': new_comment.created_at.strftime('%Y-%m-%d %H:%M:%S')
    })

@app.route('/update_comment/<int:comment_id>', methods=['POST'])
def update_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    comment.content = request.form.get('content')
    db.session.commit()
    return jsonify({'success': True})

@app.route('/delete_comment/<int:comment_id>', methods=['POST'])
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    return jsonify({'success': True})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
