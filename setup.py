from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('MIT-LICENSE.txt') as f:
    license = f.read()

setup(
    name='DSAE_PBHL',
    version='1.2.0',
    description='Package of the sparse autoencoder (SAE), deep SAE (DASE), SAE with parametric bias in hidden layer (SAE with PBHL), and DSAE with PBHL',
    long_description=readme,
    author='Ryo Ozaki',
    author_email='ryo.ozaki@em.ci.ritsumei.ac.jp',
    url='https://github.com/RyoOzaki/SparseAutoencoder',
    license=license,
    install_requires=['numpy', 'tensorflow==2.5.0'],
    packages=['DSAE_PBHL','DSAE_PBHL.util']
)
