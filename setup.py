import os, sys
from setuptools import setup, find_packages

setup(
    name = 'gnebehay_parser',
    version = '1.0',
    #
    ## following advice on find_packages excluding tests from https://setuptools.readthedocs.io/en/latest/setuptools.html#using-find-packages
    packages = find_packages( exclude = ["*.tests", "*.tests.*", "tests" ] ),
    url = 'https://github.com/tanimislam/gnebehay_parser',
    license = 'BSD-2-Clause',
    author = 'Tanim Islam',
    author_email = 'tanim.islam@gmail.com',
    description = "Offshoot of Georg Nebehay's arithmetic parser, with enhancements",
    #
    ## classification: where in package space does "iv_tanim live"?
    ## follow (poorly) advice I infer from https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-setup-script
    classifiers=[
    # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
      'Development Status :: 5 - Production/Stable',
      'Intended Audience :: End Users/Desktop',
      'License :: OSI Approved :: BSD License',
      'Operating System :: POSIX',
      'Environment :: Console',
      'Programming Language :: Python :: 3',
    # uncomment if you test on these interpreters:
    # 'Programming Language :: Python :: Implementation :: IronPython',
    # 'Programming Language :: Python :: Implementation :: Jython',
    # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
    ],
    #
    ## requirements
    # install_requires = reqs,
    python_requires = '>=3.7',
    #
    ## the executables I am creating
    entry_points = {
        'console_scripts' : [
            #
            ## CLI stuff
            "gnebehay_compute  = gnebehay_parser.cli.compute:main",
            "gnebehay_graphviz = gnebehay_parser.cli.graphviz:main",
        ]
    },
    #
    ## big fatass WTF because setuptools is unclear about whether I can give a directory that can then be resolved by
    ## other resources
    ## here is the link to the terrible undocumented documentation: https://setuptools.readthedocs.io/en/latest/setuptools.html#including-data-files
    #package_data = {
    #    "ive_tanim" : [
    #        "resources/*.json",
    #        ],
    #}
)
