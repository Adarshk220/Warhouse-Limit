from odoo import models
from odoo.exceptions import ValidationError


class StockPicking(models.Model):
    """Model for inheritance in stock moves"""
    _inherit = "stock.picking"

    def button_validate(self):
        res = super().button_validate()
        for line in self.move_ids:
            limit = line.product_id.warehouse_limit_ids.filtered(
                lambda r: r.warehouse_id.id == self.picking_type_id.warehouse_id.id).warehouse_limit
            if line.product_uom_qty > limit and line.product_id.detailed_type == 'product':
                raise ValidationError("Warehouse limit exceeds")
        return res
