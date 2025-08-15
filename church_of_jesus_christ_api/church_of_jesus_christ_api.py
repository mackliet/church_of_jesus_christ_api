import importlib.resources

with importlib.resources.open_text(__package__, "README") as readme:
    readme_contents = readme.read()

class ChurchOfJesusChristAPI(object):
    raise ImportError(readme_contents)