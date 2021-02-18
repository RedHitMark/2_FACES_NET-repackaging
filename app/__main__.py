import uvicorn
import os

from .app import app

# SERVER_PORT = os.getenv("SERVER_NAME")
SERVER_PORT = 5000


uvicorn.run(app, host="0.0.0.0", port=SERVER_PORT, log_level="info")
