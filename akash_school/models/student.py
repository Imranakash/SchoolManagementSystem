from pkg_resources import require

from odoo import api, fields, models

class SchoolStudent(models.Model):
    _name = "school.student"
    _inherit = ['mail.thread']
    _description="SclM Project"
    # _rec_name = 'name'

    name = fields.Char(string="Name", required=True,tracking=True)
    date_of_birth = fields.Date(string="DOB")
    gender = fields.Selection([('male','Male'),('female','Female')], string="Gender")
    cls =  fields.Selection([('6','Six'),('7','Seven'),('8','Eight'),('9','Nine'),('10','Ten')], string="Class")
    section = fields.Selection([('a','A(Male)'),('b','B(female)')],string="Section")
    cls_schedule = fields.Datetime(string="Class Schedule", tracking=True)
    sub_ids = fields.Many2many('school.tutorial',string='Subject Tag')

