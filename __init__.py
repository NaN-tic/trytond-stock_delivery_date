# This file is part stock_delivery_date module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import sale
from . import shipment


def register():
    Pool.register(
        sale.Sale,
        shipment.ShipmentOut,
        module='stock_delivery_date', type_='model')
