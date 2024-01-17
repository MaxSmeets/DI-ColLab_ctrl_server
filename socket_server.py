import asyncio
import websockets

# List of clients
connected_clients = {}


async def handle_client(websocket, path):
    connected_clients.update
    print(f"Nieuwe verbinding: {websocket.remote_address}")
    try:
        # Wait for client message
        async for message in websocket:
            print(f"Ontvangen van {websocket.remote_address}: {message}")
            splitted = message.split(",")
            if splitted[0] == "N":
                connected_clients.update(
                    {splitted[1]: [websocket, splitted[2], splitted[3]]}
                )
                # Send message back to all clients
                for key, value in connected_clients.items():
                    for key2, value2 in connected_clients.items():
                        await value[0].send(f"N,{key2},{value2[1]},{value2[2]}")
            elif splitted[0] == "P":
                connected_clients.update(
                    {splitted[1]: [websocket, splitted[2], splitted[3]]}
                )
                # Send message back to all clients
                for key, value in connected_clients.items():
                    for key2, value2 in connected_clients.items():
                        await value[0].send(f"P,{key2},{value2[1]},{value2[2]}")

    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        for key, value in connected_clients.items():
            if value[0] == websocket:
                connected_clients.pop(key)

        print(f"Verbinding gesloten: {websocket.remote_address}")


# Start WebSocket-server
start_server = websockets.serve(handle_client, "192.168.43.164", 6969)

print("WebSocket-server gestart op ws://192.168.43.164:6969")

# Start event loop
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
