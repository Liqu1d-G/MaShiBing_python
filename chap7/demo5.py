# Editor : Liquid
# Time :  17:38

# 字典元素的遍历

score = {'张三' : 100, '李四' : 90, '王五': 45}

for item in score:
    print(item, score[item], score.get(item))
