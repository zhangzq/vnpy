# encoding: UTF-8

from vnpy.trader import vtConstant
from .zbGateway import zbGateway

gatewayClass = zbGateway
gatewayName = 'ZB'
gatewayDisplayName = 'ZB'
gatewayType = vtConstant.GATEWAYTYPE_BTC
gatewayQryEnabled = True

