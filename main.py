import os
from flask import Flask, render_template, redirect, request, url_for
from sqlalchemy import String, Integer
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///tasks.db"
db = SQLAlchemy(app)



class Task(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    new_task: Mapped[int] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        add_task = Task(new_task= request.form.get("newtask"))
        db.session.add(add_task)
        db.session.commit()
        return redirect(url_for('index'))
    
    task = db.session.execute(db.select(Task)).scalars().all()
    return render_template("index.html", tasks=task)

@app.route("/delete")
def delete():
    item_id = request.args.get("id")
    delete_task = db.session.execute(db.select(Task).where(Task.id == item_id)).scalar()
    db.session.delete(delete_task)
    db.session.commit()
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)