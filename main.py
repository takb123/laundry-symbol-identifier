from fastapi import FastAPI, Request, UploadFile
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
# TODO: Sketch up a basic home page desgin
# TODO: Add File Uploading support for /image
# TODO: Add validation needed for iamge
# TODO: Get Dockerfile Ready for deployment

# INFO: Pipeline should be: Post Reqeust -> /image -> AI -> Response
# INFO: Info should be implemented as business logic?

# INFO: Takuto
# TODO: Get AI Integrated into backend
# TODO: Handle Business logic for processing Images


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.post("/image")
def submit_image(file: UploadFile | None = None):
    if not file:
        return "what"
    else:
        return "submitted file"


@app.get("/todo/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: int):
    return templates.TemplateResponse('base.html',
                                      {'request': request, 'id': id})
