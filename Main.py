from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, \
    QMessageBox, QComboBox, QLineEdit, QProgressBar, QCommandLinkButton
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QDir
from loguru import logger


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.resize(800, 600)

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


        else:
            logger.error("加载UI文件失败")

    def login(self):
        QMessageBox.information(self, "提示", f"功能还在开发中！\n\n"
                                              f"您输入的账号为：{self.account_selection.currentText()}\n"
                                              f"您输入的密码为：{self.password_input.text()}")


if __name__ == "__main__":
    # 初始化日志记录器
    logger.add("app.log", format="{time} {level} {message}", level="DEBUG")
    logger.info("应用程序启动")

    # 创建QApplication对象，初始化GUI应用程序
    app = QApplication([])

    # 创建MainWindow对象并显示
    mainWin = LoginWindow()
    mainWin.show()

    # 进入应用程序的主循环
    app.exec()

    logger.info("应用程序退出")
