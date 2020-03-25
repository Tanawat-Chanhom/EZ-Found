import os

def main():
    with open('package.txt', 'r') as file:
        packages = file.read()
        packages = packages.split()
        packages = " ".join(packages)
    print("Going to install follwing package(s): " + packages)
    os.system('py -m pip install ' + packages)

if __name__ == "__main__":
    main()