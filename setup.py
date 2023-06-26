# -*- coding: utf-8 -*-

import setuptools
from stocky.version import PLUGIN_VERSION


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setuptools.setup(
    name="stock listing",
    version=PLUGIN_VERSION,
    author="Christoph Metzner",
    author_email="a@a.de",
    description="List all items of an stock location",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords="inventree stock",
    url="",
    license="MIT",
    packages=setuptools.find_packages(),
    setup_requires=[
        "wheel",
        "twine",
    ],
    python_requires=">=3.6",
    entry_points={
        "inventree_plugins": [
            "StockListing = stocky.stocky:StockListing"
        ]
    },
    include_package_data=True,
)
