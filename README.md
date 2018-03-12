A [Polybar](https://github.com/jaagr/polybar) module to display online channels from Twitch


## Dependencies

- [font-awesome](https://fontawesome.com/) for Twitch icon

## Setup

1. Copy `ploybar-twitch` and `settings.py` to `~/.config/polybar` (or pull this repo and symlink the script)

2. Make `polybar-twitch` executable with `chmod +x ~/.config/polybar/polybar-twitch`

3. Add the module to your polybar config:

```
[module/twitch]
type = custom/script
exec = python -u ~/.config/polybar/polybar_twitch
format = <label>

format-prefix = 
format-prefix-padding = 1

tail = true
```

## TODO

- [X] Cycling of online channels
- [ ] Click to open stream with streamlink 



