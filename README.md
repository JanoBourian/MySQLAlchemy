# MySQLAlchemy
A crash course about sqlalchemy and mysql databases using docker how support tech

List of topics

* [Using Docker Cotainers](#section1)
    * [General context](#section1-1)
* [Using Flask and connecting with our MySQL database](#section2)
    * [Code](#section2-1)
    * [Aditional info](#section2-2)
* [About SQLAlchemy](#section3)
    * [List of commands](#section3-1)
    * [Basic Relationship Patterns](#section3-2)
        * [One to One](#section3-2-1)
        * [Many to Many](#section3-2-2)
        * [Many to One](#section3-2-3)
        * [One to Many](#section3-2-4)
    * [Create Tables in database](#section3-3)
    * [Working with Data](#section3-4)
    * [Data manipulation with the ORM](#section3-5)
* [About MySQL](#section4)
* [About PostgreSQL](#section5)
* [requirements.txt](#section6)
* [First Example](#section7)

This Repo has the most important information about how work with some database and SQLAlchemy (an ORM python interface). In this case We will work with MySQL and PostreSQL.

<div id="section1"> </div>

# Using Docker Containers 

## Download, create and run the MySQL container

The steps are something like:

    * Download the official image
    * Check the image
    * Run the container with the next flags:
        * --name: container name
        * --env/-e:  environment variables (MYSQL_ROOT_PASSWORD)
        * -p: port assignment (<local>:<external>)
        * -v: where the data will be saved
        * --detach/-d: if prefer execute it in background
    * Try the connection and availability

```bash
docker ps -a
docker image
docker pull mysql:latest
docker images
docker run --name mysqlflask -e MYSQL_ROOT_PASSWORD=my-secret-pw -v C:<windows_path>/mysqlflask:/var/lib/mysql -p 6036:3306 -d mysql
docker logs mysqlflask
docker exec -it mysqlflask bash
```

### Auxiliar information
* [Official image](https://hub.docker.com/_/mysql)
* [Tutorial 1](https://hevodata.com/learn/docker-mysql/)


## Download, create and run the PostgreSQL container


<div id="section1-1"> </div>

## General context

If you want more information about Docker please check the info about other courses:

* [Docker Ilixum](https://github.com/JanoBourian/softwareArchitecture/tree/main/dockerIlixum)
* [Docker Beginner](https://github.com/JanoBourian/dockerBeginner)

<div id="section2"> </div>

# Using Flask and SQLAlchemy to connect with our MySQL database

For a better work is necessary follow the official documentation, please check sqlalchemy docs in [SQLAlchemy docs](https://docs.sqlalchemy.org/en/14/) if you have less time please check it [the quickstart guide](https://docs.sqlalchemy.org/en/14/orm/quickstart.html)

The general steps for connect database and SQLAlchemy ORM (And then work with it in Flask) are:

    * Install the dependences: Flask and SQLAlchemy
    * Establishing Connectivity:
        * engine and create_engine.
        * test connection with ORM Session

<div id="section2-1"> </div>

## Code


### Establishing and testing the connection
```python
import pymysql
from sqlalchemy import create_engine
from sqlalchemy import text
engine = create_engine("mysql+pymysql://root:password@localhost:3306/mysqlflask", echo = True, future = True)
with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())
```

### Executing with an ORM Session
```python
from sqlalchemy.orm import Session
from sqlalchemy import text
stmt = text("select 'hello world'")
with Session(engine) as session:
    result = session.execute(stmt)
    print(result.all())
```

<div id="section2-2"> </div>

## Aditional info:

* [Engine Configuration](https://docs.sqlalchemy.org/en/14/core/engines.html)

* [Engine and Connection Use](https://docs.sqlalchemy.org/en/14/core/engines_connections.html)

* [Create Engine parameters](https://docs.sqlalchemy.org/en/14/core/engines.html#sqlalchemy.create_engine)

* [Session object information](https://docs.sqlalchemy.org/en/14/orm/session_basics.html#id1)

* [Session maker object](https://docs.sqlalchemy.org/en/14/orm/session_api.html#sqlalchemy.orm.sessionmaker)

* [Select Object, a powerfull tool](https://docs.sqlalchemy.org/en/14/core/selectable.html#sqlalchemy.sql.expression.select)

* [Working with data](https://docs.sqlalchemy.org/en/14/tutorial/data.html#tutorial-working-with-data)

* [Data manipulation with the ORM](https://docs.sqlalchemy.org/en/14/tutorial/orm_data_manipulation.html#tutorial-orm-data-manipulation)

* [Working with related Objects](https://docs.sqlalchemy.org/en/14/tutorial/orm_related_objects.html)

* [SQL statements](https://docs.sqlalchemy.org/en/14/core/expression_api.html)

* [Relationship configuration](https://docs.sqlalchemy.org/en/14/orm/relationships.html)

* [Important lectures](https://docs.sqlalchemy.org/en/14/tutorial/further_reading.html#tutorial-further-reading)

<div id="section3"> </div>

# About SQLAlchemy


<div id="section3-1"> </div>

## List of commands

Here is the list of each importate 
```python
import pymysql
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import select
from sqlalchemy import insert
from sqlalchemy import update
from sqlalchemy import delete
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
```

--- 
Establishing a connection

```python
engine = create_engine() #create the respectly engine
```

---

Committing changes

Ever you use the *execute()* command you should be kept the changes with *commit()*

```python
with engine.connect() as conn:
    conn.execute("raw query")
    conn.commit()
```

---

Fetching rows

You can consult the info of some differents ways:

- Tupple assigment 
- Integer index
- Atrribute name
- Mapping access (*result.mappings()*)

```python
with engine.connect() as conn:
    result = conn.execute("get info query")
    for row in result:
        print(f"x:{row.x}  y:{row.y}")
```
--- 

Working with an ORM Session

After the *session.execute()* we can use *session.commit()* to save the changes.

```python
from sqlalchemy.orm import Session
from sqlalchemy import text
stmt = text("select 'hello world'")
with Session(engine) as session:
    result = session.execute(stmt)
    print(result.all())
```
---

Opening and closing a Session: In this case the session is closed automatically for the *with* statement.
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
engine = create_engine("Example of connection with pool and dialect")
with Session(engine) as session:
    session.add(some_object)
    session.add(some_other_object)
    session.commit()

```
---

Framing out a begin / commit / rollback block: In case to find an exception. 
```python
with Session(engine) as session:
    session.begin()
    try:
        session.add(some_object)
        session.add(some_other_object)
    except:
        session.rollback()
        raise 
    else:
        session.commit()
```
---

The *begin()* method provides a context manager interface for the same sequence of operations.
```python
with Session(engine) as session:
    with session.begin():
        session.add(some_object)
        session.add(some_other_object)
    # inner context calls session.commit(), if there were no exceptions
# outer context calls session.close()
```
---

Combine context
```python
with Session(engine) as session, session.begin():
    session.add(some_object)
    session.add(some_other_object)
# inner context calls session.commit(), if there were no exceptions
# outer context calls session.close()
```
---

Working with *sessionmaker*
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine()

Session = sessionmaker(engine)

with Session() as session:
    session.add(some_object)
    session.add(some_other_other)
    session.commit()
# closes the session
```
---

The *sessionmaker* object provides an analogue method like *Engine.begin()* You can use it like this:
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine()

Session = sessionmaker(engine)

with Session.begin() as session:
    session.add(some_object)
    session.add(some_other_object)
# commits the transaction, closes the session
```
---

Querying (old style)
```python
results = session.query(User).filter_by(name = "Ed").first()
results = session.query(User.name, User.fullname).all()
```
---

Querying (new style)
```python
from sqlalchemy import select
from sqlalchemy.orm import Session

session = Session(engine, future=True)

statement = select(User).filter_by(name="Ed")
result = session.execute(statement).scalars().all()

statement = select(User, Address).join('addresses').filter_by(name = "Ed")
result = session.execute(statement).all()

statement = select(User.name, User.fullname)
result = session.execute(statement).all()
```
---

Declarative Base (MetaData, Table and Column)

```python
from sqlalchemy.orm import declarative_base
Base = declarative_base()
```

<div id="section3-2"> </div>

## Basic Relationship Patterns

The basic code for this section:
```python
from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
```

<div id="section3-2-1"> </div>

### One to One relationship

```python
class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)

    # one-to-many collection
    children = relationship("Child", back_populates="parent")


class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("parent.id"))

    # many-to-one scalar
    parent = relationship("Parent", back_populates="children")
```

<div id="section3-2-2"> </div>

### Many to Many relationship

```python
association_table = Table(
    "association",
    Base.metadata,
    Column("left_id", ForeignKey("left.id")),
    Column("right_id", ForeignKey("right.id")),
)


class Parent(Base):
    __tablename__ = "left"
    id = Column(Integer, primary_key=True)
    children = relationship("Child", secondary=association_table)


class Child(Base):
    __tablename__ = "right"
    id = Column(Integer, primary_key=True)
```

<div id="section3-2-3"> </div>

### Many to One relationship


```python
class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey("child.id"))
    child = relationship("Child")


class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
```

<div id="section3-2-4"> </div>

### One to Many relationship

```python
class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    children = relationship("Child")


class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("parent.id"))
```

<div id="section3-3"> </div>

# Create Tables in database

If you want to work with database started with the Database creation you can try with *sqlalchemy-utils* with its module *database_exists* and *create_database*. Form more information please visit the next [link](https://stackoverflow.com/questions/6506578/how-to-create-a-new-database-using-sqlalchemy)

<div id="section3-4"> </div>

# Working with Data

<div id="section3-5"> </div>

# Data manipulation with the ORM

## Inserting rows with Core

### INSERT

```python
from sqlalchemy import insert
stmt = insert(user_table).values(name="", fullname="")
print(stmt)
compiled = stmt.compile()
compiled.params
with engine.connect() as conn:
    result = conn.execute(stmt)
    conn.commit()
```

### INSERT + RETURNING
```python
from sqlalchemy import insert
insert_stmt = insert(address_table).returning(address_table.c.id, address_table.c.email_address)
print(insert_stmt)
```

## Selecting rows with Core or ORM

### SELECT with where clause
```python
from sqlalchemy import select
select_stmt = select(user_table).where(user_table.c.name == '')
print(select_stmt)
with engine.connect() as conn:
    for row in conn.execute(select_stmt):
        print(row)
```

### Complex queries

For complex queries will be necessary check the official docs. 

## Updating and deleting Rows with Core

### update()
```python
from sqlalchemy import update
update_stmt = update(user_table).where(user_table.c.name == '').values(fullname == '')
print(update_stmt)
```

### delete()
```python
from sqlalchemy import delete
delete_stmt = delete(user_table).where(user_table.c.name == '')
print(delete_stmt)
```

<div id="section4"> </div>

# About MySQL 

If you want more information about this topic can read my repositories.

* [SQL info](https://github.com/JanoBourian/dbSQL)

<div id="section5"> </div>

# About PostgreSQL

<div id="section6"> </div>

# Requirements.txt
* black
* SQLAlchemy
* PyMySQL

<div id="section7"> </div>

# First example

## Part I The Database connection
```python
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.ext.declarative import declarative_base
from .config import init_connection_engine

engine = init_connection_engine()

Session = sessionmaker(autocommit = False, autoflush = True, bind = engine)

Base = declarative_base()

db = Session()
```
---

## Part II The configuration
```python
from config.env_reader import env
from typing import Dict 
import sqlalchemy

def init_connection_engine():
    db_config = {
        "pool_size": 5,
        "max_overflow": 2,
        "pool_timeout": 30,
        "pool_recycle": 1800
    }
    
    if env("ENVIRONMENT") not in ["dev", "qas", "int", "prd"]:
        return init_local_connection(db_config)
    else:
        return init_cloud_connection(db_config)

def init_local_connection(db_config:Dict[str, int]):
    
    ## Local vars
    drivername = "mysql+pymysql"
    db_user = env("EXPEDIENTE_DB_USER")
    db_pass = env("EXPEDIENTE_DB_PASSWORD")
    db_name = env("EXPEDIENTE_DB_NAME")
    db_host = env("EXPEDIENTE_INSTANCE_HOST")
    db_port = env("EXPEDIENTE_DB_PORT")
    
    pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL.create(
            drivername = drivername,
            username = db_user,
            password = db_pass,
            host = db_host,
            port = db_port,
            database = db_name
        ),
        **db_config
    )
    
    return pool

def init_cloud_connection(db_config:Dict[str, int]):
    
    ## Cloud vars
    drivername = "mysql+pymysql"
    db_user = env("EXPEDIENTE_DB_USER")
    db_pass = env("EXPEDIENTE_DB_PASSWORD")
    db_name = env("EXPEDIENTE_DB_NAME")
    instance_connection_name = env("EXPEDIENTE_INSTANCE_CONNECTION_NAME")
    
    pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL.create(
            drivername = drivername,
            username = db_user,
            password = db_pass,
            database = db_name,
            query = {
                "unix_socket": f"/cloudsql/{instance_connection_name}"
            }
        ),
        **db_config
    )
    
    return pool
```
---

## Part III The models
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class PerfilDocumento(Base):
    __tablename__ = 'perfil_documento'
    id_perfil_documento = Column(Integer, primary_key=True, index=True)
    clave_documento = Column(String, ForeignKey('documento.clave_documento'))
    clave_permiso = Column(String, ForeignKey('permiso.clave_permiso'))
    id_estado = Column(Integer, ForeignKey('estados.id_estado'))
    id_perfil = Column(Integer, ForeignKey('perfil.id_perfil'))
    
    # relationships
    clave_documento_detail = relationship("Documento", foreign_keys=[clave_documento])
    clave_permiso_detail = relationship("Permiso", foreign_keys=[clave_permiso])
    id_estado_detail = relationship("Estado", foreign_keys=[id_estado])
    id_perfil_detail = relationship("Perfil", foreign_keys=[id_perfil])

class Permiso(Base):
    __tablename__ = 'permiso'
    clave_permiso = Column(String, primary_key=True, index=True)
    nombre_permiso = Column(String, unique=True, nullable=False)
    
class Estado(Base):
    __tablename__ = 'estados'
    id_estado = Column(Integer, primary_key=True, index=True)
    nombre_estado = Column(String, unique=True, nullable=False)
    
class Perfil(Base):
    __tablename__ = 'perfil'
    id_perfil = Column(Integer, primary_key=True, index=True)
    nombre_perfil = Column(String, unique=True, nullable=False)
    
class Documento(Base):
    __tablename__ = 'documento'
    clave_documento = Column(String, primary_key=True, index=True)
    nombre_documento = Column(String, unique=True, nullable=False)
    id_doc_factory = Column(Integer)
    id_nivel = Column(Integer, ForeignKey('niveles.id_nivel'))
    
    # relationships
    id_nivel_detail = relationship("Niveles", foreign_keys=[id_nivel])
    

class Niveles(Base):
    __tablename__ = 'niveles'
    id_nivel = Column(Integer, primary_key=True, index=True)
    nombre_nivel = Column(String, unique=True, nullable=False)
```