import os
import shutil
import stat


class Directory:
    """ Directory utils. """

    @staticmethod
    def create(directory):
        """
        Create a directory recursively.
        :param directory: directory to create
        """
        os.makedirs(directory)

    @staticmethod
    def touch(file):
        """
        'Touch' the specified file.
        :param file: file to create
        """
        # Create directory
        try:
            Directory.create(os.path.dirname(file))
        except FileExistsError:
            pass

        # Touch file
        open(file, 'a').close()

    @staticmethod
    def delete(directory):
        """
        Remove a directory.
        :param directory:
        """
        try:
            shutil.rmtree(directory)
        except FileNotFoundError:
            pass

    @staticmethod
    def copy(src, dst, symlinks=False, ignore=None):
        """
        Copy a directory recursively.
        :param src: source directory
        :param dst: destination directory
        :param symlinks: follow symlinks ?
        :param ignore: ignore files list
        """
        if not os.path.exists(dst):
            os.makedirs(dst)
            shutil.copystat(src, dst)
        lst = os.listdir(src)
        if ignore:
            excl = ignore(src, lst)
            lst = [x for x in lst if x not in excl]
        for item in lst:
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if symlinks and os.path.islink(s):
                if os.path.lexists(d):
                    os.remove(d)
                os.symlink(os.readlink(s), d)
                try:
                    st = os.lstat(s)
                    mode = stat.S_IMODE(st.st_mode)
                    os.lchmod(d, mode)
                except:
                    pass  # lchmod not available
            elif os.path.isdir(s):
                Directory.copy(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)
