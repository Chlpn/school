{
    'name': 'School Management',
    'version': '1.0',
    'category': 'Accounting',
    'sequence': 14,
    'author': "Neenu Robin",
    'website': 'www',
    'summary': '',
    'depends': ['account', 'account_accountant','account_cancel','web_readonly_bypass','base_multi_company'],
    'data': [
                'views/teachers.xml',
                'views/department.xml',
'views/all_wizard_view.xml',
                            ],
    'demo': [

            ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
