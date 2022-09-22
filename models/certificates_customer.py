from odoo import models, fields, api
import re
from odoo.exceptions import ValidationError


class CertificatesCustomer(models.Model):
    _name = "certificates.customer"
    _description = "Customers"
    _rec_name = "customer_name"

    customer_name = fields.Char()
    customer_phone = fields.Char()

    @api.constrains("customer_phone")
    def _validate_customer_phone(self):
        # pattern = "([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
        pattern = "^01[0125][0-9]{8}$"
        if not re.fullmatch(pattern, self.customer_phone):
            raise ValidationError("Not Valid Phone Number!")

    _sql_constraints = [
        ('unique_email', 'UNIQUE(customer_phone)', 'Phone Number already exists')
    ]
