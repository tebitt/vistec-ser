import setuptools

requirements = [
    "chardet",
    "cython",
    "torch",
    "torchvision",
    "torchtext",
    "torchaudio",
    "pytorch-lightning",
    "pandas",
    "numpy",
    "soundfile",
    "PyYAML",
    "wget",
    "fastapi",
    "aiofiles",
    "python-multipart",
    "uvicorn",
]

setuptools.setup(
    name="vistec-ser",
    version="0.4.6a3",
    author="Chompakorn Chaksangchaichot",
    author_email="chompakorn.cc@gmail.com",
    description="Speech Emotion Recognition models and training using PyTorch",
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/tann9949/vistec-ser',
    packages=setuptools.find_packages(include=['vistec_ser*']),
    install_requires=requirements,
    classifiers=[
        # "2 - Pre-Alpha", "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.6',
    ],
    python_requires='>=3.6'
)
