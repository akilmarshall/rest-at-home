from fastapi import FastAPI
from rest_at_home import hp_wx

app = FastAPI()


@app.get('/wx/hp/current')
def wx_current_hp():
    wx_data_hp = hp_wx.WxDataHP()
    return wx_data_hp.current()
