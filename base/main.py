from os import getenv


def main():
    name = 'base-python'
    envType = getenv('ENT_TYPE')
    print(f'envType--> ${envType}')
    if envType:
        name = f'docker with ENT_TYPE={envType}'
    print(f'Hi, {name}')


if __name__ == '__main__':
    main()
