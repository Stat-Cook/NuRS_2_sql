import setuptools

setuptools.setup(
    name='NURS2SQL',
    version='0.3',
    author='Robert Cook',
    description='',
    packages=['nurs_2_sql'],
    entry_points={
        'console_scripts': ['nurs2sql=nurs_2_sql.cli:nurs_2_sql',
                            'nurs_bulk_insert=nurs_2_sql.cli:bulk_insert_cli'],
    },
    install_requires=[
        'setuptools',
        'pandas >= 1.4.3',
        'numpy >= 1.16.0',
        "sqlalchemy"
    ],
    python_requires='>=3.5'
)
