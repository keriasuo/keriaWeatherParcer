import itertools
import sys

from PyQt6 import QtWidgets
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap, QFont, QMovie, QCursor
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QMenu, \
    QMessageBox, QErrorMessage
import requests
from PyQt6 import QtCore
from bs4 import BeautifulSoup
import GUIforWeather

url = 'https://world-weather.ru/pogoda/ukraine/donetsk/'
urll = 'https://sinoptik.ua/погода-ростов-на-дону'
r = requests.get(url)
rr = requests.get(urll)
soup = BeautifulSoup(r.text, 'html.parser')
ssoup = BeautifulSoup(rr.text, 'html.parser')


class ExampleApp(QtWidgets.QMainWindow, GUIforWeather.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.label_picweek1.hide()
        self.label_picweek2.hide()
        self.label_picweek3.hide()
        self.label_picweek4.hide()
        self.label_picweek5.hide()
        self.label_picweek6.hide()

        self.label_day1.hide()
        self.label_day2.hide()
        self.label_day3.hide()
        self.label_day4.hide()
        self.label_day5.hide()
        self.label_day6.hide()

        self.label_min1.hide()
        self.label_min2.hide()
        self.label_min3.hide()
        self.label_min4.hide()
        self.label_min5.hide()
        self.label_min6.hide()

        self.label_minz1.hide()
        self.label_minz2.hide()
        self.label_minz3.hide()
        self.label_minz4.hide()
        self.label_minz5.hide()
        self.label_minz6.hide()

        self.label_max1.hide()
        self.label_max2.hide()
        self.label_max3.hide()
        self.label_max4.hide()
        self.label_max5.hide()
        self.label_max6.hide()

        self.label_maxz1.hide()
        self.label_maxz2.hide()
        self.label_maxz3.hide()
        self.label_maxz4.hide()
        self.label_maxz5.hide()
        self.label_maxz6.hide()

        self.label_week1.hide()
        self.label_week2.hide()
        self.label_week3.hide()
        self.label_week4.hide()
        self.label_week5.hide()
        self.label_week6.hide()

        self.label_ch1.hide()
        self.label_ch2.hide()
        self.label_ch3.hide()
        self.label_ch4.hide()
        self.label_ch5.hide()
        self.label_ch6.hide()

        picnightb = QPixmap("icons/nightcloudbig.png")
        piccloudb = QPixmap("icons/cloudbig.png")
        piccloudsb = QPixmap("icons/cloudsbig.png")
        picrainb = QPixmap("icons/rainbig.png")
        picwindb = QPixmap("icons/windbig.png")
        picsnowb = QPixmap("icons/snowbig.png")
        picsunnyb = QPixmap("icons/sunnybig.png")

        picnights = QPixmap("icons/nightcloudsmall.png")
        picclouds = QPixmap("icons/cloudsmall.png")
        piccloudss = QPixmap("icons/cloudssmall.png")
        picrains = QPixmap("icons/rainsmall.png")
        picwinds = QPixmap("icons/windsmall.png")
        picsnows = QPixmap("icons/snowsmall.png")
        picsunnys = QPixmap("icons/sunnysmall.png")

        self.label_picweek1.setPixmap(picnights)
        self.label_picweek2.setPixmap(picnights)
        self.label_picweek3.setPixmap(picnights)
        self.label_picweek4.setPixmap(picnights)
        self.label_picweek5.setPixmap(picnights)
        self.label_picweek6.setPixmap(picnights)
        self.label_picmain.setPixmap(picnightb)
        self.label_pic1.setPixmap(picsnows)
        self.label_pic2.setPixmap(picrains)
        self.label_pic3.setPixmap(picsunnys)
        self.label_pic4.setPixmap(picrains)
        self.label_12.setFont(QFont('Segoe UI', 16))
        self.label_feels.setFont(QFont('Segoe UI', 12))
        self.label_wind.setFont(QFont('Segoi UI', 11))
        self.label_pressure.setFont(QFont('Segoi UI', 11))
        self.label_cloudiness.setFont(QFont('Segoi UI', 11))
        self.label_sunrise.setFont(QFont('Segoi UI', 11))
        self.label_sunset.setFont(QFont('Segoi UI', 11))
        self.label_8.setFont(QFont('Segoi UI', 16))
        self.label_10.setFont(QFont('Segoi UI', 16))

        self.label_todaynight.setFont(QFont('Segoi UI', 16))
        self.label_todaymorning.setFont(QFont('Segoi UI', 16))
        self.label_todayday.setFont(QFont('Segoi UI', 16))
        self.label_todayafter.setFont(QFont('Segoi UI', 16))
        self.label_9.setFont(QFont('Segoi UI', 16))

        self.label_nighttemp.setFont(QFont('Segoi UI', 16))
        self.label_morningtemp.setFont(QFont('Segoi UI', 16))
        self.label_daytemp.setFont(QFont('Segoi UI', 16))
        self.label_aftertemp.setFont(QFont('Segoi UI', 16))
        self.pushButton.clicked.connect(self.btn_find)
        self.pushButton_3.clicked.connect(self.btn_close)
        self.pushButton_2.clicked.connect(self.btn_svern)
        self.pushButton_4.clicked.connect(self.btn_use1)
        self.pushButton_5.clicked.connect(self.btn_use2)

        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowOpacity(0.9)
        radius = 30
        self.centralwidget.setStyleSheet(
            """
            background:black;
            border-top-left-radius:{0}px;
            border-bottom-left-radius:{0}px;
            border-top-right-radius:{0}px;
            border-bottom-right-radius:{0}px;
            """.format(radius)
        )
        self.lineEdit_2.returnPressed.connect(self.pushButton.click)

    def btn_close(self):
        app.closeAllWindows()
    def btn_use1(self):
        self.pushButton_4.setText('⚫')
        self.pushButton_5.setText('⚪')
        self.label_todayday.hide()
        self.label_todaymorning.hide()
        self.label_todayafter.hide()
        self.label_todaynight.hide()
        self.label_pic1.hide()
        self.label_pic2.hide()
        self.label_pic3.hide()
        self.label_pic4.hide()
        self.label_nighttemp.hide()
        self.label_morningtemp.hide()
        self.label_daytemp.hide()
        self.label_aftertemp.hide()
        self.label.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_7.hide()
        self.label_6.hide()
        self.label_5.hide()
        self.label_pressure.hide()
        self.label_feels.hide()
        self.label_wind.hide()
        self.label_cloudiness.hide()
        self.label_sunrise.hide()
        self.label_sunset.hide()
        self.line_2.hide()

        self.label_picweek1.show()
        self.label_picweek2.show()
        self.label_picweek3.show()
        self.label_picweek4.show()
        self.label_picweek5.show()
        self.label_picweek6.show()

        self.label_day1.show()
        self.label_day2.show()
        self.label_day3.show()
        self.label_day4.show()
        self.label_day5.show()
        self.label_day6.show()

        self.label_min1.show()
        self.label_min2.show()
        self.label_min3.show()
        self.label_min4.show()
        self.label_min5.show()
        self.label_min6.show()

        self.label_minz1.show()
        self.label_minz2.show()
        self.label_minz3.show()
        self.label_minz4.show()
        self.label_minz5.show()
        self.label_minz6.show()

        self.label_max1.show()
        self.label_max2.show()
        self.label_max3.show()
        self.label_max4.show()
        self.label_max5.show()
        self.label_max6.show()

        self.label_maxz1.show()
        self.label_maxz2.show()
        self.label_maxz3.show()
        self.label_maxz4.show()
        self.label_maxz5.show()
        self.label_maxz6.show()

        self.label_week1.show()
        self.label_week2.show()
        self.label_week3.show()
        self.label_week4.show()
        self.label_week5.show()
        self.label_week6.show()

        self.label_ch1.show()
        self.label_ch2.show()
        self.label_ch3.show()
        self.label_ch4.show()
        self.label_ch5.show()
        self.label_ch6.show()
    def btn_use2(self):
        self.pushButton_4.setText('⚪')
        self.pushButton_5.setText('⚫')
        self.label_todayday.show()
        self.label_todaymorning.show()
        self.label_todayafter.show()
        self.label_todaynight.show()
        self.label_pic1.show()
        self.label_pic2.show()
        self.label_pic3.show()
        self.label_pic4.show()
        self.label_nighttemp.show()
        self.label_morningtemp.show()
        self.label_daytemp.show()
        self.label_aftertemp.show()
        self.label.show()
        self.label_2.show()
        self.label_3.show()
        self.label_7.show()
        self.label_6.show()
        self.label_5.show()
        self.label_pressure.show()
        self.label_feels.show()
        self.label_wind.show()
        self.label_cloudiness.show()
        self.label_sunrise.show()
        self.label_sunset.show()
        self.line_2.show()

        self.label_picweek1.hide()
        self.label_picweek2.hide()
        self.label_picweek3.hide()
        self.label_picweek4.hide()
        self.label_picweek5.hide()
        self.label_picweek6.hide()

        self.label_day1.hide()
        self.label_day2.hide()
        self.label_day3.hide()
        self.label_day4.hide()
        self.label_day5.hide()
        self.label_day6.hide()

        self.label_min1.hide()
        self.label_min2.hide()
        self.label_min3.hide()
        self.label_min4.hide()
        self.label_min5.hide()
        self.label_min6.hide()

        self.label_minz1.hide()
        self.label_minz2.hide()
        self.label_minz3.hide()
        self.label_minz4.hide()
        self.label_minz5.hide()
        self.label_minz6.hide()

        self.label_max1.hide()
        self.label_max2.hide()
        self.label_max3.hide()
        self.label_max4.hide()
        self.label_max5.hide()
        self.label_max6.hide()

        self.label_maxz1.hide()
        self.label_maxz2.hide()
        self.label_maxz3.hide()
        self.label_maxz4.hide()
        self.label_maxz5.hide()
        self.label_maxz6.hide()

        self.label_week1.hide()
        self.label_week2.hide()
        self.label_week3.hide()
        self.label_week4.hide()
        self.label_week5.hide()
        self.label_week6.hide()

        self.label_ch1.hide()
        self.label_ch2.hide()
        self.label_ch3.hide()
        self.label_ch4.hide()
        self.label_ch5.hide()
        self.label_ch6.hide()
    def btn_svern(self):
        self.showMinimized()

    def btn_find(self):
        try:
            global urll, rr, ssoup
            urll = 'https://sinoptik.ua/погода-'+ self.lineEdit_2.text()
            rr = requests.get(urll)
            ssoup = BeautifulSoup(rr.text, 'html.parser')
            print(urll)
            main()
            self.update()
        except:
            error_message = QtWidgets.QErrorMessage(self)
            radius = 30
            error_message.setStyleSheet(
                """
                color: white;
                background:black;
                border-top-left-radius:{0}px;
                border-bottom-left-radius:{0}px;
                border-top-right-radius:{0}px;
                border-bottom-right-radius:{0}px;
                """.format(radius))
            error_message.setWindowTitle("Ошибка")
            error_message.showMessage("Неверно указан город/страна")

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()
            event.accept()


def parcing_maintemp():
    temp = ssoup.find('p', class_='today-temp')
    Str = str(temp.text)
    Remove_last = Str[:-1]
    return Remove_last
def parcing_city():
    temp = ssoup.find('div', class_='cityName cityNameShort').find('strong')
    # temp = soup.find('p', id='form-search-examples').nextSibling
    return temp.text
def parcing_feelslike():
    temp = ssoup.find('p', class_='today-temp')
    Str = str(temp.text)
    Remove_last = Str[:-1]
    return Remove_last
def parcing_wind():
    temp = ssoup.find_all('tr', class_='gray')[2].find_all('td')[5]
    return temp.text
def parcing_pressure():
    temp = ssoup.find_all('tr', class_='gray')[1].find_all('td')[5]
    return temp.text + 'мм'
def parcing_vlaga():
    temp = ssoup.find_all('table', class_='weatherDetails')[0].find_all('tr')[6].find_all('td')[3]
    return temp.text + '%'
def parcing_surise():
    temp = ssoup.find('div', class_='infoDaylight').find('span')
    return temp.text
def parcing_sunset():
    temp = ssoup.find('div', class_='infoDaylight').find_all('span')[1]
    return temp.text
def parcing_nowdate():
    temp = ssoup.find('p', class_='date dateFree')
    return temp.text
def parcing_nowmonth():
    temp = ssoup.find('p', class_='month')
    return temp.text
def parcing_week():
    temp = soup.find('div', class_='day-week')
    return temp.text
def parcing_night():
    temp = ssoup.find_all('td', colspan='2')[0]
    return temp.text.capitalize()
def parcing_nighttemp():
    temp = ssoup.find('tr', class_='temperature').find_all('td')[1]
    return temp.text
def parcing_morning():
    temp = ssoup.find_all('td', colspan='2')[1]
    return temp.text.capitalize()
def parcing_morningtemp():
    temp = ssoup.find('tr', class_='temperature').find_all('td')[3]
    return temp.text
def parcing_day():
    temp = ssoup.find_all('td', colspan='2')[2]
    return temp.text.capitalize()
def parcing_daytemp():
    temp = ssoup.find('tr', class_='temperature').find_all('td')[5]
    return temp.text
def parcing_after():
    temp = ssoup.find_all('td', colspan='2')[3]
    return temp.text.capitalize()
def parcing_aftertemp():
    temp = ssoup.find('tr', class_='temperature').find_all('td')[7]
    return temp.text
def parcing_country():
    temp = ssoup.find('div', class_='city').find('span')
    return temp.text
def parcing_week2():
    temp = ssoup.find('div', class_='main', id='bd2').find(class_='day-link')
    return temp.text
def parcing_week3():
    temp = ssoup.find('div', class_='main', id='bd3').find(class_='day-link')
    return temp.text
def parcing_week4():
    temp = ssoup.find('div', class_='main', id='bd4').find(class_='day-link')
    return temp.text
def parcing_week5():
    temp = ssoup.find('div', class_='main', id='bd5').find(class_='day-link')
    return temp.text
def parcing_week6():
    temp = ssoup.find('div', class_='main', id='bd6').find(class_='day-link')
    return temp.text
def parcing_week7():
    temp = ssoup.find('div', class_='main', id='bd7').find(class_='day-link')
    return temp.text
def parcing_day1():
    temp = ssoup.find('div', class_='main', id='bd2').find(class_='date').text
    return temp
def parcing_day2():
    temp = ssoup.find('div', class_='main', id='bd3').find(class_='date').text
    return temp
def parcing_day3():
    temp = ssoup.find('div', class_='main', id='bd4').find(class_='date').text
    return temp
def parcing_day4():
    temp = ssoup.find('div', class_='main', id='bd5').find(class_='date').text
    return temp
def parcing_day5():
    temp = ssoup.find('div', class_='main', id='bd6').find(class_='date').text
    return temp
def parcing_day6():
    temp = ssoup.find('div', class_='main', id='bd7').find(class_='date').text
    return temp
def parcing_ch1():
    temp = ssoup.find('div', class_='main', id='bd2').find(class_='month').text
    return temp
def parcing_ch2():
    temp = ssoup.find('div', class_='main', id='bd3').find(class_='month').text
    return temp
def parcing_ch3():
    temp = ssoup.find('div', class_='main', id='bd4').find(class_='month').text
    return temp
def parcing_ch4():
    temp = ssoup.find('div', class_='main', id='bd5').find(class_='month').text
    return temp
def parcing_ch5():
    temp = ssoup.find('div', class_='main', id='bd6').find(class_='month').text
    return temp
def parcing_ch6():
    temp = ssoup.find('div', class_='main', id='bd7').find(class_='month').text
    return temp
def parcing_min1():
    temp = ssoup.find('div', class_='main', id='bd2').find('div', class_='min').find('span').text
    return temp
def parcing_min2():
    temp = ssoup.find('div', class_='main', id='bd3').find('div', class_='min').find('span').text
    return temp
def parcing_min3():
    temp = ssoup.find('div', class_='main', id='bd4').find('div', class_='min').find('span').text
    return temp
def parcing_min4():
    temp = ssoup.find('div', class_='main', id='bd5').find('div', class_='min').find('span').text
    return temp
def parcing_min5():
    temp = ssoup.find('div', class_='main', id='bd6').find('div', class_='min').find('span').text
    return temp
def parcing_min6():
    temp = ssoup.find('div', class_='main', id='bd7').find('div', class_='min').find('span').text
    return temp
def parcing_max1():
    temp = ssoup.find('div', class_='main', id='bd2').find('div', class_='max').find('span').text
    return temp
def parcing_max2():
    temp = ssoup.find('div', class_='main', id='bd3').find('div', class_='max').find('span').text
    return temp
def parcing_max3():
    temp = ssoup.find('div', class_='main', id='bd4').find('div', class_='max').find('span').text
    return temp
def parcing_max4():
    temp = ssoup.find('div', class_='main', id='bd5').find('div', class_='max').find('span').text
    return temp
def parcing_max5():
    temp = ssoup.find('div', class_='main', id='bd6').find('div', class_='max').find('span').text
    return temp
def parcing_max6():
    temp = ssoup.find('div', class_='main', id='bd7').find('div', class_='max').find('span').text
    return temp
def main():
    window.label_minz1.setText(parcing_min1())
    window.label_minz2.setText(parcing_min2())
    window.label_minz3.setText(parcing_min3())
    window.label_minz4.setText(parcing_min4())
    window.label_minz5.setText(parcing_min5())
    window.label_minz6.setText(parcing_min6())
    window.label_maxz1.setText(parcing_max1())
    window.label_maxz2.setText(parcing_max2())
    window.label_maxz3.setText(parcing_max3())
    window.label_maxz4.setText(parcing_max4())
    window.label_maxz5.setText(parcing_max5())
    window.label_maxz6.setText(parcing_max6())
    window.label_ch1.setText(parcing_ch1())
    window.label_ch2.setText(parcing_ch2())
    window.label_ch3.setText(parcing_ch3())
    window.label_ch4.setText(parcing_ch4())
    window.label_ch5.setText(parcing_ch5())
    window.label_ch6.setText(parcing_ch6())
    window.label_day1.setText(parcing_day1())
    window.label_day2.setText(parcing_day2())
    window.label_day3.setText(parcing_day3())
    window.label_day4.setText(parcing_day4())
    window.label_day5.setText(parcing_day5())
    window.label_day6.setText(parcing_day6())
    window.label_week1.setText(parcing_week2())
    window.label_week2.setText(parcing_week3())
    window.label_week3.setText(parcing_week4())
    window.label_week4.setText(parcing_week5())
    window.label_week5.setText(parcing_week6())
    window.label_week6.setText(parcing_week7())
    window.label_12.setText(parcing_city() + " " + parcing_maintemp())
    window.label_feels.setText(parcing_feelslike())
    window.label_wind.setText(parcing_wind() + 'м/с')
    window.label_pressure.setText(parcing_pressure())
    window.label_cloudiness.setText(parcing_vlaga())
    window.label_sunrise.setText(parcing_surise())
    window.label_sunset.setText(parcing_sunset())
    window.label_8.setText(parcing_nowdate() + " " + parcing_nowmonth())
    window.label_10.setText(parcing_week())

    window.label_todaynight.setText(parcing_night())
    window.label_nighttemp.setText(parcing_nighttemp())
    window.label_todaymorning.setText(parcing_morning())
    window.label_morningtemp.setText(parcing_morningtemp())
    window.label_todayday.setText(parcing_day())
    window.label_daytemp.setText(parcing_daytemp())
    window.label_todayafter.setText(parcing_after())
    window.label_aftertemp.setText(parcing_aftertemp())
    window.label_9.setText(parcing_country())

    picnightb = QPixmap("icons/nightcloudbig.png")
    piccloudb = QPixmap("icons/cloudbig.png")
    piccloudsb = QPixmap("icons/cloudsbig.png")
    picrainb = QPixmap("icons/rainbig.png")
    picwindb = QPixmap("icons/windbig.png")
    picsnowb = QPixmap("icons/snowbig.png")
    picsunnyb = QPixmap("icons/sunnybig.png")
    picpartlyb = QPixmap("icons/partlycloudbig.png")
    piclightb = QPixmap("icons/lightingbig.png")

    picnights = QPixmap("icons/nightcloudsmall.png")
    picclouds = QPixmap("icons/cloudsmall.png")
    piccloudss = QPixmap("icons/cloudssmall.png")
    picrains = QPixmap("icons/rainsmall.png")
    picwinds = QPixmap("icons/windsmall.png")
    picsnows = QPixmap("icons/snowsmall.png")
    picsunnys = QPixmap("icons/sunnysmall.png")
    picpartlys = QPixmap("icons/partlycloudsmall.png")
    piclights = QPixmap("icons/lightingsmall.png")

    temp = ssoup.find('div', class_='main loaded', id='bd1').find('div')['title']
    if temp == 'Сплошная облачность, мелкий дождь':
        window.label_picmain.setPixmap(picrainb)
    if temp == 'Облачно с прояснениями':
        window.label_picmain.setPixmap(picpartlyb)
    if temp == 'Ясно':
        window.label_picmain.setPixmap(picsunnyb)
    if temp == 'Сплошная облачность, дождь':
        window.label_picmain.setPixmap(picrainb)
    if temp == 'Сплошная облачность':
        window.label_picmain.setPixmap(piccloudsb)
    if temp == 'Облачно с прояснениями, снег':
        window.label_picmain.setPixmap(picsnowb)
    if temp == 'Небольшая облачность':
        window.label_picmain.setPixmap(picpartlyb)
    if temp == 'Переменная облачность':
        window.label_picmain.setPixmap(picpartlyb)
    if temp == 'Сплошная облачность, дождь, грозы':
        window.label_picmain.setPixmap(piclightb)

    temp = ssoup.find('div', class_='main', id='bd2').find('div')['title']
    if temp == 'Сплошная облачность, мелкий дождь':
        window.label_picweek1.setPixmap(picrains)
    if temp == 'Облачно с прояснениями':
        window.label_picweek1.setPixmap(picpartlys)
    if temp == 'Ясно':
        window.label_picweek1.setPixmap(picsunnys)
    if temp == 'Сплошная облачность, дождь':
        window.label_picweek1.setPixmap(picrains)
    if temp == 'Сплошная облачность':
        window.label_picweek1.setPixmap(piccloudss)
    if temp == 'Облачно с прояснениями, снег':
        window.label_picweek1.setPixmap(picsnows)
    if temp == 'Небольшая облачность':
        window.label_picweek1.setPixmap(picpartlys)
    if temp == 'Переменная облачность':
        window.label_picweek1.setPixmap(picpartlys)
    if temp == 'Сплошная облачность, дождь, грозы':
        window.label_picweek1.setPixmap(piclights)

    temp = ssoup.find('div', class_='main', id='bd3').find('div')['title']
    if temp == 'Сплошная облачность, мелкий дождь':
        window.label_picweek2.setPixmap(picrains)
    if temp == 'Облачно с прояснениями':
        window.label_picweek2.setPixmap(picpartlys)
    if temp == 'Ясно':
        window.label_picweek2.setPixmap(picsunnys)
    if temp == 'Сплошная облачность, дождь':
        window.label_picweek2.setPixmap(picrains)
    if temp == 'Сплошная облачность':
        window.label_picweek2.setPixmap(piccloudss)
    if temp == 'Облачно с прояснениями, снег':
        window.label_picweek2.setPixmap(picsnows)
    if temp == 'Небольшая облачность':
        window.label_picweek2.setPixmap(picpartlys)
    if temp == 'Переменная облачность':
        window.label_picweek2.setPixmap(picpartlys)
    if temp == 'Сплошная облачность, дождь, грозы':
        window.label_picweek2.setPixmap(piclights)

    temp = ssoup.find('div', class_='main', id='bd4').find('div')['title']
    if temp == 'Сплошная облачность, мелкий дождь':
        window.label_picweek3.setPixmap(picrains)
    if temp == 'Облачно с прояснениями':
        window.label_picweek3.setPixmap(picpartlys)
    if temp == 'Ясно':
        window.label_picweek3.setPixmap(picsunnys)
    if temp == 'Сплошная облачность, дождь':
        window.label_picweek3.setPixmap(picrains)
    if temp == 'Сплошная облачность':
        window.label_picweek3.setPixmap(piccloudss)
    if temp == 'Облачно с прояснениями, снег':
        window.label_picweek3.setPixmap(picsnows)
    if temp == 'Небольшая облачность':
        window.label_picweek3.setPixmap(picpartlys)
    if temp == 'Переменная облачность':
        window.label_picweek3.setPixmap(picpartlys)
    if temp == 'Сплошная облачность, дождь, грозы':
        window.label_picweek3.setPixmap(piclights)

    temp = ssoup.find('div', class_='main', id='bd5').find('div')['title']
    if temp == 'Сплошная облачность, мелкий дождь':
        window.label_picweek4.setPixmap(picrains)
    if temp == 'Облачно с прояснениями':
        window.label_picweek4.setPixmap(picpartlys)
    if temp == 'Ясно':
        window.label_picweek4.setPixmap(picsunnys)
    if temp == 'Сплошная облачность, дождь':
        window.label_picweek4.setPixmap(picrains)
    if temp == 'Сплошная облачность':
        window.label_picweek4.setPixmap(piccloudss)
    if temp == 'Облачно с прояснениями, снег':
        window.label_picweek4.setPixmap(picsnows)
    if temp == 'Небольшая облачность':
        window.label_picweek4.setPixmap(picpartlys)
    if temp == 'Переменная облачность':
        window.label_picweek4.setPixmap(picpartlys)
    if temp == 'Сплошная облачность, дождь, грозы':
        window.label_picweek4.setPixmap(piclights)

    temp = ssoup.find('div', class_='main', id='bd6').find('div')['title']
    if temp == 'Сплошная облачность, мелкий дождь':
        window.label_picweek5.setPixmap(picrains)
    if temp == 'Облачно с прояснениями':
        window.label_picweek5.setPixmap(picpartlys)
    if temp == 'Ясно':
        window.label_picweek5.setPixmap(picsunnys)
    if temp == 'Сплошная облачность, дождь':
        window.label_picweek5.setPixmap(picrains)
    if temp == 'Сплошная облачность':
        window.label_picweek5.setPixmap(piccloudss)
    if temp == 'Облачно с прояснениями, снег':
        window.label_picweek5.setPixmap(picsnows)
    if temp == 'Небольшая облачность':
        window.label_picweek5.setPixmap(picpartlys)
    if temp == 'Переменная облачность':
        window.label_picweek5.setPixmap(picpartlys)
    if temp == 'Сплошная облачность, дождь, грозы':
        window.label_picweek5.setPixmap(piclights)

    temp = ssoup.find('div', class_='main', id='bd7').find('div')['title']
    if temp == 'Сплошная облачность, мелкий дождь':
        window.label_picweek6.setPixmap(picrains)
    if temp == 'Облачно с прояснениями':
        window.label_picweek6.setPixmap(picpartlys)
    if temp == 'Ясно':
        window.label_picweek6.setPixmap(picsunnys)
    if temp == 'Сплошная облачность, дождь':
        window.label_picweek6.setPixmap(picrains)
    if temp == 'Сплошная облачность':
        window.label_picweek6.setPixmap(piccloudss)
    if temp == 'Облачно с прояснениями, снег':
        window.label_picweek6.setPixmap(picsnows)
    if temp == 'Небольшая облачность':
        window.label_picweek6.setPixmap(picpartlys)
    if temp == 'Переменная облачность':
        window.label_picweek6.setPixmap(picpartlys)
    if temp == 'Сплошная облачность, дождь, грозы':
        window.label_picweek6.setPixmap(piclights)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()

    urll = 'https://sinoptik.ua/погода-москва'
    rr = requests.get(urll)
    ssoup = BeautifulSoup(rr.text, 'html.parser')
    temp = ssoup.find('div', class_='main loaded', id='bd1').find('div')['title']
    print(temp)
    main()

    window.show()
    sys.exit(app.exec())