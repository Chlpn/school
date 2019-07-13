# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError
import odoo.addons.decimal_precision as dp
from datetime import datetime


class AddTeacher(models.TransientModel):
    _name = "add.teacher.wizard"
    

    rec_id = fields.Char(string='Teacher id')
    rec_name = fields.Char(string='Teacher Name')

    @api.multi
    def add_new(self):
        addmore = self.env['dept.master'].browse(self.env.context.get('active_id'))


        vals = {
                   'teacher_id':self.rec_id,
                    'teacher_name':self.rec_name,
                    'department':addmore.id,

        }
        dept_master = self.env['teachers.master'].create(vals)
        addmore.add_teacher()

