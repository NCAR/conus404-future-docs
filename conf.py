git clone --depth 1 https://github.com/NCAR/conus404-future-docs .
git fetch origin --force --prune --prune-tags --depth 50
cat .readthedocs.yaml
asdf global python 3.13.3
python -mvirtualenv $READTHEDOCS_VIRTUALENV_PATH
python -m pip install --upgrade --no-cache-dir pip setuptools
python -m pip install --upgrade --no-cache-dir sphinx
