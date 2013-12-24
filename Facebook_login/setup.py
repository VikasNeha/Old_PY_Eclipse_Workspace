from distutils.core import setup
import py2exe
 
setup(
    console=['facebook_login.py'],
    options={
            "py2exe":{
                    "skip_archive": True,
                    "unbuffered": True,
                    "optimize": 2
            }
    }
)