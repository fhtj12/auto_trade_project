import matplotlib.pyplot as plt
from data.investar import Analyzer
from db.db_manager import DBManager

# DB Connection test
# db = DBManager()
# with db : 
#     result = db.select("fetchTest")

# print(type(result))

from db.sql.test import Test
b = Test(id = '1')
b.save()

# mk = Analyzer.MarketDB()
# df = mk.get_daily_price('005930', '2017-07-10', '2018-06-30')

# plt.figure(figsize=(9, 6))
# plt.subplot(2, 1, 1)
# plt.title('Samsung Electronics (Investar Data)')
# plt.plot(df.index, df['close'], 'c', label='Close')
# plt.legend(loc='best')
# plt.subplot(2, 1, 2)
# plt.bar(df.index, df['volume'], color='g', label='Volume')
# plt.legend(loc='best')
# plt.show()