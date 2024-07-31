from setuptools import find_packages, setup


setup(
    name="syncformer",
    version="0.0.1",
    packages=find_packages(
        exclude=[
            "build",
            "configs",
            "scripts",
            "_repo_assets"
        ]
    ),
    setup_requires=["wheel"],
)
