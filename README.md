# fasten-pypi-plugin

A Python plugin that can be used to analyze and report issues about a modules dependencies at build time.

To get this plugin running:

**On Linux, the following commands may require `sudo` privilege, but that may cause problems with your system as the official package manager for linux is `apt`.  
Therefore, it is recommended by the [official python documentation](https://docs.python.org/3/tutorial/venv.html) to use a virtual environment for python development.**

1. Make sure that you have the packages [`pycg`](https://github.com/vitsalis/pycg) and [`pycg-stitch`](https://github.com/fasten-project/pycg-stitch) installed.  
   To install them run the following inside the pycg / pycg-stitch folder:
    ```
    pip install pycg pycg-stitch requests 
    ```

2. To install the `pypi-plugin` on your system run the following command inside the pypi-plugin folder:
    ```
    python3 setup.py sdist bdist_wheel
    python3 -m pip install dist/fasten-0.0.1-py3-none-any.whl
    ```
   If you installed the plugin already but made any changes, you can reinstall it via:
    ```
    python3 -m pip install --force-reinstall dist/fasten-0.0.1-py3-none-any.whl
    ```

3. After the installation is complete, run
    ```
    fasten -h
    ```
   to get instructions on how to use the plugin.

**Steps 5 to 7 explain how to use a local database running [docker-python-pipeline](https://github.com/fasten-project/fasten-docker-deployment).  
These steps are optional as the pypi-plugin takes its information from the fasten server by default.**

4. Run the docker-python-pipeline first:
    ```
    sudo docker-compose --profile python up -d
    ```

5. Feed the database with the [testPackages.txt](https://github.com/fasten-project/fasten-pypi-plugin/blob/development/testPackages.txt)-file:
    ```
    cat testPackages.txt | sudo docker-compose exec -T kafka kafka-console-producer.sh --broker-list kafka:9092 --topic fasten.PyPI.releases --property 'parse.key=true' --property 'key.separator=|'
    ```

6. Check if the pipeline is fed (will take a while):
 * via curl:
    ```
    curl -X GET localhost:9080/api/pypi/packages
    ```
 * via the `metadata-db` container:
	* exec inside the container:
    ```
    sudo docker-compose exec metadata-db /bin/bash
    ```
	* query the database:
    ```
    PGPASSWORD=fasten1234 psql --host localhost --port 5432 --username fasten fasten_python --command="SELECT * FROM packages;"
    ```

7. Change the `url` variable in the [main](https://github.com/fasten-project/fasten-pypi-plugin/blob/packageCreation/src/fasten/__main__.py) function to `http://127.0.0.1:9080` to connect to your local database.

8. You can also run the pypi-plugin from inside the `fasten-pypi-plugin/src/fasten`-folder for development or testing purposes:
    ```
    python3 main.py \
            --product fasten-pypi-plugin \
            --pkg_name fasten-pypi-plugin \
            --project_path ./ \
            --timestamp 42 \
            --version 1.0 \
            --requirements ../../requirements.txt \
            --fasten_data callGraphs/ \
            --scg_path callGraphs/
    ```

1. The Call-Graphs can be found inside the `fasten-pypi-plugin/src/fasten/callGraphs`-folder.
