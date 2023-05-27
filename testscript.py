import xarray as xr

ds = xr.open_dataset('weather_forecasts/latest_weather_fc.nc')

msl = ds['msl'].to_dataframe()

print(msl.head())
