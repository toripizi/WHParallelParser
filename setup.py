from setuptools import setup


setup(
    name="WHParallelParser",
    version="0.2.0",
    license="MIT",
    author="MMK_group",
    author_email="maciekgoncerzewicz@gmail.com",
    packages=["WHParallelParser"],
    package_dir={"": "./"},
    url="https://github.com/gmyrianthous/example-publish-pypi",
    keywords="example project",
    install_requires=[
        "bs4",
        "requests",
    ],
)
