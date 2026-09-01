Home assistant has nice integration for rest API(s).
However, there are some API(s) I would like to consume in Home assistant that do not offer a rest interface.
So this project provides the in between with python and Fast API.

# Deploy




```
# make the bin
uv sync --frozen  
# install the update service and timer
cp rest-at-home.service rest-at-home.timer ~/.config/systemd/user/ 
# enable and start the timer
systemctl --user enable --now rest-at-home.timer
# check timer
systemctl --user list-timers rest-at-home.timer
```
