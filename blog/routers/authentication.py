from fastapi import APIRouter,Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, database, models, token
from sqlalchemy.orm import Session
from ..hashing import Hash
router = APIRouter(prefix='/login', tags=['Authentication'])

@router.post('/')
def user_login(req: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == req.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User email incorrect")
    
    if not Hash.verify(user.password,req.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Password invalid")
        
    access_token = token.create_access_token(data={"sub":user.email})
    return {"access_token":access_token,"token_type":"bearer"}