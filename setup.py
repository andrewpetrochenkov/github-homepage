import setuptools

setuptools.setup(
    name='github-homepage',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/github-homepage']
)
