# markdown-figure

An extension to the [Python Markdown](https://pypi.python.org/pypi/Markdown) package.

The exension wraps all images in the markdown document or text in `<figure>` tags, inserting a `<figcaption>` as well by re-using the `img alt` tag from markdown syntax (text in square brackets).

To install, clone the git repo and use ```pip install markdown-figure```

Then the extension can be used by doing:
```python

import markdown
from mdfigure import FigureExtension

md = markdown.Markdown(extensions=[FigureExtension()])

# Wrap an Image
md.convert('![my description](image.jpg)')
```
