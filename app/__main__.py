import uvicorn
import os

from .app import app

SERVER_PORT = int(os.getenv("SERVER_NAME"))

uvicorn.run(app, host="0.0.0.0", port=SERVER_PORT, log_level="info")
