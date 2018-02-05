# Polybar Twitch

A [Polybar] module to display online channels from Twitch


## Dependencies

[twitchnotifier]

[font-awesome] for Twitch icon

## Setup

1. copy `ploybar_twitch` to `~/.config/polybar` (or pull this repo and symlink the script)

2. Make the scrip executable with `chmod +x ~/.config/polybar/polybar_twitch`

3. Add the module to your polybar config:

```[module/twitch]
type = custom/script
exec = ~/.config/polybar/polybar_twitch
format = <label>

format-prefix = 
format-prefix-padding = 1```


## TODO

- Cycling of online channels
- Click to open stream with streamlink 



