from os.path import join
from pythonforandroid.recipe import Recipe, current_directory, shprint
import shutil, sh

class TiffRecipe(Recipe):

    version='4.0.10'
    url = 'https://download.osgeo.org/libtiff/tiff-{version}.tar.gz'
    site_packages_name = 'tiff'
    name = 'tiff'

    # built_libraries = {'name.so' : 'path'}

    def get_recipe_env(self, arch, **kwargs):
        env = super().get_recipe_env(arch, **kwargs)
        # modify env
        return env
    
    def build_arch(self, arch):
        super().build_arch(arch)
        env = self.get_recipe_env()
        
        # necessary?
        with current_directory(self.get_build_dir(arch.arch)):
            shprint(sh.Command('./configure'), _env=env)
            shprint(sh.make, _env=env)


recipe = TiffRecipe()