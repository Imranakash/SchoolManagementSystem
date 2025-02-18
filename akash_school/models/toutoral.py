from odoo import api, fields, models

class SchoolTutorial(models.Model):
    _name = "school.tutorial"
    _description = "Tutorial Exam"


    name=fields.Char(string="Subjects",required=True)
    sequence = fields.Integer(default=10)
    gpa = fields.Float(string="GPA", default=0.00)



