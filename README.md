# tweety

## Setup
1. Clone the repo - `git clone https://github.com/sunit-poddar/tweety.git`
2. Create `.env` file -  
  2.1 `touch .env`  
2. Initialize Pip shell - `pipenv shell --three`
3. Install requirements - `pipenv install`
4. Create Postgres database ([Reference](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04)) -  
  4.1 Enter into with password - `psql`  
  4.2 `CREATE DATABASE tweety_dev;`  
  4.3 `CREATE USER tweety_dev_app WITH PASSWORD 'root';`  
  4.4 `ALTER ROLE tweety_dev_app SET client_encoding TO 'utf8';`  
  4.5 `ALTER ROLE tweety_dev_app SET default_transaction_isolation TO 'read committed';`  
  4.6 `ALTER ROLE tweety_dev_app SET timezone TO 'UTC';`  
  4.7 `GRANT ALL PRIVILEGES ON DATABASE tweety_dev TO tweety_dev_app;` 
  4.8 Exit - `\q`
  
  
 
 ## Sample .env content
```
SECRET_KEY='<secret_key>'
DATABASE_NAME="tweety_dev"
DATABASE_USER="tweety_dev_app"
DATABASE_PASSWORD="root"
DATABASE_HOST=""
DATABASE_PORT=""
```
  
