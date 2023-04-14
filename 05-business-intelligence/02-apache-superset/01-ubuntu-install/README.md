#### About
> Apache Superset

Apache Superset is a modern, open-source data exploration and visualization platform that empowers users to interact with and analyze complex data sets. With Superset, users can easily create interactive and visually appealing dashboards, charts, and reports from a wide range of data sources.

> Installation
1. Create the environment using environment.yml
```
$ conda env create -n superset-env -f environment.yml
```
2. Add following environment variables to .bashrc and run source .bashrc
```
$ export FLASK_APP=superset
$ export SUPERSET_CONFIG_PATH=~/.superset/superset_config.py
```
3. Ensure secret key is generated using ssl and quoted in superset_config.py
```
$ SECRET_KEY='1211c822255634b1aafa87c8d790c076' #generate your own ssl key
```
4. Run the following command
```
$ superset db upgrade
$ superset init
$ export FLASK_APP=superset & superset fab create-admin
$ superset run -p 8080 --with-threads --reload --debugger
```
5. Use the created username and password to access the webapp at http://127.0.0.1:8088/
6. Installation done !