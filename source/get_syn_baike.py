import baike_crawler_model
import re


def get_syn(name):
    syn = baike_crawler_model.baike_search((name, '001'))
    print(syn)
    syn1 = [name]
    symbols = [',', '，', '、', '；', '字', '号', '又字', '又号']
    for symbol in symbols:
        for item in syn:
            item: str
            if symbol in item:
                sp = item.split(symbol)
                for s in sp:
                    syn.append(s)
                syn.remove(item)
    for item in syn:
        if item in ["", "又", "字", "号"] or item == name:
            pass
        else:
            syn1.append(re.sub(u"\\(.*?\\)|\\{.*?\\}|\\[.*?]|\\（.*?\\）", "", item))
    if len(syn1) != 1:
        file = open(r"../output/name_syn.txt", "a", encoding='UTF8')
        file.write(", ".join(syn1))
        file.write("\n")
    return syn1
