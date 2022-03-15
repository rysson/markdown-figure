"""
Extension for markbox to make all images lightbox

copyright @2015 Alicia Schep <aschep@gmail.com>

"""
import markdown
from markdown.treeprocessors import Treeprocessor
from markdown import Extension
from markdown.util import etree
from copy import copy
import re


class FigureTreeprocessor(Treeprocessor):
    """ Figure Treeprocessor """

    RE_EOL = re.compile(r'  \r?\n')

    def __init__(self, md, figure_classes=None, img_classes=None, figcaption_classes=None,
                 multiline=True):
        Treeprocessor.__init__(self, md)
        self._figure_classes = figure_classes
        self._img_classes = img_classes
        self._figcaption_classes = figcaption_classes
        self._multiline = multiline

    def run(self, root):
        parent_map = {c: p for p in root.iter() for c in p}
        images = root.getiterator("img")
        for count, image in enumerate(images):
            caption = image.attrib["alt"]
            image.set("alt", caption)
            parent = parent_map[image]
            idx = list(parent).index(image)

            figure = etree.Element('figure')
            figcap = etree.Element('figcaption')

            if self._figure_classes is not None:
                figure.set("class", self._figure_classes)
            else:
                figure.set("class", "figure" + str(count + 1))

            if self._img_classes is not None:
                image.set("class", self._img_classes)

            if self._figcaption_classes is not None:
                figcap.set("class", self._figcaption_classes)

            figure.set("data-title", caption)
            figure.tail = copy(image.tail)
            parent.insert(idx, figure)
            parent.remove(image)
            image.tail = markdown.util.AtomicString("")
            figure.append(image)

            if self._multiline is True:
                for n, line in enumerate(self.RE_EOL.split(caption)):
                    if n == 0:
                        figcap.text = line
                    else:
                        br = etree.Element('br')
                        br.tail = line
                        figcap.append(br)
            else:
                figcap.text = caption
            figure.append(figcap)


class FigureExtension(Extension):
    """
    LightboxImagesExtension
    Extension class for markdown
    """
    def __init__(self, **kwargs):
        self.config = {
            'figure_classes': [None, "Class attributes assigned to the <figure /> tag"],
            'img_classes': [None, "Class attributes assigned to the <img /> tag"],
            'figcaption_classes': [None, "Class attributes assigned to the <figcaption /> tag"],
            'multiline': [True, "Support line breaks in <figcaption /> tag"],
        }
        super(FigureExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md, md_globals):
        figures = FigureTreeprocessor(md,
                                      self.getConfig('figure_classes'),
                                      self.getConfig('img_classes'),
                                      self.getConfig('figcaption_classes'),
                                      self.getConfig('multiline'))
        md.treeprocessors.add("figure", figures, "_end")
        md.registerExtension(self)


def makeExtension(*args, **kwargs):
    """ Return extension. """
    return FigureExtension(*args, **kwargs)
