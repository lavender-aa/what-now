from os.path import join
from pythonforandroid.recipe import Recipe, current_directory, shprint
import shutil, sh

# use BAD to build tesseract libraries
# WARNING: requires docker to be installed in host

class PyTesseractRecipe(Recipe):

    version=''
    url = ''
    site_packages_name = 'pytesseract'
    name = 'pytesseract'
    
    depends = ['tesseract-ocr']
    # built_libraries = [''] TODO: test, add
    hostpython_prerequisites = ["setuptools>=77"]

    def get_recipe_env(self, arch, **kwargs):
        env = super().get_recipe_env(arch, **kwargs)
        # modify env
        return env
    
    def build_arch(self, arch):
        super().build_arch(arch)
        # env = self.get_recipe_env()
        
        with current_directory(self.get_build_dir(arch.arch)):
            pass


recipe = PyTesseractRecipe()