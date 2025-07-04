# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Grocery Shop',
    'version' : '17.0.0.1',
    'summary': 'Grocery Details',
    'sequence': 1,
    'description': """
Grocery Details
====================
Thjshxghjdghcdbhfjhj jhvjgeuhebehgrn case you work with an (external) account to keep your books, and you still want to keep track of payments. This module also offers you an easy method of registering payments, without having to encode complete abstracts of account.
    """,
    'category': 'Others',
    'website': 'https://www.ocore48.com',
    'depends': [],
    'data': [
            'security/ir.model.access.csv',
            'views/grocery_details_views.xml',
            'data/grocery_sequence.xml',
            'views/grocery_location_views.xml',
            
          ],
   
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
