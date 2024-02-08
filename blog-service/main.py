from fastapi import FastAPI, Depends
from blog.database import engine, SessionLocal
from blog import schemas, models
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def index():
    return {"data": "Home Page of Blog Site"}


@app.post('/blog')
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blogs')
def blogs(db: Session = Depends(get_db)):
    all_blogs = db.query(models.Blog).all()
    return all_blogs