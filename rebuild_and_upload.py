import os

if __name__ == "__main__":

    for gcc_version in ["4.6", "4.8", "4.9", "5.2", "5.3", "5.4", "6.2", "6.3"]:
        folder_name = "gcc_{}".format(gcc_version)
        image_name = "meshell/conangcc{}".format(gcc_version.replace(".", ""))
        os.system("cd {} && ./build.sh".format(folder_name))
        os.system("sudo docker push {}".format(image_name))
