import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

# Load the data using xarray
nc_file = r"C:\Users\hp\OneDrive\Desktop\GitHub\Whales\Data\sample_data.nc"
data = xr.open_dataset(nc_file)
print(data)

#read_netcdf(nc_file, grid=None, name=None, just_grid=False, halo=0, nodata_value=-9999.0)

# Extract the latitude and longitude ranges
lat_range = data['lat'].values
lon_range = data['lon'].values
#print(lat_range.shape, lon_range.shape)

# Create a meshgrid of latitude and longitude values
lon, lat = np.meshgrid(lon_range, lat_range)
print(lon.shape, lat.shape)

print(data['tos'].values.shape)

# Plot the grid using pcolormesh
plt.pcolormesh(lon, lat, data['tos'].values[0,:,:])

# Add colorbar, title, and labels if needed
plt.colorbar()
plt.title('Grid of Map Regions')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Show the plot
plt.show()

