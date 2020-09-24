def mergeKLists(lists):
    result = []
    # for i in range(len(lists)):
    #     for j in range(len(lists[i])):
    #         result.append(lists[i][j])
    # return sorted(result)
    for i in tuple(lists):

        for j in i:
            result.append(j)
    return sorted(result)


# ll = [[1,4,5],[1,3,4],[2,6]]
# for i in ll:
#     for j in i:
#         print(j)
print(mergeKLists([[1,4,5],[1,3,4],[2,6]]))
