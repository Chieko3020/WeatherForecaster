from PySide6.QtWidgets import QDialog, QTableView, QMessageBox
from ui_history import Ui_History
from PySide6.QtCore import Qt, QSortFilterProxyModel, QRegularExpression
from PySide6.QtGui import QStandardItemModel, QStandardItem
import pandas as pd

class History(QDialog):
    def __init__(self, excel_file, parent=None):
        super().__init__(parent)
        self.ui = Ui_History()
        self.ui.setupUi(self)
        self.excel_file = excel_file
        self.initUI()

    def initUI(self):
        # 初始化UI 连接信号与槽
        self.loadHistory()  # 导入记录文件
        self.ui.deleteButton.clicked.connect(self.deleteSelectedRow)
        self.ui.closeButton.clicked.connect(self.accept)
        self.ui.searchEdit.returnPressed.connect(self.filterHistory)
        #self.ui.tableView.setCurrentIndex(-1, -1)
        self.ui.searchColumnComboBox.addItems(['城市','日期','星期','天气状况'])
        self.ui.searchColumnComboBox.currentTextChanged.connect(self.filterHistory)

    def loadHistory(self):
        # 加载Excel文件中的历史记录至DataFrame，并显示在表格中
        try:
            self.df = pd.read_excel(self.excel_file)
            self.model = QStandardItemModel(self)
            self.proxy_model = QSortFilterProxyModel(self)
            self.proxy_model.setSourceModel(self.model)
            self.proxy_model.setFilterKeyColumn(0)  # 默认按第一列筛选
            self.ui.tableView.setModel(self.proxy_model)  # 修改为 QTableView
            self.displayHistory(self.df)
        except FileNotFoundError:
            self.df = pd.DataFrame()
            self.ui.tableView.setRowCount(0)

    def deleteSelectedRow(self):
        # 删除选中的行，并更新Excel文件
        row = self.ui.tableView.currentIndex().row()
        if row >= 0:  # 检查是否选中了有效行
            self.model.removeRow(row)
            self.df = pd.read_excel(self.excel_file)
            self.df = self.df.drop(self.df.index[row])
            self.df.to_excel(self.excel_file, index=False)
        else:
            QMessageBox.warning(self, '删除错误', '未选中任何行。')

    def filterHistory(self):
        # 根据输入框中的城市模糊查询历史记录，并显示在表格中
        search_text = self.ui.searchEdit.text().strip().lower()
        search_column = self.ui.searchColumnComboBox.currentText().strip().lower()  # 从下拉框中获取选择的筛选条件
        if not search_text:
            self.proxy_model.setFilterRegularExpression(QRegularExpression("", QRegularExpression.CaseInsensitiveOption))
        else:
            if search_column == '城市':
                self.proxy_model.setFilterKeyColumn(0)  # 设置筛选列
            elif search_column == '日期':
                self.proxy_model.setFilterKeyColumn(1)  # 设置筛选列
            elif search_column == '星期':
                self.proxy_model.setFilterKeyColumn(2)  # 设置筛选列
            elif search_column == '天气状况':
                self.proxy_model.setFilterKeyColumn(3)  # 设置筛选列
            self.proxy_model.setFilterRegularExpression(QRegularExpression(search_text, QRegularExpression.CaseInsensitiveOption))

    def displayHistory(self, df):
        # 在表格中显示历史记录
        self.model.clear()
        self.model.setColumnCount(11)
        self.model.setHorizontalHeaderLabels(['城市', '日期', '星期', '天气类型', '高温', '低温', '日出时间', '日落时间', '空气质量', '风向', '风力'])

        for _, row in df.iterrows():
            items = [
                QStandardItem(str(row['city'])),
                QStandardItem(str(row['ymd'])),
                QStandardItem(str(row['week'])),
                QStandardItem(str(row['type'])),
                QStandardItem(str(row['high'].replace('高温 ', ''))),
                QStandardItem(str(row['low'].replace('低温 ', ''))),
                QStandardItem(str(row['sunrise'])),
                QStandardItem(str(row['sunset'])),
                QStandardItem(str(row['aqi'])),
                QStandardItem(str(row['fx'])),
                QStandardItem(str(row['fl']))
            ]
            self.model.appendRow(items)
