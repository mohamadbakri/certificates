from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import datetime


class CertificatesCertificate(models.Model):
    _name = "certificates.certificate"
    _description = "Certificates"
    _rec_name = "customer"

    allow_printing = fields.Boolean(default=True)
    print_log_history_ids = fields.One2many("certificates.log.history", "certificate_id")
    serial_number = fields.Char(readonly=True)
    motor_number = fields.Char()
    chassis_number = fields.Char()
    price = fields.Integer()
    certificate_type = fields.Many2one("certificates.type")
    traffic_department = fields.Many2one("certificates.department")
    brand = fields.Many2one("certificates.brand")
    customer = fields.Char()
    vehicle_type = fields.Selection([
        ("c", "Car"),
        ("b", "Bus"),
        ("mb", "Minibus"),
        ("mb", "Microbus"),
    ])
    car_model = fields.Selection(
        [((str(datetime.today().year - r)), (str(datetime.today().year - r))) for r in range(21)])

    @api.model
    def create(self, vals):
        vals['serial_number'] = self.env['ir.sequence'].next_by_code('certificates.certificate')
        return super(CertificatesCertificate, self).create(vals)
    #
    # def print_report(self):
    #     if self.env.user.has_group("certificates.certificates_supervisors_group"):
    #         self.certificate_print_log()
    #         return self.env.ref("certificates.certificate_report_action").report_action(self)
    #     elif self.env.user.has_group("certificates.certificates_normal_users_group") and \
    #             not self.env.user.has_group("certificates.certificates_supervisors_group") and self.allow_printing:
    #         self.allow_printing = False
    #         self.certificate_print_log()
    #         return self.env.ref("certificates.certificate_report_action").report_action(self)
    #     else:
    #         raise UserError("You've run out of printing!")

    def print_report(self):
        if self.env.user.has_group("certificates.certificates_supervisors_group"):
            self.certificate_print_log()
            return self.env.ref("certificates.certificate_report_action").report_action(self)
        elif self.env.user.has_group("certificates.certificates_normal_users_group") and \
                not self.env.user.has_group("certificates.certificates_supervisors_group") and self.allow_printing:
            self.allow_printing = False
            self.certificate_print_log()
            return self.env.ref("certificates.certificate_report_action").report_action(self)
        else:
            raise UserError("You've run out of printing!")

    def certificate_print_log(self):
        self.env["certificates.log.history"].create({
            "certificate_id": self.id,
        })

    def allow_reprint_report(self):
        self.allow_printing = True


class LogHistory(models.Model):
    _name = "certificates.log.history"
    certificate_id = fields.Many2one("certificates.certificate")

