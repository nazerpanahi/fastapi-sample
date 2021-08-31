import http.cookies

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.router import router as root_router
from config import settings, AppConstants

http.cookies._is_legal_key = lambda _: True
app = FastAPI(
    title=AppConstants.title,
    description=AppConstants.description,
    version=AppConstants.version
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)
app.include_router(router=root_router)

if settings.DEBUG:
    if __name__ == "__main__":
        import uvicorn

        uvicorn.run('app:app', host='0.0.0.0', port=8000, debug=False, reload=False)
