"""A setuptools based setup module.
"""

from setuptools import setup


__author__ = 'robodasha'
__email__ = 'damirah@live.com'


with open('README.md') as fp:
    description = fp.read()

setup(
    name='crossref_resolver',
    version='0.1',
    description='Resolve citations to DOIs using CrossRef API',
    long_description=description,
    license='MIT',
    url='https://github.com/robodasha/crossref_resolver',
    author='Drahomira Herrmannova',
    author_email='damirah@live.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development',
        'Topic :: Utilities'
    ],
    keywords='crossref doi citation',
    packages=['crossref_resolver'],
    install_requires=['wheel', 'configparser', 'ordereddict']
)
