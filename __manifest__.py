{
    "name": "Certificates App",
    'depends': ['crm'],
    "data": [
        "security/certificates_security.xml",
        "security/ir.model.access.csv",
        "views/certificates_certificate_views.xml",
        "views/certificates_type_views.xml",
        "views/certificates_department_views.xml",
        "views/certificates_customer_views.xml",
        "views/certificates_brand_views.xml",
        'views/res_partner_views.xml',
        "data/sequence_data.xml",
        'reports/certificate_report.xml',
        'reports/certificate_template.xml'
    ]
}
