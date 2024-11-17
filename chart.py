# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
# chart_dialog.py
from PySide6.QtWidgets import QDialog, QVBoxLayout
from ui_chart import Ui_chart
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
# 设置全局字体为SimHei字体，解决负号显示问题
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
class ChartWidget(QDialog):
    def __init__(self, weather_info, parent=None):
        super().__init__(parent)
        self.ui = Ui_chart()
        self.ui.setupUi(self)
        self.weather_info = weather_info
        self.initUI()

    def initUI(self):
        #初始化UI
        self.plotChart()#绘制图表

    def plotChart(self):
        #绘制图表
        dates = [day['ymd'][5:] for day in self.weather_info]#处理日期格式，去掉年份
        #处理高温和低温格式，只保留值
        highs = [int(day['high'].replace('高温 ', '').replace('℃', '')) for day in self.weather_info]
        lows = [int(day['low'].replace('低温 ', '').replace('℃', '')) for day in self.weather_info]

        fig, ax = plt.subplots()
        # 绘制高温和低温曲线，并设置颜色、标签、标题
        ax.plot(dates, highs, color='red', label='高温')
        ax.plot(dates, lows, color='blue', label='低温')
        ax.legend()
        ax.set_xlabel('日期')
        ax.set_ylabel('温度 (℃)')
        ax.set_title('15天气温趋势')
        # 将图表嵌入并且绘制到Qt的QWidget中
        canvas = FigureCanvas(fig)# 将 Matplotlib 图表转换为 Qt 可用的绘图组件FigureCanvas
        layout = self.ui.chartWidget.layout()# 获取 chartWidget 的布局管理器QVBoxLayout
        if layout is None:
            #如果不存在则创建一个
            layout = QVBoxLayout(self.ui.chartWidget)
        layout.addWidget(canvas)
        canvas.draw()
