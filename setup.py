from setuptools import setup, find_packages, find_namespace_packages

try:
    with open("README.md") as fh:
        long_description = fh.read()
except:
    long_description = ""

setup(
    name='django-auditlog2',
    version='0.5.0',
    packages=find_packages(where="src", exclude=['*tests*', 'src']),
    package_dir={"": "src"},
    url='https://github.com/Canned-Django/django-auditlog',
    license='MIT',
    author='Andreas Hasenkopf',
    author_email='andi@hasenkopf2000.net',
    description='Audit log app for Django',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'django-jsonfield',
        'python-dateutil'
    ],
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
    ],        
)
