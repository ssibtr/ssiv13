# -*- coding: utf-8 -*-
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd.
# - © Technaureus Info Solutions Pvt. Ltd 2019. All rights reserved.

from odoo import models, fields, api, _


class ProductTemplateCWUOM(models.Model):
    _inherit = 'product.template'

    def _default_cw_uom(self):
        return self.env["uom.uom"].search([], limit=1, order='id').id

    cw_uom_id = fields.Many2one('uom.uom', string="Catch Weight UOM",
                                default=_default_cw_uom)
    sale_price_base = fields.Selection([('uom', 'UOM'), ('cwuom', 'CW-UOM')], string="Sale Price Base")
    purchase_price_base = fields.Selection([('uom', 'UOM'), ('cwuom', 'CW-UOM')], string="Purchase Price Base")
