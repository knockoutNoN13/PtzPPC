import asyncio

async def handle_connection(reader, writer):

    addr = writer.get_extra_info("peername")
    print("Connected by", addr)
    try:
        writer.write(b'''
 ______     ______     ______     ______     __    __     ______     ______   ______     __     __  __    
/\  == \   /\  __ \   /\  ___\   /\  ___\   /\ "-./  \   /\  __ \   /\__  _\ /\  == \   /\ \   /\_\_\_\   
\ \  __<   \ \  __ \  \ \___  \  \ \  __\   \ \ \-./\ \  \ \  __ \  \/_/\ \/ \ \  __<   \ \ \  \/_/\_\/_  
 \ \_____\  \ \_\ \_\  \/\_____\  \ \_____\  \ \_\ \ \_\  \ \_\ \_\    \ \_\  \ \_\ \_\  \ \_\   /\_\/\_\ 
  \/_____/   \/_/\/_/   \/_____/   \/_____/   \/_/  \/_/   \/_/\/_/     \/_/   \/_/ /_/   \/_/   \/_/\/_/ 
                                                                                                          
''')
    except ConnectionError:
        print(f"Client suddenly closed while receiving from {addr}")
        pass

    questions = [1, 2, 3]
    answears = [1, 2, 3]
    
    for i in range(3):

        try:
            writer.write( (str(questions[i]) + '\n').encode('UTF-8') )

        except ConnectionError:
            break

        try:
            data = await reader.read(1024)
            data = ''.join(data.decode().split())

        except ConnectionError:
            break

        if not data:
            break

        if data != str(answears[i]):
            print('break on = ')
            break

        if i == 2:
            writer.write(b'flag')

    # while True:
    #     # Receive
    #     try:
    #         data = await reader.read(1024)

    #     except ConnectionError:
    #         print(f"Client suddenly closed while receiving from {addr}")
    #         break

    #     if not data:
    #         break

    #     data = data.upper()

    #     try:
    #         writer.write(data)

    #     except ConnectionError:
    #         print(f"Client suddenly closed, cannot send")
    #         break

    writer.close()
    print("Disconnected by", addr)

async def main(host, port):
    server = await asyncio.start_server(handle_connection, host, port)
    async with server:
        await server.serve_forever()

HOST, PORT = "0.0.0.0", 8080

if __name__ == "__main__":
    asyncio.run(main(HOST, PORT))