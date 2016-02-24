# This file is part stock_delivery_date module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['Sale']
__metaclass__ = PoolMeta


class Sale:
    __name__ = 'sale.sale'
    delivery_date = fields.DateTime('Delivery Date',
        states={
            'readonly': ~Eval('state').in_(['draft', 'quotation']),
            },
        depends=['state'])

    def _get_shipment_sale(self, Shipment, key):
        shipment = super(Sale, self)._get_shipment_sale(Shipment, key)
        if Shipment.__name__ == 'stock.shipment.out':
            if self.delivery_date:
                shipment.delivery_date = self.delivery_date
        return shipment
