dict_README.md

字典，是Python中唯一的內置映射類型，其中的值不按順序排列，而是存儲在鍵下。

字典由鍵及其相應的值組成，這種鍵-值對，稱為項（item）。

每個鍵與其值之間都用冒號分隔，項之間用逗號分隔，而整個字典放在花括號內。

空字典（沒有任何項）用兩個花括號表示，類似於下面這樣：{}

在字典（以及其他映射類型）中，鍵必須是獨一無二的，而字典中的值無需如此。

鍵的類型：字典中的鍵可以是任何不可變的類型，如整數、浮點數（實數）、字符串或元組。

下面是Python字典的一些用途：
1_表示棋盤的狀態，其中每個鍵都是由坐標組成的元組；
2_存儲文件修改時間，其中的鍵為文件名；
3_電話簿 / 地址簿。