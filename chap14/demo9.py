# 导入带有包的模块时注意事项

# 使用import方式进行导入时，只能跟包名或模块名
import calc
import pakage1


# 使用from...import方式可以导入包，模块，函数等
from pakage1 import module_A
from pakage1.module_A import a
