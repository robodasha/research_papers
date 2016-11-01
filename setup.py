"""A setuptools based setup module.
"""

from setuptools import setup


__author__ = 'robodasha'
__email__ = 'damirah@live.com'


with open('README.md') as fp:
    description = fp.read()

setup(
    name='research_papers',
    version='0.1.1',
    description='Numerous tools for working with research papers',
    long_description=description,
    license='MIT',
    url='https://github.com/robodasha/research_papers',
    author='Drahomira Herrmannova',
    author_email='damirah@live.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering',
        'Topic :: Text Processing',
        'Topic :: Utilities'
    ],
    keywords='text mining',
    packages=['research_papers'],
    install_requires=['wheel', 'configparser', 'ordereddict', 'mendeley',
                      'pdfminer3k']
)
