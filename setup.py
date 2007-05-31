from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='python-gettext',
      version=version,
      description="Python Gettext implementation.",
      long_description="""\
This implementation of Gettext for Python includes a Msgfmt class which can be
used to generate compiled mo files from Gettext po files and includes support
for the newer msgctxt keyword.
""",
      classifiers=[],
      keywords='Python Gettext Msgctxt',
      author='Hanno Schlichting',
      author_email='hanno@hannosch.info',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'tests']),
      include_package_data=True,
      zip_safe=False,
      )
