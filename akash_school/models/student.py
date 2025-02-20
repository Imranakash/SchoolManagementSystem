from email.policy import default

from pkg_resources import require

from odoo import api, fields, models

class SchoolStudent(models.Model):
    _name = "school.student"
    _inherit = ['mail.thread']
    _description="SclM Project"
    _rec_names_search=['reg','name']
    _rec_name = 'name'

    name = fields.Char(string="Name", required=True,tracking=True)
    reg = fields.Char(string='Registration No')
    date_of_birth = fields.Date(string="DOB")
    gender = fields.Selection([('male','Male'),('female','Female')], string="Gender")
    cls =  fields.Selection([('6','Six'),('7','Seven'),('8','Eight'),('9','Nine'),('10','Ten')], string="Class")
    section = fields.Selection([('a','A(Male)'),('b','B(female)')],string="Section")
    cls_schedule = fields.Datetime(string="Class Schedule", tracking=True)
    sub_ids = fields.Many2many('school.tutorial',string='Subject Tag')
    phn = fields.Char(string='Contact:',default='+880')
    address = fields.Char(string='Address:')


    def _compute_display_name(self):
        for rec in self:
            rec.display_name=f"[{rec.reg}] {rec.name}"

    # def name_get(self):
    #     """ Show registration number in dropdown search and selection fields. """
    #     result = []
    #     for record in self:
    #         name = f"[{record.reg}] {record.name}" if record.reg else record.name
    #         result.append((record.id, name))
    #     return result
    #
    # def _compute_display_name(self):
    #     """ Show only student name in tree and form views. """
    #     for rec in self:
    #         rec.display_name = rec.name  # No registration number in tree view.

