import random


def random_password(plen=10, ucfirst=True, spchar=True):
    if plen >= 6 and plen % 2 != 0:
        plen = plen+1
    elif plen < 8:
        return None, 'length too small'
    length = plen - 2
    conso = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    vocal = ['a', 'e', 'i', 'o', 'u']
    spchars = ['!', '@', '#', '$', '%', '^', '*', '&', '*', '-', '+', '?']
    password = ''
    pmax = length // 2
    for i in range(1, pmax + 1):
        password += conso[random.randint(0, 19)]
        password += vocal[random.randint(0, 4)]

    if spchar:
        password = password[:-1] + spchars[random.randint(0, 11)]

    password += str(random.randint(10, 99))

    if ucfirst:
        password = password.capitalize()

    return password, 'success'


if __name__ == "__main__":
    p = random_password(11, True, True)
    print(p)
