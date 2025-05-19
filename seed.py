from sqlalchemy.orm import Session
from database import engine
import models as m


m.Base.metadata.drop_all(bind=engine)
m.Base.metadata.create_all(bind=engine)


with Session(bind=engine) as session:

    
    
    category1 = m.Category(type="Muscle")
    category2 = m.Category(type="Wagon")
    category3 = m.Category(type="SUV")
    session.add_all([category1, category2, category3])
    session.commit()  


    mustang = m.Car(
        brand="Ford",
        model="Mustang",
        yearofproduction=1964,
        category=category1,
        mileage=10000,
        dateinsystem="2022-01-01",
        image="https://example.com/image.jpg",
        
    )
    
    audi_s6 = m.Car(
        brand="Audi",
        model="S6 avant",
        yearofproduction=2020,
        category=category2,
        mileage=10000,
        dateinsystem="2022-01-01",
        image="https://example.com/image.jpg",
        
    )
    
    audi_q8 = m.Car(
        brand="Audi",
        model="Q8",
        yearofproduction=2022,
        category=category3,
        mileage=10000,
        dateinsystem="2022-01-01",
        image="https://example.com/image.jpg",
        
    )
    user= m.User(
        username="root",
        password="root"
    )
    
    session.add_all([mustang, audi_s6, audi_q8])
    session.commit()