# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class PickingType(models.Model):
    _inherit = "stock.picking.type"

    report_display_customer_signature = fields.Boolean(
        string='Report display customer signature', default=False,
        help="If this case is checked,the system will display the customer signature in the bottom of the report.")

