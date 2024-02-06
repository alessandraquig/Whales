import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Load the data using xarray
nc_file = "Data\bathymetry.nc"
data = xr.open_dataset(nc_file)
print(data)

dep_var, var_name = data['elevation'], 'Depth'

# Extract the latitude and longitude ranges
lat_range = data['latitude'].values
lon_range = data['longitude'].values
#print(lat_range.shape, lon_range.shape)

# Create a meshgrid of latitude and longitude values
lon, lat = np.meshgrid(lon_range, lat_range)
print(lon.shape, lat.shape)

print(dep_var.values.shape)

fig, ax = plt.subplots(figsize=(10, 6), subplot_kw={'projection': ccrs.PlateCarree()})

# Plot the data on a latitude and longitude scale
im = ax.pcolormesh(lon, lat, dep_var, transform=ccrs.PlateCarree(), cmap='blues')

# Mask out land
ax.add_feature(cfeature.LAND, zorder=1, facecolor='w')

# Add coastlines
ax.coastlines('50m')

# Add a colorbar
cbar = plt.colorbar(im, ax=ax)

# Set the title and labels
ax.set_title('Depth')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

# Show the plot
plt.show()

