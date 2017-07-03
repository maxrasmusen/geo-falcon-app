# Devices web server
## Usage
- Clone the repo
- Install needed packages by running ```pip install -r requirements.txt``` in the root directory.
- Run the app by running ```gunicorn device_app:app``` in the app directory.
- Run the tests by running ```python devices_test.py``` in the tests directory.

## Endpoints
- Get one device -> 'GET' '/devices', Header -> {"device-name": device_name}
- Get all devices -> 'GET' '/devices'
