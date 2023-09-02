import sys
#from pathos.multiprocessing import ProcessingPool as Pool
from multiprocessing import Pool
from pytube import YouTube
from youtubeMultiDownloader import UiMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class YouTubeInstance:
    def __init__(self, path):
        self.youtube = YouTube
        self.path = path
        #self.ui_obj = ui_obj

    def download_file(self, url):
        self.youtube(url).streams.get_highest_resolution().download(self.path)
        #self.ui.ui.youtube_outputs.setText(f'Video \'{self.youtube.title}\' has been downloaded successfully!')


class YouTubeMultiDownloader(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.pool = Pool
        self.ui = UiMainWindow()
        self.ui.setup_ui(self)
        self.path_to_dir = None
        self.urls = None

    def _get_urls_from_form(self):
        self.urls = self.ui.youtube_urls.toPlainText().split('\n')
        return len(self.urls)

    def choose_directory(self):
        self.path_to_dir = str(QFileDialog.getExistingDirectory(self, "Select Directory"))

    def run_multi_downloads(self):
        youtube = YouTubeInstance(self.path_to_dir)
        self.pool(self._get_urls_from_form()).map(youtube.download_file, self.urls)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = YouTubeMultiDownloader()
    application.show()
    sys.exit(app.exec_())
    
    # https://stackoverflow.com/questions/70054547/how-to-right-use-pool-in-parallel-downloading-files