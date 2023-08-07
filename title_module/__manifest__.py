# -*- coding: utf-8 -*-
{
    "name": "title_module",
    "summary": """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.odoo.com""",
    "author": "Billy Butcher",
    "website": "zephertech",
    "support": "billybutcher0004@gmail.com",
    "license": "OPL-1",
    "category": "Uncategorized",
    "version": "0.1",
    "depends": ["web"],
    "data": [
        # "security/ir.model.access.csv",
        "views/views.xml",
    ],
    "images": [
        "static/description/icon.png",
    ],
    'assets': {
        'web.assets_backend': [
            'title_module/static/src/MyInheritedView.js',
        ]
    },
}