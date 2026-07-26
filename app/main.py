import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def test():
    return {"ok": 200}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=False)
