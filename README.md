# stock_relationship
用程序计算美的与格力股价关系，制作搬砖模型

中国国内两家电巨头美的和格力是一对老冤家，股票相关性都非常高。有不少人买股票就是用这种搬砖的方式，对于相关性很高的股票，如果基中一个相对来说涨得比较多了，那就将仓位移到低估的另一个上，利用这种方法来尽量赚取更多的收益。

这里用python来做多项式拟合，求出美的与格力股价的相关性，进而为搬砖操作提供一个科学的指导。

假设美的与格力的相关函数为： midea = a * gree + b

那么求出a和b即可，利用numpy的polyfit函数可以非常方便地求出来。

以 2017.03.02日后的数据可以得到

__midea = 1.519 * gree - 9.923__

画图可得：

![plot image](https://github.com/inspire365/stock_relationship/blob/master/mg.png)


