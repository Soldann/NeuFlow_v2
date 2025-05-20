from distutils.core import setup

setup(name='NeuFlow_v2',
      version='1.0',
      description='Fast Optical Flow Algorithm',
      url='https://github.com/Soldann/NeuFlow_v2',
      packages=['NeuFlow', "NeuFlow.data_utils"],
      install_requires=[
        "torch",
        "huggingface_hub",
      ],
    )
# from setuptools import setup, find_packages

# setup(
#     name="NeuFlow",
#     version="0.1.0",
#     # author="Your Name",
#     # author_email="your.email@example.com",
#     description="Neuflow_v2",
#     long_description=open("README.md").read(),
#     long_description_content_type="text/markdown",
#     url="https://github.com/Soldann/NeuFlow_v2",
#     packages=find_packages(),
#     install_requires=[
#         "numpy",
#         "opencv-python",
#         # Add other dependencies here
#     ],
#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: Apache License 2.0",
#         "Operating System :: OS Independent",
#     ],
#     python_requires=">=3.6",
# )
