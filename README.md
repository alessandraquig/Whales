# Whales

This project is designed to work with Underwater Africa's existing datasets. It takes sea surface temperature, sea surface color, bathymetry, and sea surface height? (surface currents?) to create a complete dataset at 0.1 x 0.1 degree and daily resolution. From there, I'm planning to add whale presence data, along with (maybe) pseudoabsences generated along search grid.

Random forest?

### Data Sources

SST: https://coastwatch.pfeg.noaa.gov/erddap/griddap/jplMURSST41.html
(Full request link for coordinates and dates is https://coastwatch.pfeg.noaa.gov/erddap/griddap/jplMURSST41.nc?analysed_sst%5B(2018-01-01T09:00:00Z):1:(2023-12-31T09:00:00Z)%5D%5B(-24.5):1:(-22.5)%5D%5B(34.5):1:(36.5)%5D)
Color: https://rsg.pml.ac.uk/thredds/ncss/grid/CCI_ALL-v6.0-1km-DAILY/dataset.html
(Full request link for coordinates and dates is https://rsg.pml.ac.uk/thredds/ncss/CCI_ALL-v6.0-1km-DAILY?var=chlor_a&north=-22.5&west=34.5&east=36.5&south=-24.5&disableProjSubset=on&horizStride=1&time_start=2018-01-01T00%3A00%3A00Z&time_end=2023-12-31T00%3A00%3A00Z&timeStride=1&addLatLon=true&accept=netcdf)
Bathymetry: https://download.gebco.net/
SSH: https://data.marine.copernicus.eu/product/GLOBAL_MULTIYEAR_PHY_001_030/services
Surface currents: https://data.marine.copernicus.eu/product/GLOBAL_MULTIYEAR_PHY_001_030/services
Distance from shore: Can be calculated

For currents, I had to download two separate datasets split in June/July 2021 and the combine them using the bash command (while running whales_proj Python environment): cdo mergetime currents_2018-2021.nc currents_2021-2023.nc currents_2018-2023.nc

### Helpful links
https://ferret.pmel.noaa.gov/Ferret/documentation/coards-netcdf-conventions - netCDF standard column headings, etc.
