from setuptools import setup


setup(
    name="MWParser",
    version="0.1.8",
    license="MIT",
    author="MMK_group",
    author_email="maciekgoncerzewicz@gmail.com",
    packages=["MWParser"],
    package_dir={"": "./"},
    url="https://github.com/gmyrianthous/example-publish-pypi",
    keywords="example project",
    install_requires=[
        "bs4",
        "requests",
    ],
)
