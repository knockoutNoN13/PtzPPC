import socket
from pylibdmtx.pylibdmtx import decode, encode
from PIL import Image
from base64 import b64decode
import re
import io

sock = socket.socket()
sock.connect(('localhost', 8080))

sock.recv(2048).decode()
i=0
while True:
    try:
        data = sock.recv(2048).decode()

        base64Img = re.findall(r'iV.+', data)[0]

        image_data = b64decode(base64Img)

        image = Image.open(io.BytesIO(image_data))
        answer = decode(image)[0].data
        sock.send(answer)
        
    except Exception as e:
        print(e)
        print(data)
        break
    if 'OnegoCTF' in data:
        print(data)
        break

sock.close()