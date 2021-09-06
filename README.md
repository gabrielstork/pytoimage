# pytoimage

*Note: pytoimage is still in its initial stages, for now, you can normally transform your code in an image, choosing the backgroud and the text color. But, all code is currently with a single color, not differentiating anything, such as keywords, strings, functions... this will come in future versions.*

## Download

You can simply:

```sh
pip install pytoimage
```

Or you can also:

1. Clone the repository to your local machine.
2. Enter the directory.
3. Download necessary modules/libraries.

```sh
git clone https://github.com/gabrielstork/pytoimage.git
cd pytoimage
pip install -r requirements.txt
```

## Example

```python
from pytoimage import PyImage
```

The **PyImage** class has three parameters: **path** (the Python code path), **background** (*optional*, the background color of the image) and **font** (*optional*, the path of a **.ttf** font).

```python
code = PyImage('pytoimage/pytoimage.py', background=(15, 15, 15), font='fonts/Inconsolata.ttf')
```

The following method is optional, it allows you customize the theme of your image (*see initial note*).

```python
palette = {
    'line': (149, 149, 149),
    'normal': (255, 255, 255),
}

code.set_color_palette(palette=palette)
```

To generate the image, you can simply call the method with no arguments, the **start** and **end** are optionals, these are the code intervals.

```python
code.generate_image(start=39, end=51)
```

Then you can see and save the generated image.

```python
code.show_image()
```

![Example](https://raw.githubusercontent.com/gabrielstork/pytoimage/main/images/example.png?token=AUUMP4TZFVIWGTGZPVBE4FLBGYFAM)


```python
code.save_image('images/example.png')
```

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://github.com/gabrielstork)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/gabrielstork)