#!/usr/bin/env python

# from distutils.core import setup
from setuptools import setup, find_packages

import re

VERSIONFILE="buddi/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(
    name='BuDDI',
    version=verstr,
    description='BuDDI: Bulk Deconvolution with Domain Invariance',
    author='Natalie R. Davidson',
    author_email='natalie.davidson@cuanschutz.edu',
    python_requires='>=3.7, <4',
    packages=find_packages(),
    install_requires=[
        "anndata",
        "ipywidgets",
        "matplotlib_inline",
        "matplotlib_venn",
        "matplotlib",
        "numpy-groupies",
        "numpy",
        "pandas",
        "pydeseq2",
        "scanpy",
        "scipy",
        "seaborn",
        "tensorflow-estimator",
        "tensorflow-io-gcs-filesystem",
        "tensorflow[and-cuda]",
        "tqdm",
        "umap-learn",
        "upsetplot",
    ]
)