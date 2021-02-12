from setuptools import setup
import setuptools

setup(
    name='GradMatch',
    version='0.0.1',
    author='',
    author_email='',
    #packages=['GradMatch', 'GradMatch/selectionstrategies', 'GradMatch/utils'],
    url='https://anonymous.4open.science/repository/2eada7f6-5514-4409-8d90-ff4f8d7d5c03/',
    license='LICENSE.txt',
    packages=setuptools.find_packages(),
    description='GradMatch is a package for data subset selection for efficient and robust machine learning.',
    install_requires=[
        "numpy >= 1.14.2",
        "scipy >= 1.0.0",
        "numba >= 0.43.0",
        "tqdm >= 4.24.0",
        "torch >= 1.4.0",
        "apricot-select >= 0.6.0",
        "sphinxcontrib-napoleon",
        "sphinxcontrib-bibtex",
        "sphinx-rtd-theme",
        "scikit-learn",
        "torchvision >= 0.5.0",
        "matplotlib"
    ],
)
