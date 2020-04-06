{
    'name': 'Hospital Management',
    'version': '12.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Module for managing Hospitals',
    'sequence': '10',
    'license': 'AGPL-3',
    'author': 'Sumesh Majhi',
    'maintainer': 'MajhiRockzZ',
    'website': 'https://www.majhirockzz.me/',
    'depends': [
        'base',
        'mail',
    ],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'patient.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
