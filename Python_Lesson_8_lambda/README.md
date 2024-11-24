README.md

在Python中，lambda函數是一種匿名函數，即沒有名字的函數。它們通常用於需要一個函數，但該函數要么非常簡單，以至於不值得單獨定義，要么只用一次。lambda函數的基本語法如下：

lambda arguments: expression

lambda：是一個關鍵字，指出這是一個匿名函數。

arguments：是傳遞給lambda函數的參數，可以是多個，用逗號分隔。

expression：是一個關於參數的表達式，該表達式的計算結果就是lambda函數的返回值。

lambda的作用：
簡化代碼：對於簡單的函數，使用lambda可以避免正式的函數定義，使代碼更加簡潔。
作為高階函數的參數：lambda函數經常用作其他函數的參數，特別是在那些接受函數作為參數的高階函數中，如map()、filter()、sorted()等。
立即執行函數表達式（IIFE）：lambda可以用於創建立即執行的函數表達式（IIFE），這在需要一個簡短生命週期的匿名函數時非常有用。

lambda的限制：
只能包含單個表達式，不能包含多個表達式或語句。
不如具名函數那樣易於閱讀和調試，特別是對於複雜的表達式。