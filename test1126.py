def binary_search(item_dic, target_item):
    item_dic_key = list(item_dic.keys())
    for i in range(len(item_dic_key)):
        for j in range(len(item_dic_key)  - 1):
            if item_dic_key[j] > item_dic_key[j + 1]:
                item_dic_key[j], item_dic_key[j + 1] = item_dic_key[j + 1], item_dic_key[j]
    item_dic_value = []
    ans = -1
    for k in item_dic_key:
        item_dic_value.append(item_dic[k])
    for i in range(len(item_dic_value)):
        if item_dic_value[i] == target_item:
            ans = i
    return item_dic_value, ans


# def after_sorting():
#     item_dic_key = list(item_dic.keys())
#     for i in range(len(item_dic_key) - 1):
#         for j in range(len(item_dic_key) - i - 1):
#             if item_dic_key[j] > item_dic_key[j + 1]:
#                 item_dic_key[j], item_dic_key[j + 1] = item_dic_key[j + 1], item_dic_key[j]
#     item_dic_value = []
#     for k in item_dic_key:
#         item_dic_value.append(item_dic[k])
#     return item_dic_value
# def binary_search(item_dic_value):
#     for i in range(len(item_dic_value)):
#         if item_dic_value[i] == target_item:
#             ans = i
#     return ans
item_dic = {3: "a", 13: "c", 5: "b", -5: "d"}
target_item = "b"
after_searching = binary_search(item_dic, target_item)
print(list(after_searching))
