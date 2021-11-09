import socket
from network_messages import NetworkEnvelope, VersionMessage, SimpleNode

host = 'testnet.programmingbitcoin.com'
port = 18333
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, port))
stream = socket.makefile('rb', None)
version = VersionMessage()
envelope = NetworkEnvelope(version.command, version.serialize())
socket.sendall(envelope.serialize())
while True:
    new_message = NetworkEnvelope.parse(stream)
    print(new_message)



node = SimpleNode('testnet.programmingbitcoin.com', testnet=True)
version = VersionMessage()
node.send(version)
verack_received = False
version_received = False

while not verack_received and not version_received:
    message = node.wait_for(VersionMessage, VerAckMessage)
    if message.command == VerAckMessage.command:
        verack_received = True
    else:
        version_received = True
        node.send(VerAckMessage())
