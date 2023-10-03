from pylibdmtx.pylibdmtx import decode, encode
from PIL import Image
from base64 import b64encode
from uuid import uuid4
import io


def createMatrix():
    randstring = str(uuid4()).encode('utf8')
    matrix = encode(randstring)
    img = Image.frombytes('RGB', (matrix.width, matrix.height), matrix.pixels)
    
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    matrixBytes = buf.getvalue()

    b64encoded = b64encode(matrixBytes)
    return [randstring, b64encoded]

if __name__ == '__main__':
    print(createMatrix())