from setuptools import setup, find_packages
import os

version = '1.0dev0'
long_description = \
    open("README.txt").read() + "\n" + \
    open(os.path.join("docs", "HISTORY.txt")).read()

setup(name='oira.website',
      version=version,
      description="EU-OSHA OiRA Website",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Programming Language :: Python",
      ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['oira'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            'setuptools',
            'plone.api',
            'plone.app.dexterity [grok]',
            'z3c.jbot',
            'Products.LoginLockout',
            'Products.PasswordStrength',
            'collective.responsivetheme',
            'collective.z3cform.datagridfield'
      ],
      extras_require={
          # list libs needed for testing this project
          'test': [
              'mock',
              'plone.app.testing',
              'unittest2',
          ]
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
