#Displays the assoicated help markdown file
import markdown as md
from PySide2.QtWidgets import *
import app_utils

HELP_DOC_FILE_PATH = "./Help/help.md"
OLD_HELP_DOC_FILE_PATH = "./Help/help(old).md"
HELP_DOC_FILE_DIR = "./Help/"
if app_utils.is_running_as_executable():
    HELP_DOC_FILE_PATH = app_utils.get_resource_path("Help/help.md")
    OLD_HELP_DOC_FILE_PATH = app_utils.get_resource_path("Help/help(old).md")
    HELP_DOC_FILE_DIR = app_utils.get_resource_path("Help/")

class Help(QWidget):

    def __init__(self):
        super().__init__()

        self.markdown_view = QTextBrowser(readOnly=True)
        self.markdown_view.setOpenExternalLinks(True)
        self.mainLayout = QVBoxLayout()

        self.setup_ui()

    def setup_ui(self):

        # Writing xml file
        with open(HELP_DOC_FILE_PATH, "r") as f:
           doc = md.markdown(f.read(),  extensions=['fenced_code', 'codehilite', 'tables', 'attr_list'])

        self.markdown_view.setHtml(doc)
        self.mainLayout.addWidget(self.markdown_view)
        self.setLayout(self.mainLayout)



class HelpDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("HDLGen Help")

        self.markdown_view = QTextBrowser(readOnly=True)
        self.markdown_view.setOpenExternalLinks(True)

        self.mainLayout = QVBoxLayout()
        self.setFixedSize(700, 500)
        self.setup_ui()

    def setup_ui(self):

        # Writing xml file
        with open(HELP_DOC_FILE_PATH, "r") as f:
           doc = md.markdown(f.read(),  extensions=['fenced_code', 'codehilite', 'tables', 'attr_list'])

        self.markdown_view.setHtml(doc)
        self.mainLayout.addWidget(self.markdown_view)
        self.setLayout(self.mainLayout)


"""
class WebEnginePage(QWebEnginePage):
    def acceptNavigationRequest(self, url,  _type, isMainFrame):
        if _type == QWebEnginePage.NavigationTypeLinkClicked:
            QDesktopServices.openUrl(url);
            return False
        return True

class HtmlView(QWebEngineView):
    def __init__(self, *args, **kwargs):
        QWebEngineView.__init__(self, *args, **kwargs)
        self.setPage(WebEnginePage(self))
"""



