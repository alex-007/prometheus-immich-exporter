from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

version = '1.4.0'

setup(
    name='prometheus-immich-exporter',
    packages=['immich_exporter'],
    version=version,
    long_description=long_description,
    long_description_content_type="text/markdown",
    description='Prometheus exporter for immich',
   # forked from:
   # author='Esteban Sanchez',
   # author_email='esteban.sanchez@gmail.com',
   # url='https://github.com/esanchezm/prometheus-qbittorrent-exporter',
   # download_url='https://github.com/esanchezm/prometheus-qbittorrent-exporter/archive/1.1.0.tar.gz',
    keywords=['prometheus', 'immich'],
    classifiers=[],
    python_requires='>=3',
    install_requires=['attrdict==2.0.1', 'prometheus_client==0.19.0 ', 'requests==2.31.0', 'python-json-logger==2.0.7', 'psutil==5.9.8'],
    entry_points={
        'console_scripts': [
            'immich_exporter=immich_exporter.exporter:main',
        ]
    }
)
