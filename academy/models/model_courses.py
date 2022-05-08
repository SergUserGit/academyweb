from odoo import models,fields,api

class Courses(models.Model):
    #_name = 'academy.courses'
    _inherit = 'product.template'
    #taxes_id = fields.Many2many('product.template')

    name = fields.Char()
    teacher_id = fields.Many2one('academy.teachers', string="Teacher")

