from os.path import join
from pythonforandroid.recipe import Recipe, current_directory, shprint
import shutil, sh

# use BAD to build tesseract libraries
# WARNING: requires docker to be installed in host

class TesseractOCRRecipe(Recipe):

    version=''
    url = ''
    site_packages_name = 'tesseract-ocr'
    name = 'tesseract-ocr'
    
    depends = ['jpeg', 'png', 'tiff', 'leptonica']
    
    built_libraries = {}

    def get_recipe_env(self, arch, **kwargs):
        env = super().get_recipe_env(arch, **kwargs)
        
        
        env['API'] = '23'
        env['TOOLCHAIN'] = '$ANDROID_NDK_HOME_22/toolchains/llvm/prebuilt/linux-x86_64'
        env['ABI_CONFIGURE_HOST'] = '$NDKTARGET'
        env['AR'] = '$TOOLCHAIN/bin/$NDKTARGET-ar'
        env['CC'] = '$TOOLCHAIN/bin/$TARGET$API-clang'
        env['CXX'] = '$TOOLCHAIN/bin/$TARGET$API-clang++'
        env['AS'] = '$CC'
        env['LD'] = '$TOOLCHAIN/bin/$TARGET-ld'
        env['RANLIB'] = '$TOOLCHAIN/bin/$TARGET-ranlib'
        env['STRIP'] = '$TOOLCHAIN/bin/$NDKTARGET-strip'
        env['LEPTONICA_LIBS'] = '-L$ROOT/output/$OUTARCH/lib -llept'
        env['LEPTONICA_CFLAGS'] = '-I$ROOT/output/$OUTARCH/include/leptonica'
        env['PKG_CONFIG_PATH'] = '$ROOT/output/$OUTARCH/lib/pkgconfig'
        env['LIBS'] = '-L$ROOT/output/$OUTARCH/lib'
        
        return env
    
    def build_arch(self, arch):
        super().build_arch(arch)
        env = self.get_recipe_env()
        
        with current_directory(self.get_build_dir(arch.arch)):
            shprint(sh.make, 'clean', _env=env)
            shprint(sh.Command('./autogen.sh'), _env=env)
            shprint(
                sh.Command('./configure'),
                '--host=$TARGET',
                '--disable-doc',
                '--without-archive',
                '--disable-openmp',
                '--without-curl',
                '--prefix $ROOT/output/$OUTARCH',
                _env=env
            )
            shprint(sh.make, '-j', _env=env)
            shprint(sh.make, 'install', _env=env)


recipe = TesseractOCRRecipe()