from odoo import models, fields, api


class CertificatesDepartment(models.Model):
    _name = "certificates.department"
    _description = "Certificate Department"
    _rec_name = "traffic_department"

    traffic_department = fields.Char()
    department_ids = fields.One2many("certificates.certificate", "traffic_department")
