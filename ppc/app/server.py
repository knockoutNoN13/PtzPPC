import asyncio
from encoderLib import createMatrix

async def handle_connection(reader, writer):

    addr = writer.get_extra_info("peername")
    print("Connected by", addr)
    try:
        writer.write(b'''
    ____                                       
   / __ )  ____ _   _____  ___                 
  / __  | / __ `/  / ___/ / _ \                
 / /_/ / / /_/ /  (__  ) /  __/                
/_____/  \__,_/  /____/  \___/                 
                                               
    __  ___           __             _         
   /  |/  /  ____ _  / /_   _____   (_)   _  __
  / /|_/ /  / __ `/ / __/  / ___/  / /   | |/_/
 / /  / /  / /_/ / / /_   / /     / /   _>  <  
/_/  /_/   \__,_/  \__/  /_/     /_/   /_/|_|  
                                                                                                                             
''')
    except ConnectionError:
        print(f"Client suddenly closed while receiving from {addr}")
        pass

    
    for i in range(1,201):
        round = createMatrix()
        answer = round[0]
        question = round[1]

        try:
            writer.write(b'Round ' + str(i).encode() + b'/200\t' + question + b'\n')

        except ConnectionError:
            break

        try:
            data = await reader.read(1024)
            if not data:
                break
            data = ''.join(data.decode().split())      

        except ConnectionError:
            break

        if i == 200:
            writer.write(b'OnegoCTF{ju$t_bas3_0v3r_d@ta_ma7rix}')
            break

        if not data:
            writer.write(b'Oooops... no answer!')
            break

        if data != answer.decode():
            writer.write(b'Oooops... you had mistake!')
            break

    
    writer.close()
    await writer.wait_closed()
    
    print("Disconnected by", addr)

async def main(host, port):
    server = await asyncio.start_server(handle_connection, host, port)
    async with server:
        await server.serve_forever()

HOST, PORT = "0.0.0.0", 8080

if __name__ == "__main__":
    asyncio.run(main(HOST, PORT))