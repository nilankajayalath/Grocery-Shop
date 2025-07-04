from odoo import models, fields, api
from odoo.exceptions import ValidationError

class GroceryDetails(models.Model):
    _name = "grocery.details"
    _description = "Grocery Item Details"

    _order = 'name desc'

    name = fields.Char('Item Name', required=True, translate=True)
    
    category = fields.Selection([
        ('vegetable', 'Vegetable'),
        ('fruit', 'Fruit'),
        ('dairy', 'Dairy'),
        ('meat', 'Meat'),
        ('beverage', 'Beverage'),
        ('snack', 'Snack'),
        ('other', 'Other'),
    ], string='Category', required=True, default='vegetable')

    
    price = fields.Float('Unit Price', required=True)
    discount = fields.Float('Discount (%)', default=0.0)
    final_price = fields.Float('Final Price', compute='_compute_final_price', store=True)
    
    quantity = fields.Integer('Available Quantity', required=True)
    in_stock = fields.Boolean(string='In Stock', default=True)
    expiry_date = fields.Date(string="Expiry Date")

    notes = fields.Text(string="Notes")
    location_id = fields.Many2one('grocery.location', string='Location')
    tag_ids = fields.Many2many('grocery.tag',string='tags')
    batch_ids = fields.One2many('grocery.batch','grocery_id',  string='Batches')
    availability = fields.Text('Availability')
    sold = fields.Boolean('sold', default=False,Readonly=True)
    location_temp = fields.Char(related='location_id.temperature', string='Location Temp')
    


        # ✅ Custom state field for status bar
    state = fields.Selection([
        ('new', 'New'),
        ('category', 'Category'),
        ('location', 'Location'),
        ('sold', 'Sold'),
    ], string='Status', default='new', tracking=True)
    

      # Sequence field
    sequence = fields.Char(string='Grocery Sequence', required=True, copy=False, readonly=True, default='New')



    def create(self, vals):
        if vals.get('sequence', 'New') == 'New':
            vals['sequence'] = self.env['ir.sequence'].next_by_code('grocery.details') or 'New'
        return super(GroceryDetails, self).create(vals)

   

    @api.depends('price', 'discount')
    def _compute_final_price(self):
        for record in self:
            record.final_price = record.price * (1 - (record.discount / 100))


    @api.onchange('in_stock')
    def _onchange_in_stock(self):
        if self.in_stock:
            self.availability = "This item is currently in stock."
        else:
            self.availability = "This item is currently out of stock."

    def action_mark_as_sold(self):
        self.sold = True
        self.state = 'sold'

    def action_mark_as_category(self):
        self.state= 'category'

    def action_mark_as_location(self):
        self.state = 'location'    

    @api.constrains('price')
    def check_price(self):
        for record in self:
            if record.price <= 0:
                raise ValidationError("Price cannot be negative!")

    

   
    def _compute_batch_ids(self):
        for rec in self:
            rec.batch_count = len(rec.batch_ids)

    def action_batch_ids(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Batches',
            'res_model': 'grocery.batch',
            'view_mode': 'tree,form',
            'domain': [('grocery_id', '=', self.id)],
            'context': {'default_grocery_id': self.id},
            'target': 'current',
        }
