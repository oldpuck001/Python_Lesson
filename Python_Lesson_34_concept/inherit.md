inherit.md

一個類可以是一個或多個類的子類，在這種情況下，子類將繼承超類的所有方法。

你可指定多個超類，通過這樣做可組合正交（獨立且不相關）的功能。

為此，一種常見的做法是使用一個核心超類以及一個或多個混合超類。

繼承的功能：

程序員總是想避免多次輸入同樣的代碼。可以通過創建函數來達成這個目標，但現在要解決一個更微妙的問題。如果你已經有了一個類，並要創建一個與之很像的類（可能只是新增了幾個方法），該如何辦呢？創建這個新類時，你不想複製舊類的代碼，將其粘貼到新類中。

例如，你可能已经有了一个名为Shape的类，它知道如何将自己绘制到屏幕上。现在你想创建一个名为Rectangle的类，但它不仅知道如何将自己绘制到屏幕上，而且还知道如何计算其面积。你不想重新编写方法draw，因为Shape已经有一个这样的方法，且效果很好。那么该如何办呢？让Rectangle继承Shape的方法，使得对Rectangle对象调用方法draw时，将自动调用Shape类的这个方法。