from setuptools import setup

setup(
    name='attr',
    version='0.3.1',
    description='Simple decorator to set attributes of target function or class in a DRY way.',
    long_description='''

Usage example::

    # Django proposes:
    def my_calculated_field(...
    my_calculated_field.short_description = 'Field'
    my_calculated_field.admin_order_field = 'real_field'

    # DRY:
    @attr(short_description='Field', admin_order_field='real_field')
    def my_calculated_field(...

Get it::

    sudo pip install attr
    from attr import attr

New popular `attrs.org <http://attrs.org>`_ used by `pytest.org <https://pytest.org>`_ defines another "attr" package that shadows this "attr" module.

Please use "dry_attr" alias to unshadow it::

    from dry_attr import attr
    from dry_attr import dry_attr

''',
    url='https://github.com/denis-ryzhkov/attr',
    author='Denis Ryzhkov',
    author_email='denisr@denisr.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    py_modules=['attr', 'dry_attr'],
)
