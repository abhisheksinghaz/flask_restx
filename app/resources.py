from flask_restx import Resource, Namespace
import random
from .models import Course, Student
from app.extensions import db
from app.api_models import course_model, student_model, add_course_model, add_student_model

ns = Namespace("api")

@ns.route("/hello")
class Hello(Resource):
    def get(self):
        i = random.randint(1,100)
        return {"random number": i}

@ns.route("/courses")
class ViewCourses(Resource):
    @ns.marshal_list_with(course_model)
    def get(self):
        return Course.query.all()

    @ns.expect(add_course_model)
    @ns.marshal_with(course_model)
    def post(self):
        # print(ns.payload)
        course = Course(name=ns.payload.get('name'))
        db.session.add(course)
        db.session.commit()
        return course, 201


@ns.route("/students")
class ViewStudents(Resource):
    @ns.marshal_list_with(student_model)
    def get(self):
        return Student.query.all()

    @ns.expect(add_student_model)
    @ns.marshal_with(student_model)
    def post(self):
        student = Student(name=ns.payload.get('name'), course_id=ns.payload.get('course_id'))
        db.session.add(student)
        db.session.commit()
        return student, 201

