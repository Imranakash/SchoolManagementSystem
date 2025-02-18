from django.template.defaultfilters import default
from docutils.nodes import reference
from pkg_resources import require

from odoo import api, fields, models

class SchoolFinance(models.Model):
    _name = "school.finance"
    _inherit = ['mail.thread']
    _description="Financial Management"


    name = fields.Char(string="Transaction Name", required=True, tracking=True)
    transaction_date = fields.Date(string="Transaction Date", required=True)
    transaction_type = fields.Selection([
        ('income', 'Income'),
        ('expense', 'Expense')
    ], string="Transaction Type", required=True)
    amount = fields.Float(string="Amount", required=True)
    payment_method = fields.Selection([
        ('cash', 'Cash'),
        ('bank', 'Bank Transfer'),
        ('cheque', 'Cheque'),
        ('mobile', 'Mobile Payment')
    ], string="Payment Method", required=True)
    student_id = fields.Many2one('school.student', string="Student (If Applicable)")
    category = fields.Selection([
        ('tuition_fee', 'Tuition Fee'),
        ('exam_fee', 'Exam Fee'),
        ('salary', 'Teacher Salary'),
        ('others', 'Others')
    ], string="Category", required=True)
    reference = fields.Char(string="Reference Number" , default='New')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('ongoing','Ongoing'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ], string="Status", default='draft', tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
        print("odoo mates",vals_list)
        for val in vals_list:
            if val['reference']=='New':
                val['reference']=self.env['ir.sequence'].next_by_code('SF001')
        return super().create(vals_list)

    #define fuction for button (fee.xml/form)
    def action_ongoing(self):
        for rec in self:
            rec.state='ongoing'
    def action_confirmed(self):
        for rec in self:
            rec.state='confirmed'
    def action_cancelled(self):
        for rec in self:
            rec.state='cancelled'





