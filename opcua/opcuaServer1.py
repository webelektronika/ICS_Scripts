import opcua, random, time

opcServer = opcua.Server()
opcServer.set_server_name("WebElektronika - OPCUA - Szerver")
opcServer.set_endpoint("opc.tcp://192.168.56.111:4840")

opcNamespace = opcServer.register_namespace("http://192.168.56.111:4840")

opcServer.start()

objPLC1 = opcServer.get_objects_node()
PLC1 = objPLC1.add_object(opcNamespace, "PLC_1")

PLC1_sensor1 = PLC1.add_variable(opcNamespace, "Temperature", 40)
PLC1_sensor1.set_writable(writable=True)
PLC1_sensor2 = PLC1.add_variable(opcNamespace, "Humidity", 50)
PLC1_sensor2.set_writable(writable=True)
PLC1_sensor3 = PLC1.add_variable(opcNamespace, "Distance", 15)
PLC1_sensor3.set_writable(writable=False)


while True:
    PLC1_sensor1.set_value(random.randrange(15, 45))
    PLC1_sensor2.set_value(random.randrange(10, 60))
    PLC1_sensor3.set_value(random.randrange(10, 70))
    time.sleep(10)
