class.md

類：類表示一組（或一類）對象，而每個對像都屬於特定的類。類的主要任務是定義其實例將包含的方法。

從很多方面來說，將類用作類型的同義詞，正是類的定義——一種對象。每個對像都屬於特定的類，並被稱為該類的實例。

一個類的對象為另一個類的對象的子集時，前者就是後者的子類。因此“雲雀”為“鳥類”的子類，而“鳥類”為“雲雀”的超類。

在英語日常交談中，使用複數來表示類，如birds（鳥類）和larks（雲雀）。在Python中，約定使用單數並將首字母大寫，如Bird和Lark。

通過這樣的陳述，子類和超類就很容易理解。但在面向對象編程中，子類關係意味深長，因為類是由其支持的方法定義的。類的所有實例都有該類的所有方法，因此子類的所有實例都有超類的所有方法。有鑑於此，要定義子類，只需定義多出來的方法（還可能重寫一些既有的方法）。

例如，Bird類可能提供方法fly，而Penguin類（Bird的一個子類）可能新增方法eat_fish。創建Penguin類時，你還可能想重寫超類的方法，即方法fly。鑑於企鵝不能飛，因此在Penguin的實例中，方法fly應什麼都不做或引發異常。

在較舊的Python版本中，類型和類之間涇渭分明：內置對像是基於類型的，而自定義對像是基於類的。因此，你可以創建類，但不能創建類型。在較新的Python2版本中，這種差別不那麼明顯。在Python3中，已不再區分類和類型了。


Python的舊式類與新式類

在Python2.2中，Python對象的工作方法有了很大的變化。這種變化帶來了多個方面的影響。

這些影響對Python編程新手來說大都不重要，但有一點需要注意：即使你使用的是較新的Python2版本，有些功能（如特性和函數super）也不適用於舊式類。

（ChatGPT對舊式類和新式類的區別的解釋：

在Python2中，有一個概念叫做“舊式類”和“新式類”，而在Python3中，只有“新式類”存在。

新式類和舊式類的區別在於它們的類繼承關係的實現方式不同。

舊式類是基於Python早期版本的實現，它們繼承關係是基於簡單的線性列表，沒有嚴格的層次結構。如果類不顯式繼承自object，則Python2中的類就是舊式類。

新式類引入了一個新的類型樹狀結構，類型階層的頂端是object類型。新式類繼承關係更清晰，並且有更多的特性，例如能夠支持描述符協議、靜態方法等等。

在Python3中，所有的類都是新式類，即使不顯式地繼承自object。）

在Python2中，如果想讓你的類是新式的，可以在模塊開頭包含賦值語句__metaclass__ = type，或者直接或間接地繼承內置類object或其他新式類。請看下面兩個類：

class NewStyle(object):
    more_code_here

class OldStyle:
    more_code_here

在這兩個類中，NewStyle是一個新式類，而OldStyle是一個舊式類。如果文件開頭包含賦值語句__metaclass__ = type，這兩個類都將是新式類。

也可在類的作用域內給變量__metaclass__賦值，但這樣做只設置當前類的元素（metaclass）。元類是其他類所屬的類，這是一個非常複雜的主題。

在《Python基礎教程（第3版）》中，作者並沒有在所有示例中都顯式地設置元類或繼承object。然而，如果你的程序無須與舊版Python兼容，建議將所有類都定義為新式類，並使用函數super等功能。

請注意，在Python3中沒有舊式類，因此無須顯式地繼承object或將__metaclass__設置為type。所有的類都將隱式地繼承object。如果沒有指定超類，將直接繼承它，否則將間接地繼承它。