from odoo import models, fields, api


class CertificatesType(models.Model):
    _name = "certificates.type"
    _description = "Certificate Type"
    _rec_name = "certificate_type"

    certificate_type = fields.Char()
    certificate_ids = fields.One2many("certificates.certificate", "certificate_type")
