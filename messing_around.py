import nctoolkit as nc
import xarray as xr

file1 = 'Data/SST_2018-2023.nc'
file2 = 'Data/color_2018-2023.nc'

# Open the first NetCDF file
ds1 = xr.open_dataset(file1)

# Open the second NetCDF file
ds2 = xr.open_dataset(file2)

# Merge the two datasets along the time, latitude, and longitude dimensions
merged_ds = xr.merge([ds1, ds2])

# Save the merged dataset to a new NetCDF file
merged_ds.to_netcdf('Data/environmental.nc')