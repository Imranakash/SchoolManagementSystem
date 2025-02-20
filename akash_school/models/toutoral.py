from odoo import api, fields, models
from odoo.odoo.tools import file_open


class SchoolTutorial(models.Model):
    _name = "school.tutorial"
    _description = "Tutorial Exam"

    name=fields.Char(string="Subjects",required=True)
    sequence = fields.Integer(default=10)



 #Another model
class SchoolResult(models.Model):
    _name = "school.result"
    _description = "Student Result"

    name=fields.Selection([
        ('tutorial','Tutoiral'),
        ('mid', 'Mid Term'),
        ('final', 'Final')
    ],string="Result",required=True)

    student_id = fields.Many2one('school.student', string="Student (If Applicable)")
    gpa = fields.Float(string="GPA", default=0.00)




