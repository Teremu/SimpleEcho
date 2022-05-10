

from aiohttp import web
import socketio


sio = socketio.AsyncServer(cors_allowed_origins='*')
app = web.Application()
sio.attach(app)


@sio.event
async def connect(sid, environ):
    print('connect ', sid)
    # print(environ)

@sio.event
async def disconnect(sid):
    print('disconnect ', sid)

@sio.event
async def whoIam(sid, *data):
    print(sid, ":", data)

@sio.event
async def Ping(sid, *data):
    await sio.emit("Pong", data="Zipizapi", to=sid)

web.run_app(app, port=int(os.environ.get('PORT', 8000)))

input("DEBUG")
