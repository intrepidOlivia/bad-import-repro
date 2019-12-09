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