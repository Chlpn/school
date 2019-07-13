# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import odoo.addons.decimal_precision as dp
from odoo.exceptions import UserError


class Teachers(models.Model):
    _name = "dept.master"
    _name = "dept.master"
    _description = "Teachers Management"
    _rec_name = 'dept_id'

    dept_id = fields.Char(string='Department ID')
    department_name = fields.Char(string='Department Name')

    @api.multi
    def add_teacher(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Add Teacher',
            'view_mode': 'form',
            'view_type': 'form',
            'res_model': 'add.teacher.wizard',
            'target': 'new',
            'context': 'None'
        }




