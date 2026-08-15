from typing import Dict
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

class ConnectionManager:
    """Clase para administrar conexiones """
    def __init__(self):
        self.activate_connection: Dict[WebSocket, str] = {}


    async def connect(self, websocket: WebSocket, username: str):
        """Metodo para conexion"""
        await websocket.accept()
        self.activate_connection[websocket] = username
        await self.broadcast(f"🔵 {username} conectado")


    async def disconnect(self, websocket: WebSocket):
        """Metodo para desconexion"""
        username = self.activate_connection.get(websocket, "Usuario")
        self.activate_connection.pop(websocket, None)
        await self.broadcast(f"🔴 {username} desconectado")


    async def broadcast(self, message: str):
        """Metodo que envia mensajes a todos"""
        for connection in list(self.activate_connection.keys()):
            await connection.send_text(message)


manager = ConnectionManager()

@app.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket, username: str):
    """Maneja la conexion individual en un usuario"""
    await manager.connect(websocket, username)

    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"{username}: {data}")
    except WebSocketDisconnect:
        await manager.disconnect(websocket)