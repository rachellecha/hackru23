import pandas as pd
import numpy as np

# pd.options.display.float_format = '{:.2%}'.format

#rail_data folder csv import
agency = pd.read_csv("rail_data/agency.txt").set_index('agency_id')
calendar_date = pd.read_csv("rail_data/calendar_dates.txt").set_index('date')
routes = pd.read_csv("rail_data/routes.txt").set_index('route_id')
stop_times = pd.read_csv("rail_data/stop_times.txt")
stops = pd.read_csv("rail_data/stops.txt").set_index('stop_id')
trips = pd.read_csv("rail_data/trips.txt").set_index('trip_id')

#Rail Cancellations
cancellations = pd.read_csv("RAIL_CANCELLATIONS_DATA.csv", \
    names = ["YEAR", "MONTH", "CATEGORY", "CANCEL_COUNT", "CANCEL_TOTAL", "CANCEL_PERCENTAGE"], \
    dtype = {"YEAR": np.int32, "MONTH": str, "CATEGORY": str, "CANCEL_COUNT": np.int32, \
        "CANCEL_TOTAL": np.int32, "CANCEL_PERCENTAGE": np.float32}, skiprows = 1)
cancellations["MONTH"] = cancellations.MONTH.apply(lambda x: x.strip())
cancellations["CATEGORY"] = cancellations.CATEGORY.apply(lambda x: x.strip())
cancellations["CANCEL_PERCENTAGE"] = cancellations.CANCEL_PERCENTAGE.apply(lambda x: x / 100)

#Mean Distance Between Failure
mdbf = pd.read_csv("RAIL_MDBF_DATA.csv", names = ["MONTH", "MDBF"], \
    dtype = {"MONTH": str, "MDBF": np.int32}, skiprows = 1)
mdbf["MONTH"] = mdbf.MONTH.apply(lambda x: x.strip())
mdbf[["YEAR", "MONTH"]] = mdbf.MONTH.str.split(" ", expand = True)
mdbf = mdbf[["YEAR"] +  ["MONTH", "MDBF"]]

#Rail On Time Performance
otp = pd.read_csv("RAIL_OTP_DATA.csv", names = ["YEAR","MONTH","STATUS","COUNT","TOTAL","PERCENTAGE"],\
    dtype = {"YEAR": np.int32,"MONTH": str,"STATUS": str,"COUNT": np.int32,"TOTAL": np.int32,\
        "PERCENTAGE": np.float32}, skiprows = 1)
otp.drop("STATUS", axis = 1, inplace = True)
otp["MONTH"] = otp.MONTH.apply(lambda x: x.strip())
otp["PERCENTAGE"] = otp.PERCENTAGE.apply(lambda x: x / 100)