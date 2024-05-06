import netCDF4 as nc

def combine_files(input_file1, input_file2, output_file):
    # Open the input files
    file1 = nc.Dataset(input_file1, 'r')
    file2 = nc.Dataset(input_file2, 'r')

    # Create the output file
    output = nc.Dataset(output_file, 'w')

    # Copy global attributes from the first input file to the output file
    for attr_name in file1.ncattrs():
        output.setncattr(attr_name, getattr(file1, attr_name))

    # Copy dimensions from the first input file to the output file
    for dim_name, dim in file1.dimensions.items():
        output.createDimension(dim_name, len(dim) if not dim.isunlimited() else None)

    # Copy variables from the first input file to the output file
    for var_name, var in file1.variables.items():
        output.createVariable(var_name, var.dtype, var.dimensions)
        output[var_name][:] = var[:]

    # Append variables from the second input file to the output file along the time dimension
    for var_name, var in file2.variables.items():
        if 'time' in var.dimensions:
            output.createVariable(var_name, var.dtype, var.dimensions)
            output[var_name][:] = var[:]

    # Close the files
    file1.close()
    file2.close()
    output.close()

# Usage example
if __name__ == '__main__':

    input_file1 = '/Data/currents_2018-2021.nc'
    input_file2 = '/Data/currents_2021-2023.nc'
    output_file = '/Data/currents_2018-2023.nc'
    combine_files(input_file1, input_file2, output_file)