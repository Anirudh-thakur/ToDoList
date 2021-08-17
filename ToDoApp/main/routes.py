from flask import Blueprint, render_template, redirect, url_for , request

from ToDoApp.extension import mongo
main = Blueprint('main', __name__)


@main.route('/')
def index():
    todo_collection = mongo.db.todoapp
    todos = todo_collection.find()
    return render_template('index.html', todos = todos)


@main.route('/add_todo' , methods=['POST'])
def add_todo():
    todo_item = request.form.get('new-todo')
    todo_collection = mongo.db.todoapp
    todo_collection.insert_one({'text':todo_item,'complete':False})
    return redirect(url_for('main.index'))

@main.route('/complete_todo/<oid>')
def complete_todo(oid):
   return redirect(url_for('main.index'))

@main.route('/delete_completed')
def delete_completed():
    print("1")
    return redirect(url_for('main.index'))

@main.route('/delete_all')
def delete_all():
    print("2")
    return redirect(url_for('main.index'))
