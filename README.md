# RGB+W LED Strip Controller

A simple dockerized API based on Flask and uWSGI that can control a SMD5050 RGBW LED strip. Structure:

```
.
|-- bin
|   |-- chaos.sh
|   `-- run.sh
|-- docker
|   |-- app
|   |   |-- helpers
|   |   |   |-- colors.py
|   |   |   |-- __init__.py
|   |   |   `-- validator.py
|   |   |-- __init__.py
|   |   `-- models
|   |       |-- __init__.py
|   |       `-- strip.py
|   |-- app.ini
|   `-- wsgi.py
|-- Dockerfile
|-- LICENSE
|-- README.md
`-- requirements.txt

5 directories, 14 files
```

## Usage

### Get the current status of the LED Strip

**Definition**

`GET /strip`

**Response**

- `200 OK`

```json
{
	"status": "on", 
	"color": "#FF0000",
	"intensity": 1.0
}
```

### Toggle the LED Strip

**Definition**

`POST /strip`

**Arguments**

- `"status":string` can be either "on" or "off"
- `"color":string` optional, HEX value. Default `#FFFFFF`
- `"intensity":float` optional, range [0.1 - 1.0]. Default `0.5`

**Response**

- `200 OK`

```json
{
	"status": "on",
	"color": "#FF0000",
	"intensity": 0.5
}
```

### Change the color or intensity of the LED Strip

**Definition**

`POST /strip`

**Arguments**

- `"color":string`
- `"intensity":float`

At least one of the arguments must be specified

**Response**

- `200 OK`

```json
{
	"status": "on",
	"color": "#FF00000",
	"intensity": 0.5
}
```
