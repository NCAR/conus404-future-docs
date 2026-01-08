# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'c404-future-docs'
copyright = '2026, Erin Dougherty, Yongxin Zhang, Ryan Cabell'
author = 'Erin Dougherty, Yongxin Zhang, Ryan Cabell'
release = 'v1.0'

try:
    import sphinx_rtd_theme
    extensions = [
        'sphinx_rtd_theme',
    ]
    # html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    html_theme = 'sphinx_rtd_theme'
    html_theme_options = {
        'navigation_depth': -1
    }
except:
    print("Warning: sphinx_rtd_theme not installed, using default theme")
    pass
html_static_path = ['_static']
html_css_files = ['ug_theme.css']
numfig_secnum_depth = 2

#these are enforced by rstdoc, but keep them for sphinx-build
numfig = 0
smartquotes = 0
source_suffix = '.rest'
templates_path = []
language = 'en'
highlight_language = "none"
default_role = 'math'
pygments_style = 'sphinx'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
master_doc = 'index'
