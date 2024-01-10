# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import tawnydragon

# -- Project information -----------------------------------------------------

project = 'Tawnydragon'
copyright = 'Atlas of Living Australia'
author = 'Amanda Buyan, Atlas of Living Australia'

sys.path.insert(0,"../../tawnydragon/")

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx-prompt',
    'sphinxcontrib.programoutput',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosectionlabel',
    'sphinx_design'
]

autosectionlabel_prefix_document = True
napoleon_use_param = True

myst_enable_extensions = ["colon_fence"]

templates_path = ['_templates']
version = str(tawnydragon.__version__)
source_path = os.path.dirname(os.path.abspath(__file__))
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'

html_theme_options = {
	"navbar_align": "content",
	"github_url": "https://github.com/AtlasOfLivingAustralia/tawnydragon-python",
	"secondary_sidebar_items": ["page-toc"],
    "logo": {
		"image_light": "_static/logo/logo.png", # didn't have dir before
        "image_dark": "_static/logo/logo.png", 
	},
}

# was image_light
html_sidebars = {
	"index": [],
	"search": [],
    "**": ["sidebar-nav-bs"]
}

html_static_path = ['_static']

html_logo = "_static/logo/logo.png"

# html_favicon = '_static/logo/favicon.ico'

html_css_files = ['css/extra.css']

html_style = 'css/extra.css'