#!/usr/bin/env python

'''

Asynchronous Modbus Server Built in Python using the pyModbus module

'''

from pymodbus.server.asynchronous import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

import logging

# Create a datastore and populate it with test data

store = ModbusSlaveContext(
	di = ModbusSequentialDataBlock(0, [17]*100), # Discrete Inputs initializer
	co = ModbusSequentialDataBlock(0, [17]*100), # Coils initializer
	hr = ModbusSequentialDataBlock(0, [17]*100), # Holding Register initializer
	ir = ModbusSequentialDataBlock(0, [17]*100)) # Input Registers initializer
context = ModbusServerContext(slaves=store, single=True)

# Populate the Modbus server information fields, these get returned as
# response to identity queries

identity = ModbusDeviceIdentification()
identity.VendorName = 'WebElektronika.'
identity.ProductCode = 'TestCode'
identity.VendorUrl = 'https://github.com/riptideio/pyModbus'
identity.ProductName = 'Modbus Server'
identity.ModelName = 'PyModbus'
identity.MajorMinorRevision = '1.0'
identity.UserApplicationName = 'Modbus Test'

FORMAT = ('%(asctime)-15s %(threadName)-15s' '%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')

#logging.basicConfig(format=FORMAT)
logging.basicConfig(filename='logModbus.txt', encoding='utf-8', level=logging.DEBUG)
log = logging.getLogger()

#log.setLevel(logging.INFO)
# Start the listening server
print ('Starting Modbus server...')
StartTcpServer(context, identity=identity, address=("0.0.0.0", 502))
