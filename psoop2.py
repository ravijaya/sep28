class PackageManager:
    def __init__(self):
        print(self, 'am in constructor')

    def __del__(self):
        print(self, 'am getting destroyed !!!')


if __name__ == '__main__':  # namespace validation
    pm = PackageManager()
    print(pm)
