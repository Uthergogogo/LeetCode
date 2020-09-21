def letterCombinations(digits):
    phone_dict = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'],
                  7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
    if not digits:
        return []
    elif len(digits) == 1:
        return phone_dict[int(digits)]
    else:
        # 每次只加一个 加完的结果当作第一个数与之后的第二个数继续加
        res, nn, pivot = phone_dict[int(digits[0])], [], 1
        while pivot < len(digits):
            temp = phone_dict[int(digits[pivot])]
            for item in res:
                for elem in temp:
                    curr = item + elem
                    nn.append(curr)
            # res = [i + j for i in res for j in temp]
            pivot += 1
            res = nn
            nn = []
        return res


print(len(letterCombinations('234')))