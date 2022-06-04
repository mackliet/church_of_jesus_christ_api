import pathlib
from setuptools import setup, find_packages
from church_of_jesus_christ_api.__version__ import __version__

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / 'README.rst').read_text()

# This call to setup() does all the work
setup(
    name='church_of_jesus_christ_api',
    version=__version__,
    description='Get data from churchofjesuschrist.org',
    long_description=README,
    long_description_content_type='text/x-rst',
    author='Michael Mackliet',
    author_email='michael@mackliet.com',
    url='https://github.com/mackliet/church_of_jesus_christ_api',
    project_urls={
        "Documentation": "https://church-of-jesus-christ-api.readthedocs.io/en/latest/index.html",
    },
    include_package_data=True,
    packages=find_packages(),
    install_requires=['requests'],
    extras={
        'documentation': ['sphinx', 'sphinx_rtd_theme']
    }
)