from fastapi import Body, FastAPI, Depends
from sqlalchemy.orm import Session
from model import ReviewTable, UserTable, StoreTable
from db import session
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn

gain = FastAPI()

gain.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False, 
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

#회원 정보 등록
@gain.post("/gain/")
async def create_member(user_id: str = Body(...), password: str = Body(...), username: str = Body(...), db: Session = Depends(get_db)):
    new_member = UserTable()
    new_member.user_id = user_id
    new_member.password = password
    new_member.username = username
    db.add(new_member)
    db.commit()
    return "회원 등록 완료"

if __name__ == "__gain__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port)