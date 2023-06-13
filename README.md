## Install Dependencies

In your Terminal, type:

    pip install -r requirements.txt

Make sure you have Anaconda or Miniconda installed and run the following:

    conda install -c conda-forge cfgrib

## API Documentation

### GET Welcome Page

```
https://api.terraqi.com/
```

This endpoint simply returns a welcome message. Use it to test that you have successfully connected to the TerraQi API.

**Parameters:**
None

**Example request:**

```http
GET https://api.terraqi.com/
```

**Response**

```json
{
    "message": "Welcome to TerraQi API"
}
```

### POST Wind Forecast
```
https://api.terraqi.com/windfc/daily
```

**Parameters:**
- `lat`: latitude value of the grid point coordinate
- `lon`: longitude value of the grid point coordinate

**Example Request**
```json
{
    "lat": 51.4850816,
    "lon": -0.1998848
}
```

**Example Response**
```json
{
    "windpower_fc": {
        "1686614400000": 0.1122693419,
        "1686625200000": 0.2363074422,
        "1686636000000": 0.2184668481,
        "1686646800000": 0.2070340514,
        "1686657600000": 0.3460422754,
        "1686668400000": 0.4451768398,
        "1686679200000": 0.34550035,
        "1686690000000": 0.2410722524,
        "1686700800000": 0.1633887291,
        "1686711600000": 0.3006751537,
        "1686722400000": 0.1875288039,
        "1686733200000": 0.1818574518,
        "1686744000000": 0.1888142079,
        "1686754800000": 0.1344777793,
        "1686765600000": 0.1842687875,
        "1686776400000": 0.1050140932,
        "1686787200000": 0.0908293277,
        "1686798000000": 0.0551808402,
        "1686808800000": 0.1276064515,
        "1686819600000": 0.1225540638,
        "1686830400000": 0.0268399995,
        "1686841200000": 0.0238618758,
        "1686852000000": 0.1741912663,
        "1686862800000": 0.1032149941,
        "1686873600000": 0.0641671866,
        "1686884400000": 0.0663706213,
        "1686895200000": 0.0437138677,
        "1686906000000": 0.0781069323,
        "1686916800000": 0.03117387,
        "1686927600000": 0.0232977811,
        "1686938400000": 0.1457949281,
        "1686949200000": 0.1437875777,
        "1686960000000": 0.1041159704,
        "1686970800000": 0.0543761216,
        "1686981600000": 0.1246198863,
        "1686992400000": 0.1884133518,
        "1687003200000": 0.3275586069,
        "1687014000000": 0.3261328936,
        "1687024800000": 0.2860892117,
        "1687035600000": 0.2580200434,
        "1687046400000": 0.2852399945,
        "1687057200000": 0.198491618,
        "1687068000000": 0.0872025862,
        "1687078800000": 0.253704071,
        "1687089600000": 0.4292662144,
        "1687100400000": 0.5313417912,
        "1687111200000": 0.2459944487,
        "1687122000000": 0.5197150707,
        "1687132800000": 0.4108301401
    }
}
```
### POST Wind Forecast - Daily Average

```
https://api.terraqi.com/windfc/daily
```

**Parameters:**
- `lat`: latitude value of the grid point coordinate
- `lon`: longitude value of the grid point coordinate

**Example Request**
```json
{
    "lat": 51.4850816,
    "lon": -0.1998848
}
```

**Example Response**
```json
{
    "2023-06-13": {
        "average": 0.2689836752,
        "power_rating": 2
    },
    "2023-06-14": {
        "average": 0.1807531258,
        "power_rating": 1
    },
    "2023-06-15": {
        "average": 0.0905348524,
        "power_rating": 1
    },
    "2023-06-16": {
        "average": 0.0745515956,
        "power_rating": 1
    },
    "2023-06-17": {
        "average": 0.2086657607,
        "power_rating": 2
    },
    "2023-06-18": {
        "average": 0.3188694743,
        "power_rating": 2
    },
    "2023-06-19": {
        "average": 0.4108301401,
        "power_rating": 3
    }
}
```
### POST Wind Forecast - Daily Average Energy

```
https://api.terraqi.com/windfc/daily/energy
```

**Parameters:**
- `lat`: latitude value of the grid point coordinate
- `lon`: longitude value of the grid point coordinate

**Example Request**
```json
{
    "lat": 51.4850816,
    "lon": -0.1998848,
    "turbine_rated_power": 800
}
```

**Example Response**
```json
{
    "2023-06-13": {
        "AvgEnergy_Wh": 4740.4766499996,
        "power_rating": 2
    },
    "2023-06-14": {
        "AvgEnergy_Wh": 3148.3766287565,
        "power_rating": 1
    },
    "2023-06-15": {
        "AvgEnergy_Wh": 1505.4159790277,
        "power_rating": 1
    },
    "2023-06-16": {
        "AvgEnergy_Wh": 1181.8449184299,
        "power_rating": 1
    },
    "2023-06-17": {
        "AvgEnergy_Wh": 3571.8193888664,
        "power_rating": 2
    },
    "2023-06-18": {
        "AvgEnergy_Wh": 5156.3478291035,
        "power_rating": 2
    },
    "2023-06-19": {
        "AvgEnergy_Wh": 0.0,
        "power_rating": 3
    }
}
```