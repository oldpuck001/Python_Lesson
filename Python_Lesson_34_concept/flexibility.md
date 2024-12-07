flexibility.md

「Python基礎教程（第3版）」中介紹的編程理念：靈活性

設計和編程時，應以靈活性為目標。隨著對所面臨問題了解得越來越深入，你應心甘情願乃至隨時準備修改程序的方方面面，不要固守最初的想法。

原型設計

要深入了解問題和可能的實現方案，一個重要的技巧是編寫程序的簡化版本，以了解它是如何工作的。使用Python編寫原型非常容易，使用眾多其他語言編寫一個原型所需的時間足以讓你使用Python編寫多個原型。即便如此，除非萬不得已，否則不要推倒重來，因為對原型進行重構和修改，讓其變成功能上更好的系統，通常是更佳的解決方案。在實際開發工作中，完全可以先開發原型，再通過重構它來獲得最終的系統。要深入地了解推倒重來的恐怖之處，可參閱Joel Spolsky撰寫的文章“Things You Should Never Do，Part I”（http://joelonsoftware.com）。據Spolsky講，對所有軟件公司來說，推倒重來都是最嚴重的策略性錯誤。

配置

提取常量：所謂常量，指的是內置的字面量值，如數、字符串和列表。對於這些值，可將其存儲在全局變量中，並且不會修改這些全局變量，而是將它們作為常量（即符號常量）。要指出變量被視為符號常量，可遵循一種特殊的命名約定：只在變量名中使用大寫字母並用下劃線分隔單詞。並將這些包含常量的代碼行放在程序開頭。

配置文件：通過將配置變量放在配置文件中，讓用戶能夠配置程序，使其按自己希望的方式行事。這樣，用戶就可根據自己的偏好修改程序，可能讓他們使用程序時的心情更為愉悅。畢竟使用軟件時面臨的主要挫折之一是不能讓它按自己希望的方式行事。

自動化測試（先測試再編碼）

程序員無時無刻不在做這樣的事情。在編譯型語言中，將不斷重複編輯、編譯、運行的循環。在有些情況下，編譯程序時就會出現問題，程序員不得不在編輯和編譯之間來回切換。在Python中，不存在編譯階段，只有編輯和運行階段。測試就是運行程序。

要避免代碼在開發途中被淘汰，必須能夠應對變化並具備一定的靈活性，因此為程序的各個部分編寫測試至關重要（這稱為單元測試），而且是應用程序設計工作的重要組成部分。極限編程先鋒引入了“測試一點點，再編寫一點點代碼”的理念。這種理念與直覺不太相符，卻很管用，勝過與直覺一致的“編寫一點點代碼，再測試一點點”的做法。換而言之，測試在先，編碼在後。這也稱為測試驅動的編程。