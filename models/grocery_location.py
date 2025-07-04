from odoo import models, fields

class GroceryItem(models.Model):
    _name = "grocery.location"
    _description = 'Storage Location'

    name = fields.Char(string='Location Name', required=True)
    temperature = fields.Char(string='Temperature Range')
    notes = fields.Text(string='Additional Notes')