# Devices web server
## Usage
- Clone the repo
- Install needed packages by running ```pip install -r requirements.txt``` in the root directory.
- Run the app by running ```gunicorn device_app:app``` in the root directory.
- Run the tests by running ```python devices_test.py``` in the root directory.

## Endpoints
- Get one device -> 'GET' '/devices', Header -> {"name": device_name}
- Get all devices -> 'GET' '/devices'