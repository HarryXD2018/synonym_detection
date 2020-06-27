import get_syn_baike

if __name__ == '__main__':
    file = open(r"../input/input.txt", 'r', encoding='UTF8', newline='')
    for line in file:
        name = line[:line.find("	")]
        print(name)
        print(get_syn_baike.get_syn(name))
