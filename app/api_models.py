from flask_restx import fields
from .extensions import api

course_model = api.model("Course",{
    "id": fields.Integer,
    "name": fields.String
})

student_model = api.model("Student",{
    "id": fields.Integer,
    "name": fields.String,
    "course_id": fields.Integer,
    "course": fields.Nested(course_model)
})