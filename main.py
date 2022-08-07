import logging

import uvicorn
from fastapi import FastAPI, Request

from event_handlers import BaseEventHandler
from registry import Registry

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/events")
async def events(request: Request):
    data = await request.json()
    event_type = request.headers['X-GitHub-Event']
    handlers = Registry.get_handlers(event_type)
    if not handlers:
        logging.getLogger().warning('No handlers were defined for event of type {}'.format(event_type))
    for handler in handlers:
        await handler().run(data)


@app.on_event("startup")
async def startup_event():
    for handler_cls in BaseEventHandler.__subclasses__():
        event_type = handler_cls().event_type
        if event_type:
            Registry.register(event_type, handler_cls)


if __name__ == '__main__':
    uvicorn.run('main:app', port=9999, reload=True)
