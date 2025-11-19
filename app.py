from flask import Flask ,render_template ,redirect,url_for ,request
app=Flask(__name__) 
tasks = [
    {"id": 1, "title": "Acheter du pain", "done": False},
    {"id": 2, "title": "Réviser Flask", "done": True},
]
@app.route("/")
def home():
    return render_template("index.html",tasks=tasks)
@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title", "").strip()
    if title == "":
        return redirect(url_for("home"))
    new_id = tasks[-1]["id"] + 1 if tasks else 1
    new_task = {"id": new_id, "title": title, "done": False}
    tasks.append(new_task)
    return redirect(url_for("home"))
@app.route("/delete/<int:task_id>")
def delete(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]

    return redirect(url_for("home"))
@app.route("/done/<int:task_id>")
def done(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True  
            break

    return redirect(url_for("home"))

if __name__=="__main__":
    app.run(debug=True)
