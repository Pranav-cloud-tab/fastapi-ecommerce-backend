from fastapi import FastAPI
from app.database.connection import Base, engine
from app.routes import user, product  # ✅ add `product`

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(product.router)  # ✅ register product routes

@app.get("/")
def read_root():
    return {"message": "E-commerce Backend Running 🚀"}