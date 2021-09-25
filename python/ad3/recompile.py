from setuptools import setup

from Cython.Build import cythonize

setup(ext_modules=cythonize("python/ad3/factor_graph.pyx"))
