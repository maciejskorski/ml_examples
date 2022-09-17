"""Sphinx configuration."""

from cgitb import enable
import os
import sys

# General information about the project.
project = "ML Code Examples"
author = "Maciej Skorski"
copyright = "2018-2022, Maciej Skorski"

# Sources
source_suffix = ['.md','.rst','.ipynb']
master_doc = 'index'

# Sphinx Extensions
extensions = [
    "myst_nb",
    "sphinxcontrib.bibtex",
]
bibtex_bibfiles = ['citations.bib']

# html styles
html_theme = "sphinx_book_theme"
html_theme_options = {
    "repository_url": "https://github.com/maciejskorski/ml_examples/",
    "repository_branch": "master",
    "path_to_docs": "",
}

nb_execution_mode = "off"