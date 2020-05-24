# RGB+W LED Strip Controller

_Short description here_

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
	"intensity": "100%"
}
```
```json
{
	"status": "off",
	"color": null,
	"intensity": null
}
```

### Turn on the LED Strip

**Definition**

`POST /strip`

**Arguments**

- `"status":string`
- `"color":string` - optional. Default `FFFFFF`
- `"intensity":int` - optional. Default `50`

**Response**

- `200 OK`

```json
{
	"status": "on",
	"color": "#FF0000",
	"intensity": "100%"
}
```

### Turn off the LED Strip

**Definition**

`POST /strip`

**Arguments**

- `"status":string`

**Response**

- `200 OK`

```json
{
	"status": "off",
	"color": null,
	"intensity": null
}
```

### Change the color or intensity of the LED Strip

**Definition**

`POST /strip`

**Arguments**

- `"color":string`
- `"intensity":int`

At least one of the arguments must be specified

**Response**

- `200 OK`

```json
{
	"status": "on",
	"color": "#FF00000",
	"intensity": "100%"
}
```
