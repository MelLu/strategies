from vnpy.app.cta_strategy import (
    CtaTemplate
)
from vnpy.trader.object import(
    BarData,
    TickData
)

from vnpy.a
class demostrategy(CtaTemplate):
    """"""

    author = "Mel"
    # define para
    fast_window = 10
    slow_window = 20

    # define vara
    fast_ma0 = 0.0
    fast_ma1 = 0.0
    slow_ma0 = 0.0
    slow_ma1 = 0.0

    parameters = [
        "fast_window",
        "slow_window"
    ]
    variables = [
        "fast_ma0",
        "fast_ma1",
        "slow_ma0",
        "slow_ma1"
    ]

    def __init__(
        self,
        cta_engine: Any,
        strategy_name: str,
        vt_symbol: str,
        setting: dict,
    ):
        super().__init__(cta_engine,strategy_name,vt_symbol,setting)

        self.bg= Bar

    def on_init(self):
        """ strategy setup """
        self.write_log("my first strategy setup")

        self.load_bar(10)

    def on_start(self):
        """start """
        self.write_log("strategy start")

    def on_stop(self):

        self.write_log("strategy stop")

    def on_bar(self,bar:BarData):
        """K line update"""
        