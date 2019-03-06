from rest_api_test.__version__ import version
from sys import version_info


if version_info < (2, 7):
    from distutils.core import setup
    import sys
    print("Please use a newer version of python")
    sys.exit(1)


if version_info > (2, 7):
    try:
        from setuptools import setup, find_packages
    except ImportError:
        try:
                from distutils.core import setup
        except ImportError:
                from ez_setup import use_setuptools
                use_setuptools()
                from setuptools import setup, find_packages


from setuptools.command.test import test as TestCommand
import sys


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ""

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        try:
            # import here, because outside the eggs aren't loaded
            import pytest
        except ImportError:
            raise RuntimeError("py.test is not installed, "
                               "run: pip install pytest")
        errno = pytest.main([self.pytest_args])
        sys.exit(errno)


setup_args = {
    'name': 'rest-api-test',
    'version': version,
    'description': "learning python",
    'long_description': """learning python""",
    'author': "T Wiesenthal",
    'author_email': "tobias.wiesenthal@googlemail.com",
    'license': 'Copyright Tobias Wiesenthal',
    'install_requires': [
        'sqlalchemy'
        ],
    'url': 'https://github.com/twiesenthal/restApiTest.git',
    'packages': ['rest_api_test'],
    'classifiers': [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research'
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        ],

    'scripts': ['rest-api-test'],
    'tests_require': [
        'coverage >= 3.0',
        'pytest >=2.1.3',
        'mock >=1.0b1',
        ],
    "cmdclass": {'test': PyTest},
}

setup(**setup_args)
