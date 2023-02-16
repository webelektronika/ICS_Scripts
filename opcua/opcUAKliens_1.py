from opcua import Client

client = Client("opc.tcp://192.168.56.113:4840")
client.connect()

root = client.get_root_node()
print("Objects node is: " + str(root))

objects = client.get_objects_node()
objChild = objects.get_children()[1]
darab = len(objChild.get_children())

for i in range(0, darab):
    state = objChild.get_children()[i]
    print(str(state.get_browse_name()) + " - " + str(state.get_value()))

client.close_session()