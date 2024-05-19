from distutils.core import setup

setup(name='PassGen',
      version='1.0',
      description='Simple password generation utilities',
      author='Xenia',
      packages=['passgen'],
      test_suite="nose.collector",
      tests_require=["nose"]
     )
