# markdown-figure

An extension to the [Python Markdown](https://pypi.python.org/pypi/Markdown) package.

The extension wraps all images in the markdown document or text in `<figure>` tags, inserting a `<figcaption>` as well by re-using the `img alt` tag from markdown syntax (text in square brackets).

To install use `pip install markdown-figure` or use the repository `pip install git+https://github.com/janwh/markdown-figure.git`

Then the extension can be used by doing:
```python

import markdown
from mdfigure import FigureExtension

md = markdown.Markdown(extensions=[FigureExtension()])

# Wrap an Image
md.convert('![my description](image.jpg)')
```

## Configuration

| Name                 | Description                                           | Default |
| -------------------- | ----------------------------------------------------- | ------- |
| `figure_classes`     | Class attributes assigned to the `<figure />` tag     | `None`  |
| `img_classes`        | Class attributes assigned to the `<img />` tag        | `None`  |
| `figcaption_classes` | Class attributes assigned to the `<figcaption />` tag | `None`  |
| `multiline`          | Support line breaks in the `<figcaption />` tag       | `True`  |

## Options

The fragment of the image `src` link is available in `<figure data-options=""/>`.

Example of the right alignment.

```python
# Wrap an Image with "right" option
md.convert('![my description  \nsecond line](image.jpg#right)')
```

With custom CSS.

```css
figure[data-options~="right"] {
  float: right;
}
```
