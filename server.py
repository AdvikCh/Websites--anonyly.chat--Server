import trio; from trio_websocket import serve_websocket, ConnectionClosed; import os

clients = set(); PORT = int(os.environ.get("PORT", 10000))

async def relay(request):
    web_socket = await request.accept(); clients.add(web_socket)
    try:
        while True:
            data = await web_socket.get_message(); print(data)
            for client in clients: await client.send_message(data)
    except ConnectionClosed: pass
    finally: clients.remove(web_socket)

async def main(): await serve_websocket(relay, '0.0.0.0', PORT, ssl_context=None)

trio.run(main)
