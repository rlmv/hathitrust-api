#!/usr/bin/env python

from distutils.core import setup

setup(name='hathitrust_api', 
      url='github.com/rlmv/hathitrust-api',
      description='Python wrappers for the HathiTrust APIs',
      author='Robert Marchman', 
      packages=['hathitrust_api'],
      install_requires=['requests', 'requests-oauthlib']
      )
