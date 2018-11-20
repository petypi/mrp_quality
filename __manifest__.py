# -*- encoding: utf-8 -*-
#

{
    'name': 'MRP features for Quality Control',
    'version': '1.0',
    'author': 'peter mudoko',
    'category': 'Manufacturing',
    'sequence': 50,
    'summary': 'Quality Management with MRP',
    'depends': ['quality', 'mrp_workorder'],
    'description': """
    Adds workcenters to Quality Control
""",
    "data": [
        'data/quality_data.xml',
        'security/quality_mrp.xml',
        'views/quality_views.xml',
        'views/mrp_production_views.xml',
        'views/mrp_workorder_views.xml',
        'views/mrp_workcenter_views.xml',
    ],
    'qweb': ['static/src/xml/widget_template.xml'],
    "demo": ['data/quality_mrp_demo.xml'],
    'auto_install': True,

}
