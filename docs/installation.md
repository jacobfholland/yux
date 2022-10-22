<span style="font-size:3em;">Installation Guide</span>
<br>
This installation guide will help you get up and running with a development environment for Yux

# Install Postgres
_TODO: May end up using SQlite so that users dont need to install a database strucutre and everything can stayed housed in the app_

## **Debian**
### Create the file repository configuration
```
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
```
### Import the repository signing key
```
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
```
### Update the package lists
```
sudo apt-get update
```
### Install the latest version of PostgreSQL
```
sudo apt-get -y install postgresql
```
### Upgrade packages
```
sudo apt update
```
```
sudo apt upgrade
```

# Installing the Environment
_All commands are run at the root folder level of Yux_ 
Creating a virtual environment with `venv` is performed so that any python packages installed are self contained within an environment and won't interefere with the rest of your system. This step is optional, but best practice.

## **Install a Virtual Environment (optional)**
### Create a Virtual Environment
```
python3 -m venv venv
```
### Activating the Virtual Environment
```
source venv/bin/activate
```
## **PIP Install**
### Install required dependencies
```
pip install -r requirements.txt
```

# Initialize the database
## **Migration and Upgrading**
### Migrate
```
flask db migrate
```
### Upgrade
```
flask db upgrade
```

# Running Yux
## **Running the Flask development server**
```
flask --debug run
```