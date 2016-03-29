# This file is part stock_delivery_date module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta
from trytond.pyson import Eval

__all__ = ['Sale']


class Sale:
    __metaclass__ = PoolMeta
    __name__ = 'sale.sale'
    delivery_date = fields.DateTime('Delivery Date',
        states={
            'readonly': ~Eval('state').in_(['draft', 'quotation']),
            },
        depends=['state'])

    def create_shipment(self, shipment_type):
        pool = Pool()
        shipments = super(Sale, self).create_shipment(shipment_type)
        if shipment_type != 'out' or not shipments:
            return

        ShipmentOut = pool.get('stock.shipment.out')

        if self.delivery_date:
            ShipmentOut.write(shipments, {
                'delivery_date': self.delivery_date,
                })
        return shipments
