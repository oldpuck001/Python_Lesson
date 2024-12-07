polymorphism.md

多態：多態指的是能夠同樣地對待不同類型和類的對象，即無須知道對象屬於哪個類就可調用其方法。

術語多態（polymorphism）源自希臘語，意思是“有多種形態”。這大致意味著即便你不知道變量指向的是哪種對象，也能夠對其執行操作，且操作的行為將隨對象所屬的類型（類）而異。

每當有人以不同的方式實現對象時，你都需要重新實現你的模塊。如果你將該模塊賣給了別人，轉而從事其他項目的開發，客戶該如何辦呢？顯然，這種實現不同行為的方式既不靈活也不切實際。

那麼該如何做呢？讓對象自己去處理這種操作。這好像沒什麼大不了，但仔細想想將發現，這樣事情將簡單得多：每種新對像都能夠獲取或計算其價格並返回結果，而你只需向它們詢問價格即可。這正是多態（從某種程度上說還有封裝）的用武之地。

多態和方法：

每當需要在無須知道對像是什麼樣的情況下，就能對其執行操作時，都是多態在起作用。這不僅僅適用於方法，內置運算符和函數也大量使用了多態。請看下面的代碼：

>>>1 + 2
3
>>>'Fish' + 'license'
'Fishlicense'

上述代碼表明，加法運算符（+）既可用於數（這裡是整數），也可用於字符串（以及其他類型的序列）。為證明這一點，假設你要創建一個將兩個對象相加的add函數，可像下面這樣定義它（這與模塊operator中的函數add等價，但效率更低）：

def add(x, y):
    return x + y

可使用眾多不同類型的參數來調用這個函數。

>>>add(1, 2)
3
>>>add('Fish', 'licence')
'Fishlicence'

這也許有點傻，但重點在於參數可以是任何支持加法的對象（請注意，這些對象必須支持它們之間的加法，因此調用(1, ’license’)不可行）。如果要編寫一個函數，通過打印一條消息來指出對象的長度，可以像下面這樣做（它對參數的唯一要求是有長度，可對其執行函數len）。

def length_message(x):
    print("The length of", repr(x), "is", len(x))

如你所見，這個函數還使用了repr。 repr是多態的集大成者之一，可用於任何對象。

很多函數和運算符都是多態的，你編寫的大多數函數也可能如此，即便你不是有意為之。每當你使用多態的函數和運算符時，多態都將發揮作用。

事實上，要破壞多態，唯一的辦法是使用諸如type、issubclass等函數顯式地執行類型檢查，但你應盡可能避免以這種方式破壞多態。重要的是，對象按你希望的那樣行事，而非它是否是正確的類型（類）。然而，不要使用類型檢查的禁令已不像以前那麼嚴格。引入抽象基類和模塊abc後，函數issubclass本身也是多態的了！

這裡討論的多態形式是Python編程方式的核心，有時稱為鴨子類型。這個術語源自如下說法：“如果走起來像鴨子，叫起來像鴨子，那麼它就是鴨子。”有關鴨子類型的詳細信息，請參與http://en.wikipedia.org/wiki/Duck_typing。