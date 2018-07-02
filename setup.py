import setuptools

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    name='hathitrust_api',
    version='0.1.0',
    author='Bo Marchman',
    url='https://github.com/rlmv/hathitrust-api',
    description='Python wrappers for the HathiTrust APIs',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['hathitrust_api'],
    install_requires=[
        'requests',
        'requests-oauthlib'
    ],
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)
