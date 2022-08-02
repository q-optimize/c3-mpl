from setuptools import setup

setup(
    name="c3-matplotlib",
    version="1.0",
    description="Plotting for the C3 toolset",
    url="http://www.q-optimize.org",
    author="q-optimize",
    author_email="c3@q-optimize.org",
    include_package_data=True,
    packages=[
        "c3_matplotlib",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Science/Research",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=["c3-toolset>=1.3", "matplotlib>=3.5.1"],
    python_requires="~=3.7",
)
