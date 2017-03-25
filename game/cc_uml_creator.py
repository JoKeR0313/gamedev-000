import os
import datetime
import apt
from cc_logger import ccLogger


class ccUmlCreator:

    @staticmethod
    def package_check():
        cache = apt.Cache()
        if cache['pylint'].is_installed and cache['graphviz'].is_installed:
            ccLogger.trace('Packages for UML creation are installed. Creating UML images.')
            return True
        else:
            ccLogger.error('Required packages not installed. Please execute the following: '
                           'sudo apt-get install pylint, sudo apt-get install graphviz')
            return False

    @staticmethod
    def create_uml():
        if not os.path.exists('docs/uml'):
            os.makedirs('docs/uml')
        open('__init__.py', 'a').close()
        date = datetime.datetime.now().strftime('%Y_%m_%d_%H_%m_%S')
        os.system('pyreverse -o png -p '+date+' .')
        os.rename('classes_'+date+'.png', 'docs/uml/classes_'+date+'.png')
        os.rename('packages_'+date+'.png', 'docs/uml/packages_'+date+'.png')
        os.remove('__init__.py')

    @classmethod
    def run(cls):
        if cls.package_check():
            cls.create_uml()
        else:
            quit()

if __name__ == '__main__':
    ccUmlCreator.run()
