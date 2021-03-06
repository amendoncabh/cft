# coding=utf-8
##############################################################################
#
#    account_auto_fy_sequence module for Odoo
#    Copyright (C) 2014 ACSONE SA/NV (<http://acsone.eu>)
#    @author Stéphane Bidoul <stephane.bidoul@acsone.eu>
#
#    account_auto_fy_sequence is free software:
#    you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License v3 or later
#    as published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    account_auto_fy_sequence is distributed
#    in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License v3 or later for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    v3 or later along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Sale Commission Calc Adjust CFT',
    'version': '8.0.0.1.0',
    'category': 'Sales',
    'author': "Tharathip, Ecosoft",
    'website': 'http://www.ecosoft.co.th',
    'depends': [
        'sales_team',
        'sale_commission_calc',
        'sale_view_adjust_cft',
    ],
    'data': [
        'security/sale_commission_calc_adjust_cft_security.xml',
        'security/ir.model.access.csv',
        'views/res_company_view.xml',
        'views/res_users_view.xml',
        'views/sales_team_view.xml',
        'views/commission_rule_view.xml',
        'views/commission_calc_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'AGPL-3',
}
