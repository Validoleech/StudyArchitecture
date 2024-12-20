from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routers import score_router, auth_router, composition_router
from dotenv import load_dotenv
from app.proto.grpc_server import serve
import logging

app = FastAPI()

load_dotenv()

Base.metadata.create_all(bind=engine)

# Routers
app.include_router(score_router, prefix="/api", tags=["Score Service"])
app.include_router(auth_router, prefix="/api", tags=["Auth Service"])
app.include_router(composition_router, prefix="/api", tags=["Composition Service"])

if __name__ == "__main__":
    import uvicorn
    import threading

    grpc_thread = threading.Thread(target=serve)
    grpc_thread.start()
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)