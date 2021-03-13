from setuptools import setup, find_packages
import codecs
import os

#here = os.path.abspath(os.path.dirname(__file__))

#with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
#    LONG_DESCRIPTION = fh.read()

VERSION = '0.0.5'
DESCRIPTION = 'Basic HTTP server package'
LONG_DESCRIPTION = '👩‍💻 Simple Python HTTP server'

# Setting up
setup(
    name="easyhttp",
    version=VERSION,
    author="luisbrandino (Luis Brandino)",
    author_email="<luisbrandino.contato@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'webserver', 'http', 'http server', 'sockets'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)