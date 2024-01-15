import asyncio
import websockets

#List of clients
connected_clients = set()

async def handle_client(websocket, path):
    connected_clients.add(websocket)
    print(f"Nieuwe verbinding: {websocket.remote_address}")

    try:
        # Wait for client message
        async for message in websocket:
            print(f"Ontvangen van {websocket.remote_address}: {message}")

            # Send message back to all clients
            for client in connected_clients:
                await client.send(f"{websocket.remote_address}: {message}")

    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)
        print(f"Verbinding gesloten: {websocket.remote_address}")

# Start WebSocket-server
start_server = websockets.serve(handle_client, "127.0.0.1", 6969)

print("WebSocket-server gestart op ws://127.0.0.1:6969")

# Start event loop
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
