import netCDF4 as nc

def combine_dimension_names(data):
# Extract the latitude and longitude variables
    lat_var = data.variables.get('lat') or data.variables.get('latitude')
    if lat_var is not None:
        lat = lat_var[:]
    else:
        raise ValueError("Latitude variable not found in the netCDF file.")
    lon_var = data.variables.get('lon') or data.variables.get('longitude')
    if lon_var is not None:
        lon = lon_var[:]
    else:
        raise ValueError("Longitude variable not found in the netCDF file.")
    return lat, lon

if __name__ == "__main__":
    # Read the netCDF file

    file1 = nc.Dataset('Data/color_2018-2023.nc', 'r')
    file2 = nc.Dataset('Data/SST_2018-2023.nc', 'r')

    lat1, lon1 = combine_dimension_names(file1)
    lat2, lon2 = combine_dimension_names(file2)

    print(lat1.shape, lon1.shape)
    print(lat2.shape, lon2.shape)

