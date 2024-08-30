# from setuptools import setup, find_packages

# setup(
#     name='OnlineBankingApp',
#     version='0.1.0',
#     packages=find_packages(where='../'),  # Adjusting the location to include packages from the parent directory
#     package_dir={'': '../'},  # Telling setuptools to look for packages one directory above
#     scripts=[
#         'banking_app.py',
#         'performance_test.py'
#     ],
#     install_requires=[
#         # List of dependencies required
#         'bcrypt',  
#         'pytest',  
#     ],
#     entry_points={
#         'console_scripts': [
#             'run-banking-app = banking_app:main',  # This creates a command-line executable to run the app
#         ],
#     },
# )
