# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'School Management System',
    'version' : '17.0.1.5',
    'author':'Akash Software Solution',
    'summary': 'A school management system is a software solution that streamlines administrative tasks',
    'sequence': -100,
    'description': """This is a School Management System """,
    'category': 'School-Management',
    'website': '',
    'depends': [
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/clsSce.xml',
        'views/fee.xml',
        'views/salary.xml',
        'views/readonly.xml',
        'views/tutorial.xml',
        'views/result.xml',
        'views/menu.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install':False,
    'license': 'LGPL-3',
}
