from racks import __version__

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

dependencies = ['docopt', 'termcolor']


def publish():
    os.system("python setup.py sdist upload")

if sys.argv[-1] == "publish":
    publish()
    sys.exit()

setup(
    name='racks',
    version=".".join(str(x) for x in __version__),
    description='racks for stack graphs',
    long_description=open('README.rst').read(),
    url='http://www.github.com/myusuf3/racks',
    license="MIT License",
    author='Mahdi Yusuf',
    author_email='yusuf.mahdi@gmail.com',
    install_requires=dependencies,
    packages=['racks', ],
    entry_points={
        'console_scripts': [
            'racks=racks.main:start'
        ],
    },
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)
