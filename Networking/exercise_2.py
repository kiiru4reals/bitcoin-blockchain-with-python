from network_messages import NetworkEnvelope

from io import BytesIO
message_hex = 'f9beb4d976657261636b000000000000000000005df6e0e2'
stream = BytesIO(bytes.fromhex(message_hex))
envelope = NetworkEnvelope.parse(stream)
print(envelope.command)

print(envelope.payload)