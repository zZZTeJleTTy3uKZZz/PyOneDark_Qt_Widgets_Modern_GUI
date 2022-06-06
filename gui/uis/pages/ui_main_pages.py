# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pages.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(860, 456)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.p_auth = QWidget()
        self.p_auth.setObjectName(u"p_auth")
        self.p_auth.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.p_auth)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.welcome_base = QFrame(self.p_auth)
        self.welcome_base.setObjectName(u"welcome_base")
        self.welcome_base.setMinimumSize(QSize(300, 150))
        self.welcome_base.setMaximumSize(QSize(300, 150))
        self.welcome_base.setFrameShape(QFrame.NoFrame)
        self.welcome_base.setFrameShadow(QFrame.Raised)
        self.center_page_layout = QVBoxLayout(self.welcome_base)
        self.center_page_layout.setSpacing(10)
        self.center_page_layout.setObjectName(u"center_page_layout")
        self.center_page_layout.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.welcome_base)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(300, 120))
        self.logo.setMaximumSize(QSize(300, 120))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.logo_layout = QVBoxLayout(self.logo)
        self.logo_layout.setSpacing(0)
        self.logo_layout.setObjectName(u"logo_layout")
        self.logo_layout.setContentsMargins(0, 0, 0, 0)

        self.center_page_layout.addWidget(self.logo)

        self.label = QLabel(self.welcome_base)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.center_page_layout.addWidget(self.label)


        self.page_1_layout.addWidget(self.welcome_base, 0, Qt.AlignHCenter)

        self.pages.addWidget(self.p_auth)
        self.p_team = QWidget()
        self.p_team.setObjectName(u"p_team")
        self.p_team__l = QVBoxLayout(self.p_team)
        self.p_team__l.setSpacing(5)
        self.p_team__l.setObjectName(u"p_team__l")
        self.p_team__l.setContentsMargins(5, 5, 5, 5)
        self.scroll_area = QScrollArea(self.p_team)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 840, 436))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setPointSize(16)
        self.title_label.setFont(font1)
        self.title_label.setStyleSheet(u"font-size: 16pt")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.verticalSpacer = QSpacerItem(10, 15, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.row_1_layout = QHBoxLayout()
        self.row_1_layout.setObjectName(u"row_1_layout")

        self.verticalLayout.addLayout(self.row_1_layout)

        self.row_2_layout = QHBoxLayout()
        self.row_2_layout.setObjectName(u"row_2_layout")

        self.verticalLayout.addLayout(self.row_2_layout)

        self.row_3_layout = QHBoxLayout()
        self.row_3_layout.setObjectName(u"row_3_layout")

        self.verticalLayout.addLayout(self.row_3_layout)

        self.row_4_layout = QVBoxLayout()
        self.row_4_layout.setObjectName(u"row_4_layout")

        self.verticalLayout.addLayout(self.row_4_layout)

        self.row_5_layout = QVBoxLayout()
        self.row_5_layout.setObjectName(u"row_5_layout")

        self.verticalLayout.addLayout(self.row_5_layout)

        self.scroll_area.setWidget(self.contents)

        self.p_team__l.addWidget(self.scroll_area)

        self.pages.addWidget(self.p_team)
        self.p_storonnik = QWidget()
        self.p_storonnik.setObjectName(u"p_storonnik")
        self.verticalLayout_3 = QVBoxLayout(self.p_storonnik)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scroll_area_2 = QScrollArea(self.p_storonnik)
        self.scroll_area_2.setObjectName(u"scroll_area_2")
        self.scroll_area_2.setStyleSheet(u"background: transparent;")
        self.scroll_area_2.setFrameShape(QFrame.NoFrame)
        self.scroll_area_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_2.setWidgetResizable(True)
        self.contents_2 = QWidget()
        self.contents_2.setObjectName(u"contents_2")
        self.contents_2.setGeometry(QRect(0, 0, 832, 428))
        self.contents_2.setStyleSheet(u"background: transparent;")
        self.verticalLayout_2 = QVBoxLayout(self.contents_2)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.title_label_2 = QLabel(self.contents_2)
        self.title_label_2.setObjectName(u"title_label_2")
        self.title_label_2.setMaximumSize(QSize(16777215, 40))
        self.title_label_2.setFont(font1)
        self.title_label_2.setStyleSheet(u"font-size: 16pt")
        self.title_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.title_label_2)

        self.verticalSpacer_2 = QSpacerItem(10, 15, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.row_1_layout_2 = QHBoxLayout()
        self.row_1_layout_2.setObjectName(u"row_1_layout_2")

        self.verticalLayout_2.addLayout(self.row_1_layout_2)

        self.row_2_layout_2 = QHBoxLayout()
        self.row_2_layout_2.setObjectName(u"row_2_layout_2")

        self.verticalLayout_2.addLayout(self.row_2_layout_2)

        self.row_3_layout_2 = QHBoxLayout()
        self.row_3_layout_2.setObjectName(u"row_3_layout_2")

        self.verticalLayout_2.addLayout(self.row_3_layout_2)

        self.row_4_layout_2 = QVBoxLayout()
        self.row_4_layout_2.setObjectName(u"row_4_layout_2")

        self.verticalLayout_2.addLayout(self.row_4_layout_2)

        self.row_5_layout_2 = QVBoxLayout()
        self.row_5_layout_2.setObjectName(u"row_5_layout_2")

        self.verticalLayout_2.addLayout(self.row_5_layout_2)

        self.scroll_area_2.setWidget(self.contents_2)

        self.verticalLayout_3.addWidget(self.scroll_area_2)

        self.pages.addWidget(self.p_storonnik)
        self.p_event = QWidget()
        self.p_event.setObjectName(u"p_event")
        self.verticalLayout_5 = QVBoxLayout(self.p_event)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scroll_area_3 = QScrollArea(self.p_event)
        self.scroll_area_3.setObjectName(u"scroll_area_3")
        self.scroll_area_3.setStyleSheet(u"background: transparent;")
        self.scroll_area_3.setFrameShape(QFrame.NoFrame)
        self.scroll_area_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_3.setWidgetResizable(True)
        self.contents_3 = QWidget()
        self.contents_3.setObjectName(u"contents_3")
        self.contents_3.setGeometry(QRect(0, 0, 832, 428))
        self.contents_3.setStyleSheet(u"background: transparent;")
        self.verticalLayout_4 = QVBoxLayout(self.contents_3)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.title_label_3 = QLabel(self.contents_3)
        self.title_label_3.setObjectName(u"title_label_3")
        self.title_label_3.setMaximumSize(QSize(16777215, 40))
        self.title_label_3.setFont(font1)
        self.title_label_3.setStyleSheet(u"font-size: 16pt")
        self.title_label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.title_label_3)

        self.verticalSpacer_3 = QSpacerItem(10, 15, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.row_1_layout_3 = QHBoxLayout()
        self.row_1_layout_3.setObjectName(u"row_1_layout_3")

        self.verticalLayout_4.addLayout(self.row_1_layout_3)

        self.row_2_layout_3 = QHBoxLayout()
        self.row_2_layout_3.setObjectName(u"row_2_layout_3")

        self.verticalLayout_4.addLayout(self.row_2_layout_3)

        self.row_3_layout_3 = QHBoxLayout()
        self.row_3_layout_3.setObjectName(u"row_3_layout_3")

        self.verticalLayout_4.addLayout(self.row_3_layout_3)

        self.row_4_layout_3 = QVBoxLayout()
        self.row_4_layout_3.setObjectName(u"row_4_layout_3")

        self.verticalLayout_4.addLayout(self.row_4_layout_3)

        self.row_5_layout_3 = QVBoxLayout()
        self.row_5_layout_3.setObjectName(u"row_5_layout_3")

        self.verticalLayout_4.addLayout(self.row_5_layout_3)

        self.scroll_area_3.setWidget(self.contents_3)

        self.verticalLayout_5.addWidget(self.scroll_area_3)

        self.pages.addWidget(self.p_event)
        self.p_kpi = QWidget()
        self.p_kpi.setObjectName(u"p_kpi")
        self.verticalLayout_7 = QVBoxLayout(self.p_kpi)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.scroll_area_4 = QScrollArea(self.p_kpi)
        self.scroll_area_4.setObjectName(u"scroll_area_4")
        self.scroll_area_4.setStyleSheet(u"background: transparent;")
        self.scroll_area_4.setFrameShape(QFrame.NoFrame)
        self.scroll_area_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_4.setWidgetResizable(True)
        self.contents_4 = QWidget()
        self.contents_4.setObjectName(u"contents_4")
        self.contents_4.setGeometry(QRect(0, 0, 832, 428))
        self.contents_4.setStyleSheet(u"background: transparent;")
        self.verticalLayout_6 = QVBoxLayout(self.contents_4)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.title_label_4 = QLabel(self.contents_4)
        self.title_label_4.setObjectName(u"title_label_4")
        self.title_label_4.setMaximumSize(QSize(16777215, 40))
        self.title_label_4.setFont(font1)
        self.title_label_4.setStyleSheet(u"font-size: 16pt")
        self.title_label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.title_label_4)

        self.verticalSpacer_4 = QSpacerItem(10, 15, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.row_1_layout_4 = QHBoxLayout()
        self.row_1_layout_4.setObjectName(u"row_1_layout_4")

        self.verticalLayout_6.addLayout(self.row_1_layout_4)

        self.row_2_layout_4 = QHBoxLayout()
        self.row_2_layout_4.setObjectName(u"row_2_layout_4")

        self.verticalLayout_6.addLayout(self.row_2_layout_4)

        self.row_3_layout_4 = QHBoxLayout()
        self.row_3_layout_4.setObjectName(u"row_3_layout_4")

        self.verticalLayout_6.addLayout(self.row_3_layout_4)

        self.row_4_layout_4 = QVBoxLayout()
        self.row_4_layout_4.setObjectName(u"row_4_layout_4")

        self.verticalLayout_6.addLayout(self.row_4_layout_4)

        self.row_5_layout_4 = QVBoxLayout()
        self.row_5_layout_4.setObjectName(u"row_5_layout_4")

        self.verticalLayout_6.addLayout(self.row_5_layout_4)

        self.scroll_area_4.setWidget(self.contents_4)

        self.verticalLayout_7.addWidget(self.scroll_area_4)

        self.pages.addWidget(self.p_kpi)
        self.p_quote = QWidget()
        self.p_quote.setObjectName(u"p_quote")
        self.verticalLayout_9 = QVBoxLayout(self.p_quote)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.scroll_area_5 = QScrollArea(self.p_quote)
        self.scroll_area_5.setObjectName(u"scroll_area_5")
        self.scroll_area_5.setStyleSheet(u"background: transparent;")
        self.scroll_area_5.setFrameShape(QFrame.NoFrame)
        self.scroll_area_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_5.setWidgetResizable(True)
        self.contents_5 = QWidget()
        self.contents_5.setObjectName(u"contents_5")
        self.contents_5.setGeometry(QRect(0, 0, 832, 428))
        self.contents_5.setStyleSheet(u"background: transparent;")
        self.verticalLayout_8 = QVBoxLayout(self.contents_5)
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.title_label_5 = QLabel(self.contents_5)
        self.title_label_5.setObjectName(u"title_label_5")
        self.title_label_5.setMaximumSize(QSize(16777215, 40))
        self.title_label_5.setFont(font1)
        self.title_label_5.setStyleSheet(u"font-size: 16pt")
        self.title_label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.title_label_5)

        self.verticalSpacer_5 = QSpacerItem(10, 15, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_8.addItem(self.verticalSpacer_5)

        self.row_1_layout_5 = QHBoxLayout()
        self.row_1_layout_5.setObjectName(u"row_1_layout_5")

        self.verticalLayout_8.addLayout(self.row_1_layout_5)

        self.row_2_layout_5 = QHBoxLayout()
        self.row_2_layout_5.setObjectName(u"row_2_layout_5")

        self.verticalLayout_8.addLayout(self.row_2_layout_5)

        self.row_3_layout_5 = QHBoxLayout()
        self.row_3_layout_5.setObjectName(u"row_3_layout_5")

        self.verticalLayout_8.addLayout(self.row_3_layout_5)

        self.row_4_layout_5 = QVBoxLayout()
        self.row_4_layout_5.setObjectName(u"row_4_layout_5")

        self.verticalLayout_8.addLayout(self.row_4_layout_5)

        self.row_5_layout_5 = QVBoxLayout()
        self.row_5_layout_5.setObjectName(u"row_5_layout_5")

        self.verticalLayout_8.addLayout(self.row_5_layout_5)

        self.scroll_area_5.setWidget(self.contents_5)

        self.verticalLayout_9.addWidget(self.scroll_area_5)

        self.pages.addWidget(self.p_quote)
        self.p_hub = QWidget()
        self.p_hub.setObjectName(u"p_hub")
        self.verticalLayout_11 = QVBoxLayout(self.p_hub)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.scroll_area_6 = QScrollArea(self.p_hub)
        self.scroll_area_6.setObjectName(u"scroll_area_6")
        self.scroll_area_6.setStyleSheet(u"background: transparent;")
        self.scroll_area_6.setFrameShape(QFrame.NoFrame)
        self.scroll_area_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_6.setWidgetResizable(True)
        self.contents_6 = QWidget()
        self.contents_6.setObjectName(u"contents_6")
        self.contents_6.setGeometry(QRect(0, 0, 832, 428))
        self.contents_6.setStyleSheet(u"background: transparent;")
        self.verticalLayout_10 = QVBoxLayout(self.contents_6)
        self.verticalLayout_10.setSpacing(15)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.title_label_6 = QLabel(self.contents_6)
        self.title_label_6.setObjectName(u"title_label_6")
        self.title_label_6.setMaximumSize(QSize(16777215, 40))
        self.title_label_6.setFont(font1)
        self.title_label_6.setStyleSheet(u"font-size: 16pt")
        self.title_label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.title_label_6)

        self.verticalSpacer_6 = QSpacerItem(10, 15, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_10.addItem(self.verticalSpacer_6)

        self.row_1_layout_6 = QHBoxLayout()
        self.row_1_layout_6.setObjectName(u"row_1_layout_6")

        self.verticalLayout_10.addLayout(self.row_1_layout_6)

        self.row_2_layout_6 = QHBoxLayout()
        self.row_2_layout_6.setObjectName(u"row_2_layout_6")

        self.verticalLayout_10.addLayout(self.row_2_layout_6)

        self.row_3_layout_6 = QHBoxLayout()
        self.row_3_layout_6.setObjectName(u"row_3_layout_6")

        self.verticalLayout_10.addLayout(self.row_3_layout_6)

        self.row_4_layout_6 = QVBoxLayout()
        self.row_4_layout_6.setObjectName(u"row_4_layout_6")

        self.verticalLayout_10.addLayout(self.row_4_layout_6)

        self.row_5_layout_6 = QVBoxLayout()
        self.row_5_layout_6.setObjectName(u"row_5_layout_6")

        self.verticalLayout_10.addLayout(self.row_5_layout_6)

        self.scroll_area_6.setWidget(self.contents_6)

        self.verticalLayout_11.addWidget(self.scroll_area_6)

        self.pages.addWidget(self.p_hub)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"\u041f\u0430\u0440\u0442\u0438\u044f \u00ab\u041d\u043e\u0432\u044b\u0435 \u043b\u044e\u0434\u0438\u00bb", None))
        self.title_label.setText(QCoreApplication.translate("MainPages", u"\u041a\u043e\u043c\u0430\u043d\u0434\u0430", None))
        self.title_label_2.setText(QCoreApplication.translate("MainPages", u"\u0421\u0442\u043e\u0440\u043e\u043d\u043d\u0438\u043a\u0438", None))
        self.title_label_3.setText(QCoreApplication.translate("MainPages", u"\u041c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f", None))
        self.title_label_4.setText(QCoreApplication.translate("MainPages", u"KPI", None))
        self.title_label_5.setText(QCoreApplication.translate("MainPages", u"\u0426\u0438\u0442\u0430\u0442\u044b", None))
        self.title_label_6.setText(QCoreApplication.translate("MainPages", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430", None))
    # retranslateUi

