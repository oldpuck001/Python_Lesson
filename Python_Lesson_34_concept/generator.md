generator.md

生成器是一种使用普通函数语法定义的迭代器。由於歷史原因，它也被稱為簡單生成器（simple generator）。

生成器函數使用yield關鍵字而不是return來返回值。它在被調用時返回一個生成器，即一種特殊的迭代器。

當需要生成下一個值時，生成器函數會從上次yield的位置繼續執行，而不是從頭開始。這使得生成器可以記住上次的執行狀態，並在需要時生成新的值。