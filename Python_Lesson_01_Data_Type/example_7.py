# example_1.py

# 字符串格式設置

# 從Python3.6開始支持f字符串，也稱為格式化字符串字面量，可以用來格式化字串。
# 字符串包含有關如何設置格式的信息，而這些信息是使用一種微型格式指定語言（mini-language）指定的。
# 每個值都被插入字符串中，以替換用花括號括起的替換字段。

# 替換字段由如下部分組成，其中每個部分都是可選的。
# 字段名：索引或標識符，指出要設置哪個值的格式並使用結果來替換該字段。除指定值外，還可指定值的特定部分，如列表的元素。
# 轉換標誌：跟在嘆號後面的單個字符。當前支持的字符包括r（表示repr）、s（表示str）和a（表示ascii）。
# 如果指定了轉換標誌，將不使用對象本身的格式設置機制，而是使用指定的函數將對象轉換為字符串，再做進一步的格式設置。
# 格式說明符：跟在冒號後面的表達式（這種表達式是使用微型格式指定語言表示的）。
# 格式說明符讓我們能夠詳細地指定最終的格式，包括格式類型（如字符串、浮點數或十六進制數），字段寬度和數的精度，如顯示符號和千位分隔符，以及各種對齊和填充方式。

# 替換字段
a = 'world'
print(f'Hello, {a}!')

phonebook = {'Beth': '9002','Alice': '2241','Cecil': '3358'}
print(f'Cecil\'s phone number is {phonebook['Cecil']}.')

a_list = [1, 2, 3, 4, 5]
print(f'one = {a_list[0]}')

pi = 'π'

# 轉換標誌
print(f'{pi!s}')
# 函數str通常創建外觀普通的字符串版本（這裡沒有對輸入字符串做任何處理）。
print(f'{pi!r}')
# 函數repr嘗試創建給定值的Python表示（這裡是一個字符串字面量）。
print(f'{pi!a}')
# 函數ascii創建只包含ASCII字符的表示，類似於Python2中的repr。

# 格式說明符：
num_1 = 42
num_2 = 1234567.89
num_3 = -1234567.89
print(f'The number is {num_1:$^10,d}')
print(f'The number is {num_1:$^10,.2f}')
print(f'The number is {num_1:^010,.2f}')
print(f'The number is {num_1:>+10,.2f}')
print(f'The number is {num_2:> 15,.2f}')
print(f'The number is {num_3:$=15,.2f}')
print(f'The number is {num_3:=015,.2f}')
print(f'The number is {num_1:>#13b}')
print(f'The number is {num_1:<#13d}')
print(f'The number is {num_1:^#13g}')
# 可以使用填充字符来扩充对齐说明符，这样将使用指定的字符而不是默认的空格来填充。
# 符號說明符：要指定左对齐、右对齐和居中，可分别使用<、>和^。
# 符號說明符： = ，指定将填充字符放在符号和数字之间。
# 在指定宽度的数前面，可添加一个标志。这个标志可以是零、加号、减号或空格，其中零表示使用0来填充数字。
# 如果要给正数加上符号，可使用说明符+（将其放在对齐说明符后面），而不是默认的-。如果将符号说明符指定为空格，会在正数前面加上空格而不是+。
# 指定填充的后面是寬度，使用整數指定，數和字符串的對齊方式不同。
# 設置浮點數（或其他更具體的小數類型）的格式時，默認在小數點後面顯示6位小數，並根據需要設置字段的寬度，而不進行任何形式的填充。
# 使用逗号来添加千位分隔符，並且放在宽度和表示精度的句点之间。如果要使用随区域而异的千位分隔符，应使用类型说明符n。
# 精度是使用整數指定的，但需要在它前面加上一個表示小數點的句點。
# 井号（#）选项，可将其放在符号说明符和宽度之间（如果指定了这两种设置）。这个选项将触发另一种转换方式，转换细节随类型而异。
# 例如，对于二进制、八进制和十六进制转换，将加上一个前缀。对于各种十进制数，它要求必须包含小数点（对于类型g，它保留小数点后面的零）。
# 可以指定要轉換的值是哪種類型，更準確的說，是要將其視為哪種類型。在格式說明符的最後位置指定。
# 类型      含义
# b        將整數表示為二進制數
# c        將整數解讀為Unicode碼點
# d        將整數視為十進制數進行處理，這是整數默認使用的說明符
# e        使用科學表示法來表示小數（用e來表示指數）
# E        與e相同，但使用E來表示指數
# f        將小數表示為定點數
# F        與f相同，但對於特殊值（nan和inf），使用大寫表示
# g        自動在定點表示法和科學表示法之間選擇，默認用於小數的說明符，默認情況至少有1位小數
# G        與g相同，但使用大寫來表示指數和特殊值
# n        與g相同，但插入隨區域而異的數字分隔符
# o        將整數表示為八進制數
# s        保持字符串的格式不變，這是默認用於字符串的說明符
# x        將整數表示為十六進制數並使用小寫字母
# X        與x相同，但使用大寫字母
# %        將數表示為百分比值（乘以100，按說明符f設置格式，再在後面加上%）

text = 'one two three'

# 要在最終結果中包含花括號，可在格式字符串中使用兩個花括號（即{{或}}）來指定。
print(f'{{one two three}}')
print(f'{{{text}}}')

# 對於其他類型也可指定精度，但是這樣做的情形不太常見。
print(f'{text:.3}')