from setuptools import setup

setup(
    name="seed",
    description="",
    version=1.0,
    author="Ted Callahan",
    author_email="",
    license="MIT",
    package_dir={'': 'src'},
    py_modules=["main"],
    install_requires=[],
    extras_require={"test": ["pytest", "pytest-watch", "pytest-cov", "tox"]},
    entry_points={}
)