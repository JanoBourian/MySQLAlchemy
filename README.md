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
* [About MySQL](#section4)
* [About PostgreSQL](#section5)
* [requirements.txt](#section6)

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

For a better work is necessary follow the official documentation, please check sqlalchemy docs in [SQLAlchemy docs](https://docs.sqlalchemy.org/en/14/)

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

* [Working with data]

* [Data manipulation with the ORM]

* [Working with related Objects]

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
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
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

```python
engine = create_engine #create the respectly engine
```


<div id="section4"> </div>

# About MySQL 

If you want more information about this topic can read my repositories.

* [SQL info](https://github.com/JanoBourian/dbSQL)

<div id="section5"> </div>

# About PostgreSQL

<div id="section6"> </div>

# Requirements.txt
* SQLAlchemy
* PyMySQL