from setuptools import setup, find_packages
import src


long_description = """
`doit` is a task management & automation tool
`doit` comes from the idea of bringing the power of build-tools
to execute any kind of **task**
`doit` is a modern open-source build-tool written in python
designed to be simple to use and flexible to deal with complex work-flows.
It is specially suitable for building and managing custom work-flows where
there is no out-of-the-box solution available.
`doit` has been successfully used on: systems test/integration automation,
scientific computational pipelines, content generation,
configuration management, etc.
`website/docs <http://pydoit.org>`_
"""


setup(
    name='swissarmyknife',
    version='0.0.1',
    author='avimehenwal',
    author_email='avi.mehanwal@gmail.com',
    license='BSD',
    description='remove watermark',
    long_description = long_description,
    project_urls = {
        'Documentation': 'https://pydoit.org/',
        'Source': 'https://github.com/pydoit/doit/',
        'Tracker': 'https://github.com/pydoit/doit/issues',
    },

    packages=find_packages(),
    python_requires='>=3.4',
    install_requires=[
        'doit',
        'click',
    ],

    keywords='remove watermark',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: BSD License'
    ],

    extras_require={
        ':sys.platform == "darwin"': ['macfsevents'],
        ':sys.platform == "linux"': ['pyinotify'],
    },
    entry_points = {
        'console_scripts': [
            'doit = doit.__main__:main'
        ]
    },
)
