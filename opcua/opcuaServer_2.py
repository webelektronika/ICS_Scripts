import opcua, random, time

opcServer = opcua.Server()
opcServer.set_server_name("WebElektronika - OPCUA - Szerver")
opcServer.set_endpoint("opc.tcp://172.24.0.173:4840")

opcNamespace = opcServer.register_namespace("http://172.24.0.173:4840")

opcServer.start()

objPLC1 = opcServer.get_objects_node()
PLC1 = objPLC1.add_object(opcNamespace, "PLC_1")

PLC1_sensor1 = PLC1.add_variable(opcNamespace, "Temperature", 40)
PLC1_sensor1.set_writable(writable=True)
PLC1_sensor2 = PLC1.add_variable(opcNamespace, "Humidity", 50)
PLC1_sensor2.set_writable(writable=True)
PLC1_sensor3 = PLC1.add_variable(opcNamespace, "Distance", 15)
PLC1_sensor3.set_writable(writable=False)
PLC1_sensor4 = PLC1.add_variable(opcNamespace, "Test1", 10)
PLC1_sensor4.set_writable(writable=True)
PLC1_sensor5 = PLC1.add_variable(opcNamespace, "Test2", 20)
PLC1_sensor5.set_writable(writable=True)

while True:
    rand1 = random.randrange(15, 45)
    rand2 = random.randrange(15, 60)
    rand3 = random.randrange(15, 70)
    print(str(rand1) + " - " + str(rand2) + " - " + str(rand3))
    PLC1_sensor1.set_value(rand1)
    PLC1_sensor2.set_value(rand2)
    PLC1_sensor3.set_value(rand3)
    time.sleep(10)
