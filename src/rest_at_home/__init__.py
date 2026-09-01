# from . import hp_wx

# def main() -> None:
#     print("Hello from rest-at-home!")


def update():
    from . import hp_wx

    hp_wx.update_current_data()
