# Project information
project = 'pythonaibrain'
author = 'Divyanshu Sinha'
version = '1.0'
release = '1.0.8'

# Extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
]

# Source and build directories
source_suffix = '.rst'
master_doc = 'index'

# Theme
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'style': 'default',
}

# Static files
html_static_path = ['_static']

# Autodoc settings
autodoc_default_options = {
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
}
