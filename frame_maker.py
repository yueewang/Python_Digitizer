import soda_plot_function_2 as spf

url = 'http://sodaserver.tamu.edu:80/opendap/TEMP/SODA_2.3.1_01-01_python.cdf'
variable = 'TEMP'
llat = -70.
ulat = 70.
llon = 1.
rlon = 359.


time = range(1,20)

for t in time:
    spf.soda_plot(url,variable,llat, ulat, llon, rlon,t,depth=0)