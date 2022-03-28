import setuptools

setuptools.setup(
    name="propose",
    version="0.0.1",
    author="Ian Covert",
    author_email="icovert@cs.washington.edu",
    description="Gene probe selection for spatial transcriptomics",
    long_description="""
        Predictive and robust probe selection (PROPOSE) is an approach for
        selecting a small number of gene probes for a FISH study.
    """,
    long_description_content_type="text/markdown",
    url="",
    packages=['propose'],
    install_requires=[
        'numpy',
        'torch',
        'tqdm'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering"
    ],
    python_requires='>=3.6',
)
