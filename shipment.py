# This file is part stock_delivery_date module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta

__all__ = ['ShipmentOut']
__metaclass__ = PoolMeta


class ShipmentOut:
    __name__ = 'stock.shipment.out'
    delivery_date = fields.Function(fields.Date('Delivery Date',
        help='Delivery date calculated from origin'),
        'get_delivery_date')

    def get_delivery_date(self, name=None):
        if hasattr(self.origin, 'delivery_date'):
            return self.origin.delivery_date
