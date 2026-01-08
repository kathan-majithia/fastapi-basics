from fastapi import APIRouter,Depends, HTTPException, status
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..hashing import Hash

router = APIRouter(prefix='/login', tags=['Authentication'])

@router.post('/')
def user_login(req: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == req.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User email incorrect")
    
    if not Hash.verify(user.password,req.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Password invalid")
        
    return user