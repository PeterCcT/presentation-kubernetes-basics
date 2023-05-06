import uvicorn
from backend_app.app import app

uvicorn.run(app, host='0.0.0.0')