## Create connection
import pymysql
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy import delete
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine("mysql+pymysql://root:janobourian@localhost:6036/mysqlflask", echo = True, future = True)

Session = sessionmaker(autocommit = False, autoflush = True, bind = engine)

Base = declarative_base()

db = Session()

## Create models

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(30), nullable=False)
    permission_id = Column(Integer, ForeignKey("permission.id"))
    
    ## relationship
    permission = relationship("Permission")    

class Permission(Base):
    __tablename__ = "permission"
    id = Column(Integer, primary_key=True, nullable=False)
    type = Column(String(30), nullable=False)
    
    def __repr__(self):
        return f"id {self.id}, type {self.type}"

## Work with the models

Base.metadata.create_all(engine)

### Insert
value = {
    "type": "anytype"
}

admin = Permission(**value)

with db:
    with db.begin():
        db.add(admin)

### Select

select_stmt = select(Permission).where(Permission.id == 1)

for permission in db.scalars(select_stmt):
    print(permission)


results = db.query(Permission).all()
for result in results:
    print(result)
    
### Update
result = db.query(Permission).filter(Permission.id == 4).first()
print(result)
if result:
    result.type = 'contributor'
    db.commit()

### Delete
result = db.query(Permission).filter(Permission.id == 5).first()
print(result)
if result:
    db.delete(result)
    db.commit()