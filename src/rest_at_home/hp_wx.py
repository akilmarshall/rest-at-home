import pandas as pd
import datetime
import requests


class WxDataHP:

    def __init__(self):
        cols = [
            "year", "month", "day", "hour", "minute",
            "extra_col",              # undocumented 6th field, not in the official column list
            "temperature_C", "dew_pt_C", "RH_pct",
            "wind_speed_mph", "wind_direction_deg", "peak_wind_speed_mph",
            "rain_mm", "pressure_mb", "PW_mm"]

        path = "hp-wx.dat"

        df = pd.read_csv(path, sep=r"\s+", header=None, names=cols, na_values=["NaN"])

        # flag rows with fewer than 15 fields in the raw file -- columns after
        # the gap are misaligned/unreliable for these rows
        with open(path) as f:
            n_fields = pd.Series([len(line.split()) for line in f])
        df["n_fields"] = n_fields.values
        bad_rows = df["n_fields"] != 15
        print(f"{bad_rows.sum()} of {len(df)} rows have missing fields (unreliable columns)")

        # build a datetime index (HST)
        df["datetime"] = pd.to_datetime(df[["year", "month", "day", 'hour', 'minute']])

        self.data = df.loc[~bad_rows].drop(columns=['n_fields', 'PW_mm']).set_index('datetime')

    def current(self):
        return self.data.iloc[-1].to_dict()


def update_current_data():
    now = datetime.datetime.now()
    api = f'http://mkwc.ifa.hawaii.edu/archive/wx/hp/hp-wx.{now.year}.dat'
    r = requests.get(api)
    with open('hp-wx.dat', 'wb') as fd:
        fd.writelines(r.iter_content(chunk_size=128))
