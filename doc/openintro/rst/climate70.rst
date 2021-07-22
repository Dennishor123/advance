========= ===============
climate70 R Documentation
========= ===============

Temperature Summary Data, Geography Limited
-------------------------------------------

Description
~~~~~~~~~~~

A random set of monitoring locations were taken from NOAA data that had
both years of interest (1948 and 2018) as well as data for both summary
metrics of interest (dx70 and dx90, which are described below).

Usage
~~~~~

::

   climate70

Format
~~~~~~

A data frame with 197 observations on the following 7 variables.

station
   Station ID.

latitude
   Latitude of the station.

longitude
   Longitude of the station.

dx70_1948
   Number of days above 70 degrees in 1948.

dx70_2018
   Number of days above 70 degrees in 2018.

dx90_1948
   Number of days above 90 degrees in 1948.

dx90_2018
   Number of days above 90 degrees in 2018.

Details
~~~~~~~

Please keep in mind that these are two annual snapshots, and a complete
analysis would consider much more than two years of data and much
additional information for those years.

Source
~~~~~~

https://www.ncdc.noaa.gov/cdo-web/datasets, retrieved 2019-04-24.

Examples
~~~~~~~~

::


   # Data sampled are from the US, Europe, and Australia.
   # This geographic limitation may be due to the particular
   # years considered, since locations without both 1948 and
   # 2018 were discarded for this (simple) data set.
   plot(climate70$longitude, climate70$latitude)

   plot(climate70$dx70_1948, climate70$dx70_2018)
   abline(0, 1, lty = 2)
   plot(climate70$dx90_1948, climate70$dx90_2018)
   abline(0, 1, lty = 2)
   hist(climate70$dx70_2018 - climate70$dx70_1948)
   hist(climate70$dx90_2018 - climate70$dx90_1948)

   t.test(climate70$dx70_2018 - climate70$dx70_1948)
   t.test(climate70$dx90_2018 - climate70$dx90_1948)