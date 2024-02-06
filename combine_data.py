import nctoolkit as nc

file1 = 'Data/SST_2018-2023.nc'
file2 = 'Data/color_2018-2023.nc'

# Open the first NetCDF file
ds1 = nc.Dataset(file1)

# Open the second NetCDF file
ds2 = nc.Dataset(file2)

# remove the 1st netcdf files variables from the second's
ds2.drop(ds1.variables)
# merge the files
ds1.append(ds2)
ds1.merge()

# save the files as a netcdf file
#ds1.to_nc("environmental_data.nc")