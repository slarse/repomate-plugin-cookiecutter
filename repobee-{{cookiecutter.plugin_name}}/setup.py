import re
from setuptools import setup, find_packages

with open("README.md", mode="r", encoding="utf-8") as f:
    readme = f.read()

# parse the version instead of importing it to avoid dependency-related crashes
with open(
    "repobee_{{cookiecutter.plugin_name|replace('-', '_')}}/__version.py",
    mode="r",
    encoding="utf-8",
) as f:
    line = f.readline()
    __version__ = line.split("=")[1].strip(" '\"\n")
    assert re.match(r"^\d+(\.\d+){2}(-(alpha|beta|rc)(\.\d+)?)?$", __version__)

test_requirements = ["pytest", "repobee"]
required = ["repobee-plug"]

setup(
    name="repobee-{{cookiecutter.plugin_name}}",
    version=__version__,
    description="{{cookiecutter.short_description}}",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.email}}",
    url="https://github.com/"
    "{{cookiecutter.github_username}}"
    "/repobee-{{cookiecutter.plugin_name}}",
    download_url="https://github.com/"
    "{{cookiecutter.github_username}}"
    "/repobee-{{cookiecutter.plugin_name}}"
    "/archive/v{}.tar.gz".format(__version__),
    license="MIT",
    packages=find_packages(exclude=("tests", "docs")),
    tests_require=test_requirements,
    install_requires=required,
    extras_require=dict(TEST=test_requirements),
    include_package_data=True,
    zip_safe=False,
)