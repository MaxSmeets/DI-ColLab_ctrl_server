import asyncio
import websockets

# List of clients
connected_clients = {}


def update_client(websocket, vals):
    connected_clients.update(
        {websocket: [vals["uuid"], vals["pos_x"], vals["pos_y"], vals["speaking"]]}
    )


async def handle_client(websocket):
    print(f"New connection: {websocket.remote_address}")
    try:
        # Wait for client message
        async for message in websocket:
            print(f"Received from {websocket.remote_address}: {message}")
            splitted = message.split(",")
            action = splitted[0]
            vals = {
                "uuid": splitted[1],
                "pos_x": splitted[2],
                "pos_y": splitted[3],
                "speaking": splitted[4]
            }
            update_client(websocket, vals)
            if action == "N":
                for key, value in connected_clients.items():
                    await websocket.send(f"N,{value[0]},{value[1]},{value[2]},{value[3]}")
                    await key.send(f"N,{vals["uuid"]},{vals["pos_x"]},{vals["pos_y"]},{vals["speaking"]}")
            elif action == "P":
                for key, value in connected_clients.items():
                    await key.send(f"P,{vals["uuid"]},{vals["pos_x"]},{vals["pos_y"]},{vals["speaking"]}")
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        for key, value in dict(connected_clients).items():
            if key == websocket:
                disconnected_uuid = value[0]
                connected_clients.pop(key)
                for key2, value2 in connected_clients.items():
                    await key2.send(f"C,{disconnected_uuid},0,0,0")

        print(f"Connection closed: {websocket.remote_address}")


# Start WebSocket-server
start_server = websockets.serve(handle_client, "127.0.0.1", 6969)

print("WebSocket-server gestart op ws://192.168.43.164:6969")

# Start event loop
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
