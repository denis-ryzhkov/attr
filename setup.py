from distutils.core import setup

setup(
    name='attr',
    version='0.1.0',
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
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    py_modules=['attr'],
)
