from pyModbusTCP.client import ModbusClient
import random
import time

try:
    c = ModbusClient(host="192.168.56.113", auto_open=True, auto_close=False)
    c.port = 502
    c.debug = False
    wV = 0

    while True:
        rV0 = random.randint(0, 500)
        rV1 = random.randint(0, 500)
        rV2 = random.randint(0, 500)
        rV3 = random.randint(0, 500)
        rV4 = random.randint(0, 500)

        randDelay = random.randint(0,10)

        c.read_holding_registers(0, 5)
        c.write_single_register(0, rV0)
        c.write_single_register(1, rV1)
        c.write_single_register(2, rV2)
        c.write_single_register(3, rV3)
        c.write_single_register(4, rV4)

        time.sleep(randDelay)
        wV += 1
        print("Number of cycles: " + str(wV) + ", " + str(rV0) + " - " + str(rV1) + " - " + str(rV2) + " - " + str(rV3) + " - " + str(rV4))

except ValueError:
    print("Error.... ")
