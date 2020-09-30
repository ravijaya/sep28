def copy(src_file, dest_file):
    try:
        fp = open(src_file)
        fw = open(dest_file, 'w')
        1/ 0

        fw.write(fp.read())
    except FileNotFoundError as error:
        print(error)
    except:   # generic
        print('internal script errror')
    else:
        print('else - block')
        fp.close()
        fw.close()

if __name__ == '__main__':
    try:
        copy('passwd.txt', 'passwd-copy.txt')
    except:
        print("error")