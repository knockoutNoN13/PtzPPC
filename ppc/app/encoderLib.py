from pylibdmtx.pylibdmtx import decode, encode
from PIL import Image
from base64 import b64encode
from uuid import uuid4
import io


def createMatrix():
    randstring = str(uuid4())
    matrix = encode(randstring)
    img = Image.frombytes('RGB', (matrix.width, matrix.height), matrix.pixels)
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    matrixBytes = img_byte_arr.getvalue()
    b64encoded = b64encode(matrixBytes)
    return [randstring, b64encoded]

if __name__ == '__main__':
    print(createMatrix())