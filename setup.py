# installation: pip install binary_heap

from setuptools import setup


setup(
    name='d_heap',
    version='0.0.1',
    description='Python functions for working with D-ary Heap '
    '(Heap with more than 2 child nodes)',
    keywords='d-heap heap python-heap min-heap max-heap',
    long_description=open('README.rst').read(),

    author='Ramesh RV',
    author_email='rameshrvr@outlook.com',
    url='https://github.com/rameshrvr/d-ary_heap',

    platforms=['All'],
    license='MIT License',

    packages=['d_heap'],

    classifiers=[
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)

# setup keyword args: http://peak.telecommunity.com/DevCenter/setuptools

# built and uploaded to pypi with this:
# python setup.py sdist bdist_egg register upload
