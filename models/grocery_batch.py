from odoo import models, fields

class GroceryBatch(models.Model):
    _name = 'grocery.batch'
    _description = 'Grocery Batch'

    batch_name = fields.Char('Batch Name', required=True)
    expiry_date = fields.Date('Expiry Date')
    batch_quantity = fields.Integer('Batch Quantity')
    grocery_id = fields.Many2one('grocery.details', string='Grocery Item', ondelete='cascade')
