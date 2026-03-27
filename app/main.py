from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from core.database import init_db_pool, close_db_pool, init_sa_engine, close_sa_engine
from core.cache import init_redis_client, close_redis_client
from api.routers import users, posts

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    app.state.db_pool = await init_db_pool()
    app.state.sa_engine = await init_sa_engine()
    app.state.redis_client = await init_redis_client()
    yield
    # Shutdown
    await close_db_pool(app.state.db_pool)
    await close_sa_engine(app.state.sa_engine)
    await close_redis_client(app.state.redis_client)

app = FastAPI(
    title="Trendsee Publications API",
    description="Advanced FastAPI service with DI, Redis cache, Postgres.",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/api/v1")
app.include_router(posts.router, prefix="/api/v1")

@app.get("/")
async def root(request: Request):
    return {
        "message": "Trendsee API v1 ready!",
        "docs": f"{request.url}docs",
        "redoc": f"{request.url}redoc"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=False)
