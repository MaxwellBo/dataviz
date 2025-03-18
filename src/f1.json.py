
"""
Position changes during a race
==============================

Plot the position of each driver at the end of each lap.
"""

import matplotlib.pyplot as plt

import fastf1.plotting

# Load FastF1's dark color scheme
fastf1.plotting.setup_mpl(mpl_timedelta_support=False, misc_mpl_mods=False,
                          color_scheme='fastf1')


##############################################################################
# Load the session and create the plot
session = fastf1.get_session(2023, 1, 'R')
session.load(telemetry=True, weather=True)

print(session.laps.pick_drivers('1').get_pos_data().add_driver_ahead().to_json())


# create a "tidy" version of the data - we want every single driver in the session
# and we want each row to also have a driver column

