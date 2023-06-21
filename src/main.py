from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"I Love": "You"}


@app.get("/todo/{todo}")
async def read_item(todo: int):
    return {"Todo": todo}
