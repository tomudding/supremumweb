# Supremumweb


## Development environment
If you wish to run this website locally, do the following:

### Setup
0. Install python3 and git.
1. Download this git repository.
2. Run `setup.sh` (Linux, OS X) or `setup.bat` (Windows).
    - This creates a virtual environment (venv) and installs the necessary python packages.

### Start
After you have everything set up, run the following commands on the command line each time you want to start the server locally:

0. Run `source venv/bin/activate` (Linux, OS X) or `venv\Scripts\activate.bat` (Windows).
    - This activates the virtual environment we created in the setup.
    - It can be deactivated by running `source venv/bin/deactivate` (Linux, OS X) or `venv\Scripts\deactivate.bat` (Windows).
1. Execute `python3 wsgi.py`
    - This starts the development server.
2. Open `http://localhost:8080/` on your web browser to view the website.

### Automatic reload
This development server has been setup in such a way that when changing and saving a python file (`.py`), the server automatically restarts. Simply (force-)refresh your browser to view the update version: `ctrl+shift+r` (Windows, Linux) or `cmd+shift+r` (OS X).
This also works when updating a `.css` file. 

When you have updated an `.html` file, you have to restart the 

## Docker environment
If you wish to run this website in a docker setting, do the following:

0. Install docker
1. Run `bash start.sh` (Linux)
    - This creates and starts a docker container of the website. This can be accessed on `http://localhost:9500`.

## Documentation
The documentation for this repository is continued in the `app` folder.

## Configuration
The following environment variables should be provided:

| Name             | Purpose                                          |
|------------------|--------------------------------------------------|
| `SECRET_KEY`     | A secret key required to provide authentication. |
| `MYSQL_HOST`     | The hostname of a MYSQL database server.         |
| `MYSQL_PASS`     | The password of a MYSQL database user.           |
| `MYSQL_PORT`     | The port number of a MYSQL database server.      |
| `MYSQL_USER`     | The name of a MYSQL database user.               |

The following environment variables are *optional*:

| Name             | Purpose                                          |
|------------------|--------------------------------------------------|
| `APP_NAME`       | The name of the application. i.e Flask Bones     |
| `SERVER_NAME`    | The hostname and port number of the server.      |

## Updating production website
In order to update the live website, you need to push a new image of the docker container to the repository.

0. Run `docker build . -t supremum.docker-registry.gewis.nl/site:v<tag>`, where `<tag>` is the version number.
1. Run `docker push supremum.docker-registry.gewis.nl/site:v<tag>`.
2. Edit the stack at `docker.gewis.nl` to use the new version number provided in `<tag>`.
3. Congrats, you should now see your new image being used and the container to be newly created!