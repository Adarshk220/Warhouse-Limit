from odoo import fields, models


class ProductProduct(models.Model):
    """Model for inheritance in product"""
    _inherit = "product.product"

    warehouse_limit_ids = fields.One2many("product.product.warehouse"
                                          , "warehouse_limit_id", string="warehouses")


class ProductProductWarehouse(models.Model):
    """Model for warehouse limit in product"""
    _name = "product.product.warehouse"
    warehouse_limit_id = fields.Many2one("product.product")
    warehouse_id = fields.Many2one("stock.warehouse", string="Warehouse")
    warehouse_limit = fields.Integer(string="Warehouse Limit")
