# docs/conf.py
project = "pythonaibrain"
author = "Divyanshu Sinha"
version = "1.1.8"
release = "1.1.8"

# Enable Sphinx extensions
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

# Support .rst and .md files
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# Theme
html_theme = "sphinx_rtd_theme"
