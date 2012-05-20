from setuptools import find_packages
from setuptools import setup


setup(
    name='parone.theme',
    version='0.7',
    description="Parone Theme",
    long_description="",
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Programming Language :: Python",
    ],
    keywords='',
    author='Taito Horiuchi',
    author_email='taito.horiuchi@abita.fi',
    url='http://paronedesign.com/',
    license='Non-free',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['parone'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
