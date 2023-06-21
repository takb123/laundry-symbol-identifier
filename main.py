from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')


@app.get("/")
def read_root():
    return {"I Love": "You"}


@app.get("/todo/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: int):
    return templates.TemplateResponse('base.html',
                                      {'request': request, 'id': id})
