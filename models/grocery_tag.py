from odoo import models, fields

class GroceryTag(models.Model):
    _name = 'grocery.tag'
    _description = 'Grocery Tag'

    name = fields.Char(string='Tag Name', required=True)
    color = fields.Integer(string='Color')

    