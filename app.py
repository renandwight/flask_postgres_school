from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask("app")
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql+psycopg://rdwight:<password>@localhost/school"
)

db = SQLAlchemy(app)

class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50))

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer, db.ForeignKey('subjects.id'))

class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer, db.ForeignKey('subjects.id'))

def students_serializer(stud: Students) -> dict:
    return {
        "id": stud.id,
        "full_name": f"{stud.first_name} {stud.last_name}",
        "age": stud.age,
        "subject": stud.subject
    }

@app.route("/students", methods=["GET"])
def get_students():
    cohort = Students.query.all()

    return jsonify(
        [students_serializer(stud) for stud in cohort]
    )


def teachers_serializer(teach: Teachers) -> dict:
    return {
        "id": teach.id,
        "full_name": f"{teach.first_name} {teach.last_name}",
        "age": teach.age,
        "subject": teach.subject
    }

@app.route("/teachers", methods=["GET"])
def get_teachers():
    faculty = Teachers.query.all()

    return jsonify(
        [teachers_serializer(teach) for teach in faculty]
    )


def subject_serializer(sub: Subjects) -> dict:
    return {
        "id": sub.id,
        "subject": sub.subject
    }

@app.route("/subjects", methods=["GET"])
def get_subjects():
    classes = Subjects.query.all()

    return jsonify(
        [subject_serializer(sub) for sub in classes]
    )


app.run(debug=True, port=8000)