import pyqrcode, sys

if __name__ == "__main__":
    website = sys.argv[1]
    url = pyqrcode.create("https://{}.herokuapp.com".format(website))
    url.png('assets/qrcode.png', scale=4)
