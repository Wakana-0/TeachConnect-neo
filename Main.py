from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QMessageBox, QComboBox, QLineEdit, QProgressBar, QCommandLinkButton
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QDir
from PySide6.QtGui import QIcon  # 添加QIcon导入
from loguru import logger
import os
from datetime import datetime  # 添加datetime导入

# 创建logs文件夹（如果它不存在）
log_folder = './logs'
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# 生成当前时间的日志文件名
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file_name = os.path.join(log_folder, f"app_{current_time}.log")

# 初始化日志记录器，将日志文件放在logs文件夹下
logger.add(log_file_name, format="{time} {level} {message}", level="DEBUG")
logger.info("应用程序启动")

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.resize(315, 180)
        self.setWindowTitle("TeachConnect-neo - 登录")
        self.setWindowIcon(QIcon('./assets/icon.png'))  # 设置窗口图标

    def load_ui(self):
        # 创建一个QUiLoader对象
        loader = QUiLoader()
        logger.debug("QUiLoader对象已创建")

        # 获取LoginWindow.ui文件的路径
        ui_file_name = QDir.current().filePath('./pages/LoginWindow.ui')
        logger.debug(f"UI文件路径: {ui_file_name}")

        # 检查文件是否存在
        if not QFile.exists(ui_file_name):
            logger.error(f"UI文件 {ui_file_name} 不存在")
            return

        # 打开UI文件
        ui_file = QFile(ui_file_name)

        if not ui_file.open(QFile.ReadOnly):
            # 如果文件无法打开，记录错误信息并返回
            logger.error(f"无法打开 {ui_file_name}: {ui_file.errorString()}")
            return

        logger.debug("UI文件已成功打开")

        # 加载UI文件
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        if self.ui is not None:
            # 设置主窗口的中心部件
            self.setCentralWidget(self.ui)
            logger.info("UI文件已成功加载并设置为主窗口的中心部件")

            # 访问login_btn
            self.login_btn = self.ui.findChild(QPushButton, "login_btn")
            self.login_btn.clicked.connect(self.login)

            # 访问password_input
            self.password_input = self.ui.findChild(QLineEdit, "password_input")

            # 访问account_selection
            self.account_selection = self.ui.findChild(QComboBox, "account_selection")

            # 访问go_registration
            self.go_registration = self.ui.findChild(QCommandLinkButton, "go_registration")
            self.go_registration.clicked.connect(self.open_register_window)

        else:
            logger.error("加载UI文件失败")

    def login(self):
        QMessageBox.information(self, "提示", f"功能还在开发中！\n\n"
                                              f"您输入的账号为：{self.account_selection.currentText()}\n"
                                              f"您输入的密码为：{self.password_input.text()}")

    def open_register_window(self):
        self.register_window = RegisterWindow()
        self.register_window.show()


class RegisterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.resize(340, 200)
        self.setWindowTitle("TeachConnect-neo - 注册")
        self.setWindowIcon(QIcon('./assets/icon.png'))  # 设置窗口图标

    def load_ui(self):
        # 创建一个QUiLoader对象
        loader = QUiLoader()
        logger.debug("QUiLoader对象已创建")

        # 获取RegisterWindow.ui文件的路径
        ui_file_name = QDir.current().filePath('./pages/RegisterWindow.ui')
        logger.debug(f"UI文件路径: {ui_file_name}")

        # 检查文件是否存在
        if not QFile.exists(ui_file_name):
            logger.error(f"UI文件 {ui_file_name} 不存在")
            return

        # 打开UI文件
        ui_file = QFile(ui_file_name)

        if not ui_file.open(QFile.ReadOnly):
            # 如果文件无法打开，记录错误信息并返回
            logger.error(f"无法打开 {ui_file_name}: {ui_file.errorString()}")
            return

        logger.debug("UI文件已成功打开")

        # 加载UI文件
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        if self.ui is not None:
            # 设置主窗口的中心部件
            self.setCentralWidget(self.ui)
            logger.info("UI文件已成功加载并设置为主窗口的中心部件")

            # 访问account_lineEdit
            self.account_lineEdit = self.ui.findChild(QLineEdit, "account_lineEdit")

            # 访问password_lineEdit
            self.password_lineEdit = self.ui.findChild(QLineEdit, "password_lineEdit")

            # 访问confirm_password_lineEdit
            self.confirm_password_lineEdit = self.ui.findChild(QLineEdit, "confirm_password_lineEdit")

            # 访问certainly_pushButton
            self.certainly_pushButton = self.ui.findChild(QPushButton, "certainly_pushButton")
            self.certainly_pushButton.clicked.connect(self.register)

        else:
            logger.error("加载UI文件失败")

    def register(self):
        # 获取输入的账号、密码、确认密码
        account = self.account_lineEdit.text()
        password = self.password_lineEdit.text()
        confirm_password = self.confirm_password_lineEdit.text()

        # 判断输入的密码是否一致
        if password != confirm_password:
            QMessageBox.warning(self, "警告", "两次输入的密码不一致！")
            return

        QMessageBox.information(self, "提示", f"功能还在开发中\n\n账户：{account}\n密码是否一致：{password == confirm_password}")


if __name__ == "__main__":
    # 创建QApplication对象，初始化GUI应用程序
    app = QApplication([])
    app.setWindowIcon(QIcon('./assets/icon.png'))  # 设置应用程序图标

    # 创建LoginWindow对象并显示
    mainWin = LoginWindow()
    mainWin.show()

    # 进入应用程序的主循环
    app.exec()

    logger.info("应用程序退出")
