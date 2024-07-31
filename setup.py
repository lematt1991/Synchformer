from setuptools import find_packages, setup
from glob import glob
import os

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
    package_data={
        "syncformer.model.modules.feat_extractors.visual.motionformer_src": [
            os.path.basename(f)
            for f in glob("syncformer/model/modules/feat_extractors/visual/motionformer_src/*.yaml")
        ]
    },
    include_package_data=True,
    setup_requires=["wheel"],
)
