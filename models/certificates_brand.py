from odoo import models, fields


class CertificatesBrand(models.Model):
    _name = "certificates.brand"
    _description = "Certificates Brand"
    _rec_name = "vehicle_brand"

    vehicle_brand = fields.Char()
    brand_ids = fields.One2many("certificates.certificate", "brand")
