from fastapi import FastAPI

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "nord"})

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

