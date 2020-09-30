def copy(src_file, dest_file):
    try:
        fp = fw = None

        fp = open(src_file)
        fw = open(dest_file, 'w')


        fw.write(fp.read())
    except FileNotFoundError as error:
        print(error)
    except:   # generic
        print('internal script errror')
    finally:
        print('finally - block')
        if fp:
            fp.close()

        if fw:
            fw.close()

if __name__ == '__main__':
    try:
        copy('passwd.txt', 'passwd-copy.txt')
    except:
        print("error")