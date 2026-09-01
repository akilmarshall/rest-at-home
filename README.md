Home assistant has nice integration for rest API(s).
However, there are some API(s) I would like to consume in Home assistant that do not offer a rest interface.
So this project provides the in between with python and Fast API.

# Deploy

Make the bin

```
uv sync --frozen  
```

Install the unit and timer files

```
cp rest-at-home.service rest-at-home.timer ~/.config/systemd/user/ 
cp rest-at-home-api.service ~/.config/systemd/user
```

Enable and start the timer

```
systemctl --user enable --now rest-at-home.timer
```

Check timer

```
systemctl --user list-timers rest-at-home.timer
```
