# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def action_cancel(self):
        res = super(StockPicking, self).action_cancel()
        origin_order_lines = self.mapped('move_lines').mapped('sale_line_id')
        origin_order_lines.write({'cancel_motif_id':self.cancel_motif_id.id})
        return res
