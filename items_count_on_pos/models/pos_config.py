from odoo import models, fields, api, _

class pos_config(models.Model):
    _inherit = 'pos.config'

    is_total_items = fields.Boolean(string="Enable Total Items",default=False)
    is_total_qty = fields.Boolean(string="Enable Total Quantity",default=False)
    is_total_items_on_print = fields.Boolean(string="Display Total Items on Receipt",default=False)
    is_total_qty_on_print = fields.Boolean(string="Display Total Quantity on Receipt",default=False)