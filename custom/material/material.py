from odoo import api, models,fields
from odoo.exceptions import UserError

class Materialproduct(models.Model):
    _name = 'material.product'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Material Product"
    
    name = fields.Char(string= 'Name')
    code = fields.Char(string= 'Material Code')
    material_type = fields.Selection([('fabric', 'Fabric'), ('jeans', 'Jeans'), ('cotton', 'Cotton')], string="Material Type")
    material_buy_price = fields.Float(string="Buy Price")
    suppliyer_id = fields.Many2one(comodel_name="res.partner", string="Suppliyer")
               
    @api.model
    def create(self, vals):
        # if int(vals['material_buy_price']) < 100 :
        #     raise UserError('Price can\'t under 100')
        result = super(Materialproduct, self).create(vals)
        return result