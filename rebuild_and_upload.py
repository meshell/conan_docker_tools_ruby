import os
import sys

def main(argv):
    supported_gcc_versions = ["4.6", "4.8", "4.9", "5.2", "5.3", "5.4", "6.2", "6.3"]
    if len(sys.argv) == 1:
        gcc_versions = supported_gcc_versions
    else:
        gcc_versions = sys.argv[1:]
    for gcc_version in gcc_versions:
        if gcc_version in supported_gcc_versions:
            folder_name = "gcc_{}".format(gcc_version)
            image_name = "meshell/conangcc{}".format(gcc_version.replace(".", ""))
            os.system("cd {} && ./build.sh".format(folder_name))
            os.system("sudo docker push {}".format(image_name))
        else:
            print("No docker image for gcc version {} available".format(gcc_version))

if __name__ == "__main__":
   main(sys.argv[1:])
