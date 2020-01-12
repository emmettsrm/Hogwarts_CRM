from flask import Flask
from flask_restful import Api, Resource, reqparse
import time
import threading

app = Flask(__name__)
api = Api(app)

@app.route("/")
def index():
    return "Welcome to Hogwarts"

hogwarts_students =[
    {
        "id": 0,
        "first_name": "Harry",
        "last_name": "Potter",
        "creation_time": time.strftime("%H:%M:%S", time.gmtime()),
        "last_update_time": "",
        "magic_skills": {
            "Alchemy": "4",
            "Illusion": "3",
            "Summoning": "3",
            "Invisibilty": "4",
        },
        "desired_skills": {
            "Summoning": "5",
            "Invulnerability": "1",
            "Omnipresent": "1",
            "Invisibility": "5"
        },
        "desired_course": "Alchemy advanced"

    },
    {
        "id": 1,
        "first_name": "Ron",
        "last_name": "Weasley",
        "creation_time": time.strftime("%H:%M:%S", time.gmtime()),
        "last_update_time": "",
        "magic_skills": {
            "Alchemy": "3",
            "Animation": "3",
            "Healing": "3",
            "Invisibility": "2",
        },
        "desired_skills": {
            "Summoning": "1",
            "Invulnerability": "2",
            "Illusion": "1",
            "Invisibility": "3"
        },
        "desired_course": "Dating with Magic"
    }
]

class Student(Resource):
    def get(self, id=0):
        if id == 0:
            return hogwarts_students, 200
        for student in hogwarts_students:
            if(student["id"] == id):
                return student, 200
        return "Student not found.", 404

def post(self, id):
    parser = reqparse.RequestParser()
    parser.add_argument("id")
    parser.add_argument("first_name")
    parser.add_argument("last_name")
    parser.add_argument("creation_time")
    parser.add_argument("last_update_time")
    parser.add_argument("magic_skills")
    parser.add_argument("desired_skills")
    parser.add_argument("desired_course")
    params = parser.parse_args()

    for student in hogwarts_students:
        if(id == student["id"]):
            return f"Student with id {id} already exists.", 400

    student = {
        "id": int(id),
        "first_name": params["first_name"],
        "last_name": params["last_name"],
        "creation_time": params["creation_time"],
        "last_update_time": params["last_update_time"],
        "magic_skills": params["magic_skills"],
        "desired_skills": params["desired_skills"],
        "desired_courses": params["desired_courses"]
    }
    hogwarts_students.append(student)
    return student, 201

def put(self, id):
    parser = reqparse.RequestParser()
    parser.add_argument("id")
    parser.add_argument("first_name")
    parser.add_argument("last_name")
    parser.add_argument("creation_time")
    parser.add_argument("last_update_time")
    parser.add_argument("magic_skills")
    parser.add_argument("desired_skills")
    parser.add_argument("desired_course")
    params = parser.parse_args()

    for student in hogwarts_students:
        if (id == student["id"]):
            student["first_name"]: params["first_name"]
            student["last_name"]: params["last_name"]
            student["creation_time"]: params["creation_time"]
            student["last_update_time"]: params["last_update_time"]
            student["magic_skills"]: params["magic_skills"]
            student["desired_skills"]: params["desired_skills"]
            student["desired_courses"]: params["desired_courses"]
            return student, 200
        student = {
            "id": id,
            "first_name": params["first_name"],
            "last_name": params["last_name"],
            "creation_time": params["creation_time"],
            "last_update_time": params["last_update_time"],
            "magic_skills": params["magic_skills"],
            "desired_skills": params["desired_skills"],
            "desired_courses": params["desired_courses"]
        }

        hogwarts_students.append(student)
        return student, 201
def delete(self, id):
    global hogwarts_students
    hogwarts_students = [student for student in hogwarts_students if student["id"] != id]
    return f"Student with id {id} has been removed."

api.add_resource(Student, "/", "/students/", "/students/<int:id>")

if __name__ == "__main__":
    threading.Thread(target=app.run).start()