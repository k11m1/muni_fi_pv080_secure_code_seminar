# contains bunch of buggy examples
# taken from https://hackernoon.com/10-common-security-gotchas-in-python-and-how-to-avoid-them-e19fbe265e03
import subprocess
import base64
import flask
import sys

# Input injection
def transcode_file(request, filename):
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(
        source=filename)
    subprocess.call(command, shell=True)  # a bad idea!


# Assert statements
def fun_asserts(request, user):
    if (user.is_admin == False):
        sys.exit("Assert failed\n")
    # secure code...


# Pickles
class RunBinSh(object):
    def __reduce__(self):
        return (subprocess.Popen, (('/bin/sh',),))

def import_urlib_version(version):
    if (version == "2" or version == 2):
        import urllib as urllib
    if (version == "3" or version == 3):
        # sys.exit("Not a valid urlib version\n");
        import urllib3 as urllib

@app.route('/')
def index():
    module = flask.request.args.get("module")
    import_urlib_version(module)


# print(base64.b64encode(pickle.dumps(RunBinSh())))
