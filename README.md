![Python Versions](https://img.shields.io/badge/python-3.9-blue) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://www.gnu.org/licenses/agpl-3.0) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/MarcSkovMadsen/panel-vegafusion/HEAD?urlpath=lab) [![Follow on Twitter](https://img.shields.io/twitter/follow/MarcSkovMadsen.svg?style=social)](https://twitter.com/MarcSkovMadsen)

# An Introduction to dataviz in Python

This repository contains an introduction to dataviz in Python with a focus on browser based, interactive dataviz.

## Installation

```bash
git clone https://github.com/MarcSkovMadsen/dataviz-in-python.git
python -m venv .venv
source .venv/Scripts/activate
pip install -e .[all]
```

### Serve the presentation

```bash
panel serve src/dataviz_in_python/presentation/*.py
```

You view the presentation at [http://localhost:5006/introduction](http://localhost:5006/introduction).
