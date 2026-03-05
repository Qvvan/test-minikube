from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI! TEST new branch", "branch": "main"}

@app.get("/health")
def health():
    return {"status": "ok"}
