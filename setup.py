from setuptools import setup

setup(
    name="flatly",
    install_requires=[
        "pyramid",
    ],
    entry_points = """\
    [pyramid.scaffold]
    flatly=flatly:FlatProjectTemplate
    """
)
