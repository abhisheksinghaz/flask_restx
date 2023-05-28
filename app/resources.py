from flask_restx import Resource, Namespace
import random
from .models import Course, Student
from app.api_models import course_model, student_model

ns = Namespace("api")

@ns.route("/hello")
class Hello(Resource):
    def get(self):
        i = random.randint(1,100)
        return {"random number": i}

@ns.route("/view-courses")
class ViewCourses(Resource):
    @ns.marshal_list_with(course_model)
    def get(self):
        return Course.query.all()

@ns.route("/view-students")
class ViewStudents(Resource):
    @ns.marshal_list_with(student_model)
    def get(self):
        return Student.query.all()

