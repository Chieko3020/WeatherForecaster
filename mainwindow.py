# This Python file uses the following encoding: utf-8
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
import sys
import os
import requests
import pandas as pd
import rc_res
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox, QTableWidget
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt,QTime,QTimer
from history import History
from chart import ChartWidget
from ui_mainwindow import Ui_MainWindow
import rc_res
class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        #初始化UI 连接信号与槽
        self.ui.label.setText(self.getGreeting())#根据当前时间设置问候语
        self.ui.historyButton.clicked.connect(self.showHistoryDialog)
        self.ui.closeButton.clicked.connect(self.onCloseButtonClicked)
        self.ui.chartButton.clicked.connect(self.showChartDialog)
        self.excel_file = "query_history.xlsx"
        #设置可选查询城市 保存至列表
        city_list = [
            ('自动定位', 'AUTO'),
            ("北京市", "101010100"), ("哈尔滨市", "101050101"), ("长春市", "101060101"), ("沈阳市", "101070101"), ("天津市", "101030400"),
            ("呼和浩特市", "101080101"), ("乌鲁木齐市", "101130101"), ("银川市", "101170101"), ("西宁市", "101150101"), ("兰州市", "101160101"), ("西安市", "101110101"),
            ("拉萨市", "101140101"), ("成都市", "101270101"), ("重庆市", "101040100"), ("贵阳市", "101260101"), ("昆明市", "101290101"),
            ("太原市", "101100101"), ("石家庄市", "101090101"), ("济南市", "101120101"), ("郑州市", "101180101"), ("合肥市", "101220101"), ("南京市", "101190101"), ("上海市", "101020100"),
            ("武汉市", "101200101"), ("长沙市", "101250101"), ("南昌市", "101240101"), ("杭州市", "101210101"), ("福州市", "101230101"), ("台北市", "101340101"),
            ("南宁市", "101300101"), ("海口市", "101310101"), ("广州市", "101280101"), ("香港", "101320101"), ("澳门", "101330101"),
            ("深圳市", "101280601"), ("厦门市", "101230201"), ("宁波市", "101210401"), ("青岛市", "101120201"), ("大连市", "101070201"), ("桂林市", "101300501"), ("汕头市", "101280501"),
            ("连云港市", "101191001"), ("秦皇岛市", "101091101"), ("延安市", "101110300"), ("赣州市", "101240701"), ("三亚市", "101310201"), ("高雄市", "101340201"),
            ("西沙", "101310302"), ("南沙", "101280112")
        ]
        for city_name, city_code in city_list:
            self.ui.cityComboBox.addItem(city_name, city_code)
        self.initTimeEdit()#初始化计时器
        self.ui.searchButton.clicked.connect(self.searchWeather)

    def onCloseButtonClicked(self):
        # 触发窗口关闭事件，从而调用 closeEvent 方法
        self.close()

    def closeEvent(self, event):
        #重载关闭函数使得退出按钮和关闭窗口按钮均能响应并且弹出二次确认
        #同时清除临时记录文件
        ret = QMessageBox.question(self,'退出确认','确定要退出吗？', QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if ret == QMessageBox.Yes:
            if os.path.exists(self.excel_file):
                os.remove(self.excel_file)
            else:
                print(f'Excel file {self.excel_file} does not exist.')
            event.accept()  # 接受关闭事件
        else:
            event.ignore()

    def initTimeEdit(self):
        #初始化计时器 设置计时器更新频率
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)  # 每秒更新一次
        self.updateTime()  # 立即更新一次

    def updateTime(self):
        #更新计时器的显示效果
        currentTime = QTime.currentTime()
        self.ui.timeEdit.setTime(currentTime)

    def getGreeting(self):
        #根据当前时间改变问候语
        currentHour = QTime.currentTime().hour()
        if 6 <= currentHour < 12:
            return '早上好！'
        elif 12 <= currentHour < 18:
            return '下午好！'
        else:
            return '晚上好！'

    def searchWeather(self):
        #根据用户所选城市获取天气信息
        city_name = self.ui.cityComboBox.currentText()
        city_code = self.ui.cityComboBox.currentData()
        #未选择城市则弹出提示窗口
        if city_name == '':
            msgBox = QMessageBox.critical(self,'未选择需要查询的城市','在查询天气状况之前，请先选择一个城市',QMessageBox.Ok,QMessageBox.Ok)
            return
        #选择自动定位
        if city_code == 'AUTO':
            city_code, city_name = self.get_auto_city_code()#转到自动定位 获取城市代码
        weather_info = self.get_weather(city_code)#根据城市代码获取天气信息 保存至列表
        if isinstance(weather_info, list):
            #关闭初始'未查询'界面
            if self.ui.labeltable.isVisible() == True:
                self.ui.labeltable.hide()
            self.displayWeather(weather_info)#展示天气信息
            self.ui.label_2.setText(f'当前城市：{city_name}')
            self.saveQueryRecord(city_name, weather_info)  #保存查询记录
        else:
            QMessageBox.warning(self, '错误', weather_info)

    def displayWeather(self, weather_info):
        #展示天气信息
        self.ui.resultTable.setRowCount(len(weather_info))
        self.ui.resultTable.horizontalHeader().setStyleSheet("QHeaderView::section { background-color: transparent; }")
        self.ui.resultTable.verticalHeader().setStyleSheet("QHeaderView::section { background-color: transparent; }")
        for i, day_info in enumerate(weather_info):
            self.ui.resultTable.setItem(i, 0, QTableWidgetItem(day_info['ymd']))
            self.ui.resultTable.setItem(i, 1, QTableWidgetItem(day_info['week']))
            self.ui.resultTable.setItem(i, 2, QTableWidgetItem(day_info['type']))
            self.ui.resultTable.setItem(i, 3, QTableWidgetItem(day_info['high'].replace('高温 ', '')))
            self.ui.resultTable.setItem(i, 4, QTableWidgetItem(day_info['low'].replace('低温 ', '')))
            self.ui.resultTable.setItem(i, 5, QTableWidgetItem(day_info['sunrise']))
            self.ui.resultTable.setItem(i, 6, QTableWidgetItem(day_info['sunset']))
            self.ui.resultTable.setItem(i, 7, QTableWidgetItem(str(day_info['aqi'])))
            self.ui.resultTable.setItem(i, 8, QTableWidgetItem(day_info['fx']))
            self.ui.resultTable.setItem(i, 9, QTableWidgetItem(day_info['fl']))

    def get_auto_city_code(self):
        #自动定位获取城市信息
        #发送一个HTTP GET请求到API，返回基于用户IP地址的地理信息，包括城市名称
        #将API返回的响应内容转换成JSON格式，以便于后续处理
        #从JSON响应中提取城市名称。如果未找到城市信息，城市名称默认为'福州市'
        response = requests.get('https://ip.useragentinfo.com/json')
        data = response.json()
        city = data.get('city')  # 如果没有城市字段，则默认为'福州市'
        if city == '':
            msgBox = QMessageBox()
            msgBox.setWindowTitle('定位信息')
            msgBox.setText('定位失败，自动查询福州市的天气状况')
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
            city = '福州市'
            # 城市代码映射字典，包含可选城市的对应代码
        city_code_mapping = {
            "北京市": "101010100", "哈尔滨市": "101050101", "长春市": "101060101", "沈阳市": "101070101", "天津市": "101030400",
            "呼和浩特市": "101080101", "乌鲁木齐市": "101130101", "银川市": "101170101", "西宁市": "101150101", "兰州市": "101160101", "西安市": "101110101",
            "拉萨市": "101140101", "成都市": "101270101", "重庆市": "101040100", "贵阳市": "101260101", "昆明市": "101290101",
            "太原市": "101100101", "石家庄市": "101090101", "济南市": "101120101", "郑州市": "101180101", "合肥市": "101220101", "南京市": "101190101", "上海市": "101020100",
            "武汉市": "101200101", "长沙市": "101250101", "南昌市": "101240101", "杭州市": "101210101", "福州市": "101230101", "台北市": "101340101",
            "南宁市": "101300101", "海口市": "101310101", "广州市": "101280101", "香港": "101320101", "澳门": "101330101",
            "深圳市": "101280601", "厦门市": "101230201", "宁波市": "101210401", "青岛市": "101120201", "大连市": "101070201", "桂林市": "101300501", "汕头市": "101280501",
            "连云港市": "101191001", "秦皇岛市": "101091101", "延安市": "101110300", "赣州市": "101240701", "三亚市": "101310201", "高雄市": "101340201",
            "西沙": "101310302", "南沙": "101280112"
        }
        return city_code_mapping.get(city, '101230101'), city  # 如果未匹配到，默认返回福州

    def get_weather(self,city_code):
        #获取天气信息
        #发送一个HTTP GET请求到API，返回基于城市代码的天气信息
        #将API返回的响应内容转换成JSON格式，以便于后续处理
        #从JSON响应中提取各种天气信息
        url = f'http://t.weather.sojson.com/api/weather/city/{city_code}'
        response = requests.get(url)
        response.encoding = 'utf-8'
        try:
            data = response.json()
        except ValueError:
            return '无法解析天气信息'
        if data and data.get('status') == 200:
            forecast = data['data']['forecast']
            weather_info = []
            for day in forecast:
                weather_info.append({
                    'ymd': day['ymd'],
                    'week': day['week'],
                    'type': day['type'],
                    'high': day['high'],
                    'low': day['low'],
                    'sunrise': day['sunrise'],
                    'sunset': day['sunset'],
                    'aqi': day['aqi'],
                    'fx': day['fx'],
                    'fl': day['fl']
                })
            return weather_info
        else:
            return '无法获取天气信息'

    def saveQueryRecord(self, city_name, weather_info):
        #保存历史记录
        try:
            existing_df = pd.read_excel(self.excel_file)
        except FileNotFoundError:
            existing_df = pd.DataFrame()
        records = []
        for day_info in weather_info:
            records.append({
                    'city': city_name,
                    'ymd': day_info['ymd'],
                    'week': day_info['week'],
                    'type': day_info['type'],
                    'high': day_info['high'],
                    'low': day_info['low'],
                    'sunrise': day_info['sunrise'],
                    'sunset': day_info['sunset'],
                    'aqi': day_info['aqi'],
                    'fx': day_info['fx'],
                    'fl': day_info['fl']
                })
        #转换为DataFrame存储新记录
        df = pd.DataFrame(records)
        #如果现有记录不为空，合并新旧记录并删除重复记录
        if not existing_df.empty:
            combined_df = pd.concat([existing_df, df])
            combined_df.drop_duplicates(subset=['city', 'ymd'], keep='last', inplace=True)
        else:
            combined_df = df
        #将合并后的记录保存回Excel文件
        combined_df.to_excel(self.excel_file, index=False)

    def showHistoryDialog(self):
        #跳转历史记录窗口
        self.dialog = History(self.excel_file, self)  # 传递Excel文件路径
        self.dialog.exec()

    def showChartDialog(self):
        #跳转图表窗口
        city_name = self.ui.cityComboBox.currentText()
        city_code = self.ui.cityComboBox.currentData()
        #防止未查询城市天气
        if city_name == '':
            msgBox = QMessageBox.critical(self,'未选择需要查询的城市','在查询天气状况之前，请先选择一个城市',QMessageBox.Ok,QMessageBox.Ok)
            return
        if city_code == 'AUTO':
            city_code, city_name = self.get_auto_city_code()
        weather_info = self.get_weather(city_code)
        if isinstance(weather_info, list):
            self.chart = ChartWidget(weather_info, self)
            self.chart.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Mainwindow()
    widget.show()
    sys.exit(app.exec())
