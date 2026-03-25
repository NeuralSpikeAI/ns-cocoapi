from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext
from Cython.Build import cythonize
import os


class build_ext_with_numpy(build_ext):
    def finalize_options(self):
        super().finalize_options()
        import numpy
        self.include_dirs.append(numpy.get_include())

base_dir = os.path.dirname(os.path.abspath(__file__))
common_dir = os.path.join(base_dir, "common")

extensions = [
    Extension(
        "pycocotools._mask",
        sources=[
#            os.path.join(common_dir, "maskApi.c"),
            os.path.join(base_dir, "pycocotools", "_mask.pyx"),
        ],
        include_dirs=[common_dir],
    )
]
setup(
    name='ns-pycocotools',
    packages=find_packages(),
    install_requires=[
        'setuptools>=18.0',
        'cython>=0.27.3',
        'matplotlib>=2.1.0',
        'loguru'
    ],
    version='2.3.1',
    cmdclass={"build_ext": build_ext_with_numpy},
    ext_modules= extensions
)
