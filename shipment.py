# This file is part stock_delivery_date module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['ShipmentOut']


class ShipmentOut(metaclass=PoolMeta):
    __name__ = 'stock.shipment.out'
    delivery_date = fields.DateTime('Delivery Date',
        states={
            'readonly': Eval('state') != 'draft',
            },
        depends=['state'])
