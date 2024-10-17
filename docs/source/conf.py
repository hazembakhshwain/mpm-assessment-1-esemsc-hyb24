import os
import sys
sys.path.insert(0, os.path.abspath('../../acsefunctions'))
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'acsefunctions'
copyright = '2024, Hazem Bakhshwain'
author = 'Hazem Bakhshwain'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']



extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # For Google or NumPy style docstrings
    'sphinx.ext.viewcode',
]

# Add this section at the bottom of your conf.py
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'classoptions': ',oneside',  # Use oneside to reduce blank pages
    'babel': r'\usepackage[english]{babel}',  # Ensure consistent language settings
}

latex_documents = [
    ('index', 'ACSEFunctions.tex', 'ACSEFunctions Documentation',
     'Hazem Bakhshwain', 'manual'),
]
