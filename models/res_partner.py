from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    related_certificate_id = fields.Many2one("certificates.certificate", string="Customer")