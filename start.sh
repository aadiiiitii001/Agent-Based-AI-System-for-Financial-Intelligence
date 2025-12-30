# Use Render-provided PORT environment variable, fallback to 10000
PORT=${PORT:-10000}

uvicorn api.main:app --host 0.0.0.0 --port $PORT
