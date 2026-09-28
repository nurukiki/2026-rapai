from flask import Flask, render_template, request, redirect
from model.todo_db import TodoDB

app = Flask(__name__)
todo_db=TodoDB()

@app.route("/")
def index():
    values = todo_db.get()
    return render_template("task.html",tasks=values)

@app.route("/add",methods=['POST'])
def add_task():
    title = request.form['title']
    todo_db.add(title)
    return redirect("/")

@app.route("/delete/<int:todo_index>", methods = ["DELETE"])
def delete_task(todo_index):
    todo_db.remove(todo_index)
    return "",200

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001)
