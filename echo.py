"""Importaciones de FastAPI"""
from fastapi import FastAPI, WebSocket

app = FastAPI()

#Con el decorador se define que se trata de un websocket, seguido de una funcion async
@app.websocket("/ws/echo")
async def websocket_echo(websocket: WebSocket):
    """Funcion que maneja los websockets"""
    # se establece handshake
    await websocket.accept()

    #indefinir el ciclo para mantener abierto el websocket
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Echo: {data}")