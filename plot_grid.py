import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from datetime import datetime

# Load the data using xarray
nc_file = "Data/SST_2018-2023.nc"
data = xr.open_dataset(nc_file)
print(data)

# Getting time or time range
# start_date = np.datetime64('2018-01-01') 
# average = False
# if average == True:
#     year_range = 'all' # or change to target range
#     month_range = 'all'
#     day_range = 'all'
# else:
#     year = 2018
#     month = 1
#     day = 1
#     time = np.datetime64(f'{year}-{month:02}-{day:02}') - start_date
#     cal_date = f'{year}-{month}-{day}'
#     print(time, cal_date)

# time = cal_date - np.datetime64(start_date, 'D') # time index

cal_date = '2018-01-01'
start_date = datetime.strptime('2018-01-01', '%Y-%m-%d')
target_date = datetime.strptime(cal_date, '%Y-%m-%d')
time = (target_date - start_date).days


dep_var, var_name = data['analysed_sst'], 'Sea Surface Temperature'
if var_name == "Sea Surface Temperature":
    var_name_short = "SST"
dep_var = dep_var.values[time,:,:]

#read_netcdf(nc_file, grid=None, name=None, just_grid=False, halo=0, nodata_value=-9999.0)

# Extract the latitude and longitude ranges
lat_range = data['latitude'].values
lon_range = data['longitude'].values
#print(lat_range.shape, lon_range.shape)

# Create a meshgrid of latitude and longitude values
lon, lat = np.meshgrid(lon_range, lat_range)

fig, ax = plt.subplots(figsize=(10, 6), subplot_kw={'projection': ccrs.PlateCarree()})

# Plot the data on a latitude and longitude scale
im = ax.pcolormesh(lon, lat, dep_var, transform=ccrs.PlateCarree())

# Mask out land
ax.add_feature(cfeature.LAND, zorder=1, facecolor='w')

# Add coastlines
#ax.coastlines('10m')

# Add a colorbar, title, and labels
cbar = plt.colorbar(im, ax=ax)
plt.title(f'{var_name} on {cal_date}')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.savefig(f'Output/{var_name_short}_{cal_date}.pdf')

