from odoo import models,fields,api

class Teachers(models.Model):

    _name = 'academy.teachers'

    name = fields.Char()
    biography = fields.Html(string="Biography")

    course_ids = fields.One2many('product.template','teacher_id',string="Courses")

