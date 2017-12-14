"""Open source dataset of all known ammunition cartridges."""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
		name='cartridges',

		version='1.0.1',

		description='',
		long_description=long_description,

		url='https://gitlab.com/ammolytics/cartridges',

		author='Eric Higgins',
		author_email='erichiggins@gmail.com',

		license='MIT',

		classifiers=[
		],

		keywords='',

		packages=find_packages(exclude=['contrib', 'docs', 'tests']),

		install_requires=[],

		extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

		package_data={
		},

		data_files=[],

		entry_points={
		},
)
