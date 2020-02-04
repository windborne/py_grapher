from setuptools import setup

setup(
    name='py_grapher',
    version='0.1.0',
    description='Python wrapper for windborne graphing library',
    url='git@github.com:windborne/py_grapher.git',
    author='Kai Marshland',
    author_email='kai@windbornesystems.com',
    license='unlicense',
    packages=['py_grapher'],
    package_data={'py_grapher': ['index.html']},
    zip_safe=False
)
