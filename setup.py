import pathlib
from setuptools import setup

# Set __version__ without importing anything and causing issues at package build time
with open("church_of_jesus_christ_api/__version__.py") as version_file:
    exec(version_file.read())

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README").read_text()

# This call to setup() does all the work
setup(
    name="church_of_jesus_christ_api",
    version=__version__,
    description="Decommisioned package",
    long_description=README,
    long_description_content_type="text/plain",
    author="Michael Mackliet",
    author_email="michael@mackliet.com",
    url="https://github.com/mackliet/church_of_jesus_christ_api",
    package_data={
        "church_of_jesus_christ_api": ["README"]
    }
)
