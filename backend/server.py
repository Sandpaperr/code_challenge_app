# File that runs the application

from src.app import app


if __name__ == "__main__":
    import uvicorn

    # run on localhost on port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)
