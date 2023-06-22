from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')


# INFO: Jason
# PASSED: Assign index route to a template
# PASSED: Integrate HTMX for templating concerns?
# PASSED: Get Tailwind added to template
# PASSED: Get Makefile added to simplify process
# BUG: Safari seems to use old version of the Tailwind Template


# INFO: Takuto
# TODO: Get AI Integrated into backend


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.get("/test", response_class=HTMLResponse)
async def read_test_html(request: Request):
    return """
    <html>
        <body>
            <h1> Hello from the server </h1>
        </body>
    </html>
    """


@app.get("/todo/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: int):
    return templates.TemplateResponse('base.html',
                                      {'request': request, 'id': id})
