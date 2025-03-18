
"""
Position changes during a race
==============================

Plot the position of each driver at the end of each lap.
"""

import matplotlib.pyplot as plt

import fastf1.plotting
import pandas as pd

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

print(df.to_json())

