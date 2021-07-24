from fastapi import FastAPI
import uvicorn


def app():
    app = FastAPI()

    register_router(app)

    return app

def register_router(app):
    import router

    app.include_router(
        router.router,
        prefix='/app'
    )



if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8080, reload=True, debug=True)