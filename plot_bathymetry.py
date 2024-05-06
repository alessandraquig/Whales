import xarray as xr
import matplotlib.pyplot as plt
import matplotlib
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# matplotlib.use('Agg')
#
# from matplotlib import rc
# this_rc_params = {
#     "text.usetex": True,
#     "font.family": "roman"
# }
# plt.rcParams.update(this_rc_params)

# Load the data using xarray
nc_file = "Data/bathymetry_regridded.nc"
data = xr.open_dataset(nc_file)
print(data)

dep_var, var_name = data['elevation'], 'Depth'

# Extract the latitude and longitude ranges
#lat_range = data['lat'].values
#lon_range = data['lon'].values
#print(lat_range.shape, lon_range.shape)

lon = data['lon'].values
lat = data['lat'].values

# Create a meshgrid of latitude and longitude values
#lon, lat = np.meshgrid(lon_range, lat_range)
#print(lon.shape, lat.shape)

#print(dep_var.values.shape)

fig, ax = plt.subplots(figsize=(10, 6), subplot_kw={'projection': ccrs.PlateCarree()})

# Plot the data on a latitude and longitude scale
im = ax.pcolormesh(lon, lat, dep_var, transform=ccrs.PlateCarree(), vmax=0)

# Mask out land
ax.add_feature(cfeature.LAND, zorder=1, facecolor='w')

# Add coastlines
ax.coastlines('10m')

# Add a colorbar
cbar = plt.colorbar(im, ax=ax)

# Set the title and labels
ax.set_title(r'Depth (m)')
ax.set_xlabel(r'Longitude')
ax.set_ylabel(r'Latitude')

plt.savefig('Output/bathymetry_map_regridded.pdf')

