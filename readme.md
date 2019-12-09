Specifications:

* PyCharm version 2019.3
* Python version 3.7.3
* Windows 10

Reproduction instructions:

1. Configure Pycharm to initialize a virtual environment for the project.

2. Install requirements.txt

3. Start a debug session with the following configuration:

    * Script path: `src\repro.py`
    * Environment variables: `PYTHONUNBUFFERED=1`
    * Python interpreter: `[local virtual environment]`
    * Working directory: `[absolute-path]\debug-repro\`
    * [X] Add content roots to PYTHONPATH
    * [X] Add source roots to PYTHONPATH

4. View the values of `sys.modules['pkg_resources']` and `sys.executable` printed in the debug console.

My console says this:
```
Connected to pydev debugger (build 193.5233.109)
INFO: Uvicorn running on http://0.0.0.0:9000 (Press CTRL+C to quit)
INFO: Started reloader process [116224]
Main process running.
pkg_resources path: <module 'pkg_resources' from 'C:\\Repositories\\debug-repro\\env\\lib\\site-packages\\setuptools-40.8.0-py3.7.egg\\pkg_resources\\__init__.py'>
sys.executable: C:\Repositories\debug-repro\env\Scripts\python.exe
Main process running.
pkg_resources path: <module 'pkg_resources' from 'C:\\Users\\THIS_USER\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages\\pkg_resources\\__init__.py'>
sys.executable: C:\Users\THIS_USER\AppData\Local\Programs\Python\Python37\python.exe
Main process running.
pkg_resources path: <module 'pkg_resources' from 'C:\\Users\\THIS_USER\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages\\pkg_resources\\__init__.py'>
sys.executable: C:\Users\THIS_USER\AppData\Local\Programs\Python\Python37\python.exe
Uvicorn process running
INFO: Started server process [74060]
INFO: Waiting for application startup.
```
