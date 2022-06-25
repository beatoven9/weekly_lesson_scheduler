from setuptools import find_packages, setup

setup(
    name="pmp_scheduler",
    version="1.0.0",
    description="Scheduler for pmp",
    packages=find_packages(include=["pmp_scheduler", "pmp_scheduler.*"]),
    install_requires=[],
    extras_require={
        "dev": ["black==22.3.0", "isort==5.10.1", "mypy==0.950", "pytest==7.1.2"]
    },
)
