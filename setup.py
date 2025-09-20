from setuptools import setup, find_packages


setup(
    name="qcn",
    version="0.1.0",
    description="Quick Commit Note - interactive commit message CLI",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=[
    "click>=8.0",
    "toml>=0.10"
    ],
    entry_points={
    "console_scripts": [
    "qcn=qcn.cli:main",
    ]
    },
    python_requires=">=3.8",
)