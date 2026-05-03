"""
Project: Simple Blog Application
Name: KUMAR SUBODH
Date: 03-04-2026
Description: A basic CRUD blog using Flask (no database)
"""
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
# Temporary storage (in-memory)
posts = []
@app.route('/')
def index():
    return render_template('index.html', posts=posts)
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = {
            'id': len(posts),
            'title': title,
            'content': content
        }
        posts.append(post)
        return redirect(url_for('index'))
    return render_template('create.html')
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    post = posts[id]
    if request.method == 'POST':
        post['title'] = request.form['title']
        post['content'] = request.form['content']
        return redirect(url_for('index'))
    return render_template('edit.html', post=post)
@app.route('/delete/<int:id>')
def delete(id):
    posts.pop(id)
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)
