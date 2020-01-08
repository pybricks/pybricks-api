

### Prerequisites

* Git
* Python 3
* Pipenv

For docs:
* Inkscape
* Make


### Setup

    git clone --recursive https://github.com/pybricks/pybricks-api
    cd pybricks-api
    pipenv sync --dev


### Build Docs

    pipenv shell
    make -C doc html
