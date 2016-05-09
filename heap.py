def swap(alist, pos1, pos2):
    alist[pos1], alist[pos2] = alist[pos2], alist[pos1]


def isheap(heaplist):
    return(True)


def heap_add(heaplist, new_node):
    if isheap(heaplist):
        heaplist.append(new_node)
        pos_new = len(heaplist)-1

        while heaplist[pos_new] > heaplist[(pos_new//2 - 1)] and pos_new != 0:

            swap(heaplist, pos_new, pos_new//2 - 1)
            pos_new = pos_new//2 - 1


def has_children(heaplist, pos):
    try:
        l_child = heaplist[2*pos + 1]
        try:

            r_child = heaplist[2*pos + 2]
            return(l_child, r_child, 'two children')

        except IndexError:
            return(l_child, 'one child')

    except IndexError:
        return(['no children'])


def heap_rmvmax(heaplist):
    if isheap(heaplist):
        swap(heaplist, 0, -1)
        top = heaplist.pop()

        pos = 0

        while True:
            result = has_children(heaplist, pos)

# Primeiro caso - dois filhos:
            if result[-1] == 'two children':
                l_child, r_child = result[0], result[1]

                if heaplist[pos] < l_child or heaplist[pos] < r_child:

                    if l_child > r_child:
                        swap(heaplist, pos, 2*pos+1)
                        pos = 2*pos+1

                    elif r_child >= l_child:
                        swap(heaplist, pos, 2*pos+2)
                        pos = 2*pos+2

                else:
                    break

# Segundo caso -  um filho:
            elif result[-1] == 'one child':
                l_child = result[0]

                if heaplist[pos] < l_child:
                    swap(heaplist, pos, 2*pos+1)

                break

# Terceiro caso - nenhum filho:
            else:
                break

    return(top)
