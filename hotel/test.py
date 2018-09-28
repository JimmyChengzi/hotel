
import copy as c


def cut_list(L,length):
    # 中间生成的length个元素组成的列表A
    page_list = []
    # 由每页的列表A组成的列表
    all_list = []
    bList = c.deepcopy(L)

    for page in L:
        print(len(bList))


        page_list.append(bList[0])
        #print(bList[0], end="\t")
        #print(L)
        del bList[0]

        if len(page_list) == length:
            print("分段",page_list)
            all_list.append(page_list)
            page_list= []
            print()
            if len(bList) < length:
                all_list.append(bList[:])
                #print(bList)
                break

    print(all_list)
    return all_list

L = list(range(1,37))
L = ['<Hotel: 布丁酒店>', '<Hotel: 凤凰宾馆>','<Hotel: 好百年精品酒店>', '<Hotel: 速8酒店>','<Hotel: 7维也纳3好酒店>' ,'<Hotel: 福临门快捷酒店>','<Hotel: 7天连锁酒店>']

cut_list(L,5)