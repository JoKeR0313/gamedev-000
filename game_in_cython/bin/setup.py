from distutils.core import setup
from setuptools import Extension
from Cython.Build import cythonize


setup(
    ext_modules = cythonize([
        Extension("*", ["bin/*.pyx"])
    ])
)
