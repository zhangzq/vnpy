# encoding: UTF-8

from vnpy.trader import vtConstant
from .korbitGateway import korbitGateway

gatewayClass = korbitGateway
gatewayName = 'KORBIT'
gatewayDisplayName = 'KORBIT'
gatewayType = vtConstant.GATEWAYTYPE_BTC
gatewayQryEnabled = True

