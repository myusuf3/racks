from racks import __version__

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

dependencies = ['docopt', 'termcolor']


setup(
    name='racks',
    version=".".join(str(x) for x in __version__),
    description='rack on rack for stack graphs',
    url='http://www.github.com/myusuf3/racks',
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
