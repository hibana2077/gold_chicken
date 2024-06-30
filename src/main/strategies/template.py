from backtesting import Strategy
from backtesting import Backtest

def SIGNAL(df,col_name):
    return df[col_name]

class Scalping_Strategy(Strategy):
    atr_sl_rate = 1.3
    TPSL_rate = 1.5
    save_size_rate = 0.125
    init_cash = 100
    profit_target = 500
    size_multiplier_rate = 0.5

    def init(self):
        super().init()
        self.signal = self.I(SIGNAL, self.data, 'Signal')

    def next(self):
        super().next()

        slatr = self.atr_sl_rate * self.data.ATR[-1]
        size_multiplier = self.size_multiplier_rate if self.equity >= self.profit_target else 1.0

        if self.signal == 2:
            sl_price = self.data.Close[-1] - slatr
            tp_price = self.data.Close[-1] + self.TPSL_rate * slatr
            size = min(self.save_size_rate * self.equity / slatr, self.init_cash / slatr) * size_multiplier
            if self.equity > self.init_cash * 1.5:
                self.buy(sl=sl_price, tp=tp_price, size=int(size))
            else:
                self.buy(sl=sl_price, tp=tp_price)

        if self.signal == 1:
            sl_price = self.data.Close[-1] + slatr
            tp_price = self.data.Close[-1] - self.TPSL_rate * slatr
            size = min(self.save_size_rate * self.equity / slatr, self.init_cash / slatr) * size_multiplier
            if self.equity >= self.init_cash * 1.5:
                self.sell(sl=sl_price, tp=tp_price, size=int(size))
            else:
                self.sell(sl=sl_price, tp=tp_price)