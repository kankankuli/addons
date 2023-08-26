# -*- coding: utf-8 -*-
#################################################################################
# Author      : CFIS (<https://www.cfis.store/>)
# Copyright(c): 2017-Present CFIS.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://www.cfis.store/>
#################################################################################

{
    "name": "POS Items Count | Items Count on POS | Item Count POS | POS Item Count",
    "summary": """
        This module allows the POS user to keep track of the number of products added to the POS in each order. The item(s) count is also shown on the POS receipt.
        """,
    "version": "13.0.1",
    "description": """
        This module allows the POS user to keep track of the number of products added to the POS in each order. The item(s) count is also shown on the POS receipt.
        """,    
    "author": "CFIS",
    "maintainer": "CFIS",
    "license" :  "Other proprietary",
    "website": "https://www.cfis.store",
    "images": ["images/items_count_on_pos.png"],
    "category": "Point of Sale",
    "depends": [
        "base",        
        "point_of_sale",
    ],
    "data": [
        "views/assets.xml",
        "views/view_pos_config.xml",
    ],
    "qweb": [
        "static/src/xml/OrderSummary.xml",
    ],
    "installable": True,
    "application": True,
    "price"                 :  7,
    "currency"              :  "EUR",
    "pre_init_hook"         :  "pre_init_check",
}