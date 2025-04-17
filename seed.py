from sqlalchemy.orm import Session
from database import engine
import models as m


m.Base.metadata.drop_all(bind=engine)
m.Base.metadata.create_all(bind=engine)

with Session (bind=engine) as session:
    category1=m.Category(type="Muscle")
    session.add(category1)
    session.add(m.Car(brand="Ford",model="Mustang",yearofproduction=1964,category=category1))
    session.commit()