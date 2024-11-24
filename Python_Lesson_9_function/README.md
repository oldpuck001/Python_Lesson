README.md

函數執行特定的操作並返回一個值，在Python中並非所有的函數都返回值。

定義函數：def語句

從函數返回值：return

下面的函數返回一個由斐波那契數組成的列表（一種數列，其中每個數都是前兩個數的和）。

什麼都不返回的函數不包含return語句，或者包含return語句，但沒有在return後面指定值，return語句只是為了結束函數。

所有的函數都返回值。如果你沒有告訴它們該返回什麼，將返回None。

函数的参数

編寫函數旨在為當前程序（甚至其他程序）提供服務，你的職責是確保它在提供的參數正確時完成任務，並在參數不對時以顯而易見的方式失敗。 （為此，通常使用斷言或異常。）

在def語句中，位於函數名後面的變量通常稱為形參，而調用函數時提供的值稱為實參，但「Python基礎教程（第3版）」中基本不對此做嚴格的區分。在很重要的情況下，會將實參稱為值，以便將其與類似於變量的形參區分開來。

函數通過參數獲得了一系列的值，參數不過是變量而已。在函數內部給參數賦值對外部沒有任何影響。

同樣，在函數內部重新關聯參數（即給它賦值）時，函數外部的變量不受影響。參數存儲在局部作用域內。

在Python中調用函數的時候，參數有兩類：位置參數和關鍵字參數。通過給參數指定默認值，可使其變成可選的。

使用名稱指定的參數稱為關鍵字參數。關鍵字參數最大的優點在於，可以指定默認值。

結合使用位置參數和關鍵字參數時，必須先指定所有的位置參數，否則解釋器將不知道它們是哪個參數（即不知道參數對應的位置）。

通常不應結合使用位置參數和關鍵字參數。一般而言，除非必不可少的參數很少，而帶默認值的可選參數很多，否則不應結合使用關鍵字參數和位置參數。

星號*意味著收集餘下的位置參數。參數前面的星號將提供的所有值都放在一個元組中，也就是將這些值收集起來。賦值時帶星號的變量收集多餘的值，不過賦值時是將收集的值存放在列表中而不是元組中。

星號不會收集關鍵字參數。要收集關鍵字參數，可使用兩個星號。這樣得到的是一個字典而不是元組。可結合使用以上兩種技術。