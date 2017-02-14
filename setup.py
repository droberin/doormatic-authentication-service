from distutils.core import setup

setup(
    name='doormaticauthservice',
    version='1.0',
    packages=['doormatic', 'doormatic.authentication', 'doormatic.authentication.mongo'],
    url='https://github.com/droberin/doormatic-authentication-service',
    license='AGPL',
    author='Roberto Salgado',
    author_email='drober@gmail.com',
    description='Doormatic Authentication Service'
)
