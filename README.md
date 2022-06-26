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
        * test connection

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

* [Create Engine parameters](https://docs.sqlalchemy.org/en/14/core/engines.html#sqlalchemy.create_engine)

* [Session object information](https://docs.sqlalchemy.org/en/14/orm/session_basics.html#id1)

<div id="section3"> </div>

# About SQLAlchemy


<div id="section3-1"> </div>

## List of commands

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

```python
engine = create_engine #create the respectly engine
```

```python
engine = create_engine #create the respectly engine
```

```python
engine = create_engine #create the respectly engine
```

```python
engine = create_engine #create the respectly engine
```

```python
engine = create_engine #create the respectly engine
```

```python
engine = create_engine #create the respectly engine
```

```python
engine = create_engine #create the respectly engine
```

```python
engine = create_engine #create the respectly engine
```

```python
engine = create_engine #create the respectly engine
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