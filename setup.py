import setuptools

setuptools.setup(
        name = 'reguligilo',
        version = '0.1.0',
        packages = setuptools.find_packages(),
        install_requires=[
                'tqdm',
                'sentencepiece',
                'pyyaml',
            ],
        entry_points = {
            'console_scripts':[
                'reguligilo = reguligilo.main:encode',
                'ambireguligilo = reguligilo.main:ambiencode',
                'malreguligilo = reguligilo.main:decode',
                ]},)

