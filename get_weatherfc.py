from ecmwf.opendata import Client
import xarray as xr

client = Client()
parameters = ['10u', '10v', 'sp', 'msl']
client.retrieve(
    stream="oper",
    type="fc",
    step=[ 0,  3,  6,  9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 102, 105, 108, 111, 114, 117, 120, 123, 126, 129, 132, 135, 138, 141, 144],
    levtype="sfc",
    param=parameters,
    target='weather_forecasts/latest-uvp-fc.grib'
)
parameters = ['2t']
client.retrieve(
    stream="oper",
    type="fc",
    step=[ 0,  3,  6,  9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 102, 105, 108, 111, 114, 117, 120, 123, 126, 129, 132, 135, 138, 141, 144],
    levtype="sfc",
    param=parameters,
    target='weather_forecasts/latest-2t-fc.grib'
)

ds = xr.open_mfdataset('weather_forecasts/*.grib', engine='cfgrib', compat ='override')

# Define the geographical bounds for the UK
lat_min, lat_max = 49.9, 60.0
lon_min, lon_max = -10.0, 2.1

# Create a boolean array based on the latitude and longitude coordinates
in_uk = (ds['latitude'] >= lat_min) & (ds['latitude'] <= lat_max) & \
        (ds['longitude'] >= lon_min) & (ds['longitude'] <= lon_max)

# Use the boolean array to select only the rows within the UK bounds
ds = ds.where(in_uk, drop=True)

# Export ds to be used in other Python scripts as an xarray dataset
ds=ds.to_netcdf('weather_forecasts/latest_weather_fc.nc')