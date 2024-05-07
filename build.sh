pip install setuptools wheel
python setup.py clean
rm -rf src/*.egg-info
rm -rf build
rm -rf dist
python setup.py sdist bdist_wheel
