# -*- coding: utf-8 -*-
from odoo import http

class CenitWireless(http.Controller):

    @http.route(['/cenit_wireless/manage_order/'], auth='none', type='http', csrf=False)
    def manage_order(self, **kw):
        print(http.request)
        return "Hello, world"


    @http.route('/cenit_wireless/manage_orderline/', auth='public')
    def manage_orderline(self, **kw):
        print(http.request)
        return "Hello, world"