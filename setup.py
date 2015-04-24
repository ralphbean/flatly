from setuptools import setup, find_packages

f = open('README.rst')
long_description = f.read().strip()
long_description = long_description.split('split here', 1)[1]
f.close()


setup(
    name="flatly",
    version='0.3',
    description="Pyramid scaffold that is flat.  Kind of like Flask.",
    long_description=long_description,
    author='Ralph Bean',
    author_email='rbean@redhat.com',
    url='http://github.com/ralphbean/flatly/',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pyramid",
    ],
    keywords="pyramid",
    entry_points="""\
    [pyramid.scaffold]
    flatly=flatly:FlatProjectTemplate
    """
)
