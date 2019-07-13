# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import odoo.addons.decimal_precision as dp
from odoo.exceptions import UserError

class Teachers(models.Model):
    _name = "teachers.master"
    _description = "Teachers Management"
    _rec_name = 'teacher_id'


    teacher_id = fields.Char(string='Teacher ID')
    teacher_name = fields.Char(string='Teacher Name')
    department = fields.Many2one('dept.master', ondelete='restrict')



