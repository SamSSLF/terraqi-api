import xarray as xr

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
