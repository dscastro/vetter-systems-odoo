# -*- coding: utf-8 -*-

from odoo import models, fields, api


class dsc_brandmodule(models.Model):
    _name = 'dsc_brandmodule.dsc_brandmodule'
    _description = 'dsc_brandmodule.dsc_brandmodule'

    name = fields.Char()    
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    start_datetime = fields.Datetime('Start time', default=lambda self: fields.Datetime.now())
    end_datetime = fields.Datetime('End time', default=lambda self: fields.Datetime.now())
    
    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
