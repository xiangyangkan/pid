# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------

project = 'pid'
copyright = '2019, xiangyangkan'
author = 'xiangyangkan'
release = '0.0.2'
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'm2r',
]
templates_path = ['_templates']
source_suffix = ['.rst', '.md']
language = 'zh_CN'
exclude_patterns = []
pygments_style = 'sphinx'
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Extension configuration -------------------------------------------------


def autodoc_skip_member(app, what, name, obj, skip, options):
    # include __init__ and __call__ in docs
    if name in ('__init__', '__call__'):
        return False
    return skip


def setup(app):
    app.connect('autodoc-skip-member', autodoc_skip_member)
