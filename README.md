# Organisation Management System

## Working on this project

*READ **CHANGES.md***

### Clone this repo

* Clone this repo
* fetch dev branch

  ```bash
  $ git fetch origin dev
  From github.com:nervelabs-africa/org-management-system
  * branch            dev        -> FETCH_HEAD
  ```

* checkout to dev branch and start coding

  ```bash
  $ git checkout dev
  Branch 'dev' set up to track remote branch 'dev' from 'origin'.
  Switched to a new branch 'dev'
  ```

* update dev branch just to be sure

  ```bash
  $ git pull origin HEAD
  From github.com:nervelabs-africa/org-management-system
  * branch            HEAD       -> FETCH_HEAD
  Already up to date.
  ```

### Run the project setup scripts

from dev branch, run the setup script `setup_proj.py`.

```bash
$ ./scripts/setup_proj.py
install a postgresql db (y/n)?
...
```

N.b: when you run the script, it should ask for the following;

* to install a postgresql db
* virtual environment name to create?
* and if you want to install the requirements.txt automatically.

### Create .env file for local development

> *There are two env files one for your own use, and one for the app's life cycle environments*

1. .env (you shouldn't upload this) it should store
  environment variables specific to local your dev environment
  like your local database username and password.
  The backend also uses this too decide what settings to load
  so you need to make one.

2. .env-* (found in config) settings specific env file
    this file is used to load variables specific to the current
    app life cycle stage e.g dev, staging, or production.
    You should only store variables to be used with or for a specific
    settings file or life cycle stage.

#### add a .env file

> it should look something like this;

```bash
ENV=dev
DB_USER=krumitz
DB_PASSWORD=******* # password not included for security reasons
DB_HOST=localhost
DB_PORT=5432
```

Note as this are mostly user or local machine specific variables, other variables like
database name has been stored in the .env-[life-cycle-stage] file.

## READ DEVNOTES.md

### Add yourname to the contributors lists

And BOOM!!

Aaron Balogun - [Github](https://github.com/krumitzz) / [Twitter](https://twitter.com/krumitzz)

### PLEASE ALWAYS PUSH CHANGES DON'T WAIT!!! PRACTICE CONTINUOS INTEGRATION

#### HAPPY HACKING!! (^-^)
