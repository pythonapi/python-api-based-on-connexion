# Python API - Based on Connexion
**Table of content**
- [Installation](#installation)
  - [Initial requirements](#initial-requirements)
  - [Set up a Virtual Environment](#set-up-a-virtual-environment)
    - [Ubuntu 16.08](#ubuntu-16.08)      
    - [Windows](#windows)
  - [Install the required packages](#install-the-required-packages)  
- [How to work with Connexion](#how-to-work-with-connexion)
- [To do](#to-do)
- [Contributing](#contributing)
- [License](#license)

# Installation
## Initial requirements
You will need the following services on your machine before you continue:
* MySQL
* git
* python
* pip

## Set up a Virtual Environment
### Ubuntu 16.08
To install virtual environment on Ubuntu 16.06 use the commands below:
```
apt-get update
apt-get install virtualenv
virtualenv -p python my-api
ls my-api/lib
```

**Access the environment**
```
source my-api/bin/activate
```

**Exit the environment**
```
deactivate
```

### Windows
To install virtual environment on Windows use the commands below:
```
pip install virtualenv
mkvirtualenv my-api
setprojectdir .
```

**Access the environment**
```
workon my-api
```

**Exit the environment**
```
deactivate
```

## Install the required packages
Run the following lines of code:
```
pip install flask
pip install connexion
pip install pymysql

pip freeze > requirements.txt
```

# How to work with Connexion
For more information check https://github.com/zalando/connexion.

# To do
Further development is required in order to finish this project.

# Contributing
How can you contribute:

1. Fork it.
2. Create your feature branch (git checkout -b my-new-feature).
3. Commit your changes (git commit -am 'Added some feature').
4. Push to the branch (git push origin my-new-feature).
5. Create a new Pull Request.

# License
The current code is open-sourced software licensed under the [Apache license](http://www.apache.org/licenses/LICENSE-2.0).
