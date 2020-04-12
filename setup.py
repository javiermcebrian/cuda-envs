import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

long_description = (HERE / "README.md").read_text()
requirements = (HERE / "requirements.txt").read_text().splitlines()

setup(
    name='cudaenvs',
    version='0.0.1',
    scripts=['./scripts/cudaenvs'],
    author='javiermcebrian@gmail.com',
    description='CLI to manage CUDA Docker environments easily with experiment configurations.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/javiermcebrian/cuda-envs',
    license='public',
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6"
    ],
    keywords="CUDA Docker experiment",
    install_requires=requirements,
    packages=['cudaenvs'],
    include_package_data=True,
    test_suite='tests',
    zip_safe=False,
)
