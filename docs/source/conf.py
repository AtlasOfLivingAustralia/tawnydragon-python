# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'tawnydragon-python'
copyright = '2024, Amanda Buyan'
author = 'Amanda Buyan'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser',
              'sphinx-prompt',
              'sphinxcontrib.programoutput',
              'sphinx.ext.napoleon',
              'sphinx.ext.autosectionlabel',
              'sphinx_panels'
              ]

templates_path = ['_templates']
exclude_patterns = []

autosectionlabel_prefix_document = True

myst_enable_extensions = ["colon_fence"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
