from os.path import join
from pythonforandroid.recipe import Recipe, current_directory, shprint
import shutil, sh

class LeptonicaRecipe(Recipe):

    version='1.74.4'
    url = 'https://github.com/DanBloomberg/leptonica/archive/refs/tags/{version}.tar.gz'
    site_packages_name = 'leptonica'
    name = 'leptonica'

    built_libraries = {}

    def get_recipe_env(self, arch, **kwargs):
        env = super().get_recipe_env(arch, **kwargs)
        # modify env
        return env
    
    def build_arch(self, arch):
        super().build_arch(arch)
        env = self.get_recipe_env()
        
        with current_directory(self.get_build_dir(arch.arch)):
            shprint(sh.Command('./autobuild'),_env=env)
            shprint(
                sh.Command('./configure'),
                '--host=' + arch.command_prefix,
                '--disable-programs',
                '--without-giflib',
                '--without-libwebp',
                '--without-zlib',
                '--without-libopenjpeg',
                f'--prefix {self.get_build_dir(arch.arch)}',
                _env=env
            )
            shprint(sh.make, '-j', _env=env)
            shprint(sh.make, 'install', _env=env)


recipe = LeptonicaRecipe()