#! /usr/bin/env python


from setuptools import setup
setup(
    name='markdown-figure',
    version='0.0.1',
    author='Jan Willhaus',
    author_email='mail@janwillhaus.de',
    description='Markdown extension which turns images into figures',
    url='https://github.com/janwh/markdown-figures',
    py_modules=['mdfigure'],
    install_requires=['Markdown>=2.0'],
    classifiers=[
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
