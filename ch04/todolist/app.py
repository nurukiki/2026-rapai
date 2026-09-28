from flask import Flask, request, render_template, redirect
from model.todo_db import TodoDB

app = Flask(__name__)
todo_db = TodoDB()

@app.route("/")
def home():
    tasks = todo_db.get()
    print(tasks)
    return render_template("task.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form["title"]
    todo_db.add(task)

    return redirect("/")

@app.route("/delete/<int:todo_index>", methods=["DELETE"])
def delete(todo_index):
    todo_db.delete(todo_index)
    return "", 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)

