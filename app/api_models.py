from flask_restx import fields
from .extensions import api



student_model = api.model("Student",{
    "id": fields.Integer,
    "name": fields.String,
    "course_id": fields.Integer,
    # "course": fields.Nested(course_model)
})

course_model = api.model("Course",{
    "id": fields.Integer,
    "name": fields.String,
    # "enrolled_students": fields.Nested(student_model)
})

add_course_model  = api.model("AddCourse",{
    "name": fields.String
})

add_student_model = api.model("AddStudent",{
    "name": fields.String,
    "course_id": fields.Integer
})