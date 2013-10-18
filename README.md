# python-console-snake

> Lightweight, configurable snake game running in the console

![Screenshot](http://s2.postimg.org/tzpt8rs09/snake.png)

### Usage

1. `git clone git@github.com:tancredi/python-console-snake.git`
2. `cd python-console-snake`
3. `python snake`

### Options

Run `python snake -help` for list of options

```
Usage: snake [options]

Options:
  -h, --help            show this help message and exit
  -s SIZE, --size=SIZE  Game size (s | m | l)
  -f, --fullscreen      Play fullscreen
  -t THEME, --theme=THEME
                        Game theme (classic | minimal | jungle | custom)
```

### Themes

You can select a theme by running `snake -t [ theme_name ]`

The default theme is `classic`. Other available themes are the following:

#### `minimal`

![Minimal theme screenshot](http://s15.postimg.org/9qnoxbauj/snake_minimal.png)

#### `jungle`

![Jungle theme screenshot](http://s9.postimg.org/f37kp89lr/snake_jungle.png)

#### `80s`

![80s theme screenshot](http://s23.postimg.org/k27e601uy/snake80s.jpg)

### Contribute

Add your theme to `snake/themes.py`, pull requests are welcome!
