
"""
Position changes during a race
==============================

Plot the position of each driver at the end of each lap.
"""

import matplotlib.pyplot as plt
import fastf1.plotting
import pandas as pd
import duckdb

# Load FastF1's dark color scheme
fastf1.plotting.setup_mpl(mpl_timedelta_support=False, misc_mpl_mods=False,
                          color_scheme='fastf1')


##############################################################################
# Load the session and create the plot
session = fastf1.get_session(2023, 2, 'R')
session.load(telemetry=True, weather=True)

df = pd.DataFrame()

for driver in session.drivers:
  driver_pos = session.laps.pick_drivers(driver).get_pos_data().add_driver_ahead()
  driver_pos['DriverId'] = driver
  driver_pos['DriverName'] = session.get_driver(driver).FullName
  df = pd.concat([df, driver_pos], ignore_index=True)


# create a new duckdb database
con = duckdb.connect('f1.db')

# create a new table with X, Y, DriverId, DriverName
con.execute('CREATE TABLE f1 (X INTEGER, Y INTEGER, DriverId VARCHAR, DriverName VARCHAR)')
con.execute('INSERT INTO f1 SELECT X, Y, DriverId, DriverName FROM df')


# write the raw database file to stdout
# write the raw db file contents to stdout
with open('f1.db', 'rb') as f:
  print(f.read())

