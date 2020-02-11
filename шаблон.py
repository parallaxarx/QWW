"""
Приложение 'Калькулятор'
Автор: "WildWoodRogue"
"""
import sys
from PyQt5.QtWidgets import QApplication,QLabel,QWidget, QPushButton,QMessageBox,QLCDNumber,QLineEdit,QGridLayout
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon

size=65
board=5

countRowButton=5
countColumnButton=5

widthWindow=8*size
hightWindow=8*size

widthButton=widthWindow//8- board
hightButton=hightWindow//8- board

widthLabelBig=widthWindow*5//8 - board
hightLabelBig=hightWindow//4- 2*board

widthLabelSmall=widthWindow*5//8- board
hightLabelSmall=hightWindow//8- 2*board

widthLabelHistory = widthWindow*3//8- 2*board
hightLabelHistory=hightWindow*7//8- 2*board

class Main(QWidget):
    # Работа калькулятора с помощью клавиатуры
    def keyPressEvent(self, event):
        # Двумерный массив сопоставления кодов клавиш к их ключам: 1строка - код, 2строка - ключ
        arrayOfKeys = [['48','49','50','51','52','53','54','55','56','57','16777220','43','45','42','47','16777221','16777219','42','40','41', '46'],
                       ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ,'='       ,'+', '-' , '×','÷',  '='      , '<',      '×',  '(', ')', '.']]
        if (str(event.key()) in arrayOfKeys[0]):
            for ind in range(len(arrayOfKeys[0])):
                if str(event.key()) == arrayOfKeys[0][ind]:
                    key = arrayOfKeys[1][ind]
                    # Счёт
                    if key == "=":
                        try :
                            if "-" not in self.labelSmall.text():
                                output = (self.labelBig.text()+self.labelSmall.text())
                            else:
                                output = (self.labelBig.text()+'('+self.labelSmall.text()+')')
                            countOpenBrackets=output.count("(")
                            countClosedBrackets=output.count(")")
                            if countOpenBrackets>countClosedBrackets:
                                output+=(countOpenBrackets-countClosedBrackets)*")"

                            result = eval("*".join(("/".join(("**".join(output.split("^"))).split("÷"))).split("×")))
                            # result= output.split("^")
                            # result= "**".join(result)
                            self.labelBig.setText(output+"=")
                            self.labelSmall.setText(str(result))
                            #добавление в labelHistory
                            historyBefore=(output+"="+str(result))
                            historyAfter=''
                            counter=0
                            for char in historyBefore:
                                counter+=1
                                historyAfter+=char
                                if counter%21==0:
                                     historyAfter+='\n'
                                     counter=0
                                elif char == "=":
                                    historyAfter=historyAfter[:-1]+'\n='
                                    counter=0
                            self.labelHistory.setText(historyAfter+"\n\n"+self.labelHistory.text())
                        except:
                            print(output)
                    # Цифры
                    elif key in "1234567890":
                        if '=' not in self.labelBig.text():
                            self.labelSmall.setText(self.labelSmall.text()+key)
                            if self.labelBig.text()!="":
                                if self.labelBig.text()[-1]==")":
                                    self.labelBig.setText(self.labelBig.text()+"×")

                        else:
                            self.labelBig.clear();
                            self.labelSmall.setText(key)
                    # Удаление символа BackSpace
                    elif key=="<":
                        self.labelSmall.setText(self.labelSmall.text()[:-1])
                    # Арифметика
                    elif key in "+-×÷^":
                        if "-" not in self.labelSmall.text():
                            if '=' not in self.labelBig.text():

                                if self.labelSmall.text()!='' and (self.labelSmall.text() !="-"):
                                    self.labelBig.setText(self.labelBig.text()+self.labelSmall.text()+key)
                                    self.labelSmall.setText("")
                                else:
                                    if key=="-":
                                        self.labelSmall.setText('-')
                            else:
                                self.labelBig.setText(self.labelSmall.text()+key)
                                self.labelSmall.setText("")
                        else:
                            if '=' not in self.labelBig.text():
                                if self.labelSmall.text()!='' and (self.labelSmall.text() !="-"):
                                    self.labelBig.setText(self.labelBig.text()+'('+self.labelSmall.text()+')'+key)
                                    self.labelSmall.setText("")
                                else:
                                    if key=="-":
                                        self.labelSmall.setText('-')
                            else:
                                self.labelBig.setText('('+self.labelSmall.text()+')'+key)
                                self.labelSmall.setText("")
                    # Cкобки
                    elif key == "(":
                        if self.labelBig.text() != '':
                            if self.labelBig.text()[-1] == ')':
                                self.labelBig.setText(self.labelBig.text() + '*(')
                            else:
                                self.labelBig.setText(self.labelBig.text() + '(')
                        else:
                            self.labelBig.setText('(')
                    elif key == ")":
                            countOpenBrackets = (list(self.labelBig.text())).count('(')
                            countClosedBrackets = (list(self.labelBig.text())).count(')')

                            if self.labelBig.text() != '':
                                if self.labelBig.text()[-1] == '(':
                                    self.labelBig.setText(self.labelBig.text() + '0' + ')')
                                elif countClosedBrackets < countOpenBrackets:
                                    self.labelBig.setText(self.labelBig.text() + self.labelSmall.text() + ')')
                                    self.labelSmall.setText('')
                    # Точка (исправить)
                    elif key=="." and key not in self.labelSmall.text():
                        self.labelSmall.setText(self.labelSmall.text()+key)


    # Работа калькулятора с помощью мыши
    def calculation(self):
        sender=self.sender()
        key=sender.text()
        print(key)

        #вычесления
        if key =="=":
            try :
                if "-" not in self.labelSmall.text():
                    output = (self.labelBig.text()+self.labelSmall.text())
                else:
                    output = (self.labelBig.text()+'('+self.labelSmall.text()+')')
                countOpenBrackets=output.count("(")
                countClosedBrackets=output.count(")")
                if countOpenBrackets>countClosedBrackets:
                    output+=(countOpenBrackets-countClosedBrackets)*")"

                result = eval("*".join(("/".join(("**".join(output.split("^"))).split("÷"))).split("×")))
                # result= output.split("^")
                # result= "**".join(result)
                self.labelBig.setText(output+"=")
                self.labelSmall.setText(str(result))
                #добавление в labelHistory
                historyBefore=(output+"="+str(result))
                historyAfter=''
                counter=0
                for char in historyBefore:
                    counter+=1
                    historyAfter+=char
                    if counter%21==0:
                         historyAfter+='\n'
                         counter=0
                    elif char == "=":
                        historyAfter=historyAfter[:-1]+'\n='
                        counter=0
                self.labelHistory.setText(historyAfter+"\n\n"+self.labelHistory.text())
            except:
                print(output)
        #смена знака
        elif key=="±":
            if self.labelSmall.text()!="":
                if "-" in self.labelSmall.text():
                    self.labelSmall.setText(self.labelSmall.text()[1:])
                else:
                    self.labelSmall.setText("-"+self.labelSmall.text())
        #факториал
        elif key=='X!':
            if self.labelSmall.text()!="":
                resultFact=1
                fact=str(self.labelSmall.text())
                for i in range(1,int(fact)+1):
                    resultFact*=i
                self.labelSmall.setText(str(resultFact))


        #скобки
        elif key == "(":
            if self.labelBig.text() != '':
                if self.labelBig.text()[-1] == ')':
                    self.labelBig.setText(self.labelBig.text() + '*(')
                else:
                    self.labelBig.setText(self.labelBig.text() + '(')
            else:
                self.labelBig.setText('(')
        elif key == ")":
                countOpenBrackets = (list(self.labelBig.text())).count('(')
                countClosedBrackets = (list(self.labelBig.text())).count(')')

                if self.labelBig.text() != '':
                    if self.labelBig.text()[-1] == '(':
                        self.labelBig.setText(self.labelBig.text() + '0' + ')')
                    elif countClosedBrackets < countOpenBrackets:
                        self.labelBig.setText(self.labelBig.text() + self.labelSmall.text() + ')')
                        self.labelSmall.setText('')
        #корень
        elif key=="√x":
            if self.labelSmall.text()!="":
                resultRoot=float(self.labelSmall.text())
                resultRoot**=0.5
                print(resultRoot)
                self.labelSmall.setText(str(resultRoot))
        #X²
        elif key=="X²":
            if self.labelSmall.text()!="":
                resultRoot=float(self.labelSmall.text())
                resultRoot**=2
                print(resultRoot)
                self.labelSmall.setText(str(resultRoot))
        #1/X
        elif key=="⅟ₓ":
            try:
                if self.labelSmall.text()!="" or self.labelSmall.text()!="0":
                    resultRoot=float(self.labelSmall.text())
                    resultRoot=1/resultRoot
                    print(resultRoot)
                    self.labelSmall.setText(str(resultRoot))
            except ZeroDivisionError:
                pass
        #исключение множественности точек
        elif key=="." and key not in self.labelSmall.text():
            self.labelSmall.setText(self.labelSmall.text()+key)
        #ввод цифр
        elif key in "1234567890":
            if '=' not in self.labelBig.text():
                self.labelSmall.setText(self.labelSmall.text()+key)
                if self.labelBig.text()!="":
                    if self.labelBig.text()[-1]==")":
                        self.labelBig.setText(self.labelBig.text()+"×")

            else:
                self.labelBig.clear();
                self.labelSmall.setText(key)


        # очистка окон кроме истории
        elif key=="C":
            self.labelSmall.setText("")
            self.labelBig.setText("")
        # смена функционала
        elif key=="↑" or key=="↓":
            if self.buttonList[2][3].text()=="X!":
                self.buttonList[2][3].setText("X²")
                self.buttonList[2][4].setText("^")
                self.buttonList[4][2].setText("↓")
            else:
                self.buttonList[2][3].setText('X!')
                self.buttonList[2][4].setText('⅟ₓ')
                self.buttonList[4][2].setText("↑")
        # удаление последнего символа
        elif key=="<":
            self.labelSmall.setText(self.labelSmall.text()[:-1])
        # выполнение основных арифметических операций
        elif key in "+-×÷^":
            if "-" not in self.labelSmall.text():
                if '=' not in self.labelBig.text():

                    if self.labelSmall.text()!='' and (self.labelSmall.text() !="-"):
                        self.labelBig.setText(self.labelBig.text()+self.labelSmall.text()+key)
                        self.labelSmall.setText("")
                    else:
                        if key=="-":
                            self.labelSmall.setText('-')
                else:
                    self.labelBig.setText(self.labelSmall.text()+key)
                    self.labelSmall.setText("")
            else:
                if '=' not in self.labelBig.text():
                    if self.labelSmall.text()!='' and (self.labelSmall.text() !="-"):
                        self.labelBig.setText(self.labelBig.text()+'('+self.labelSmall.text()+')'+key)
                        self.labelSmall.setText("")
                    else:
                        if key=="-":
                            self.labelSmall.setText('-')
                else:
                    self.labelBig.setText('('+self.labelSmall.text()+')'+key)
                    self.labelSmall.setText("")

    def __init__(self):                                                           #создание окна
        super().__init__()
        self.initUI()
        self.setWindowIcon(QIcon('qww.jpg'))
        self.resize(QSize(widthWindow, hightWindow)) #..........................................Размер окна (Ширина, Высота)
        self.setWindowTitle('калькулятор 3000') #......................................Заголовок окна


    def initUI(self):
        # Стили
        self.setStyleSheet("""


            QWidget {

                background-color: #8d2222;;

                position:relative;
                text-align: center;
                border: 5px solid;
                }

            QLineEdit {
                background-color: #6b0000;
                border-radius: 20px;
                color:#fff;
                border: 5px solid;

            }
            #labelBig {
                background-color: #6b0000;
                border-radius: 20px;
                color:#fff;
                border: 5px solid;
            }
            #labelSmall {
                background-color: #6b0000;
                border-radius: 20px;
                color:#fff;
                border: 5px solid;
            }
            #labelHistory {
                background-color: #6b0000;
                border-radius: 20px;
                color:#fff;
                font-size: 19px;
                border: 5px solid;
            }



            QPushButton{
            background-color: #ee6e40;
            color: black;
            border-radius: 30px;
            border: 5px solid;

            font-size: 25px;
            }





        """)

        #ссоздание labels
        self.labelBig=QLabel("",self,objectName="labelBig")
        self.labelBig.resize(widthLabelBig,hightLabelBig)
        self.labelBig.move(board,board)
        self.labelBig.setFont(QFont("Trattatello",size//8))
        self.labelBig.show()

        self.labelSmall=QLabel("",self,objectName="labelSmall")
        self.labelSmall.resize(widthLabelSmall,hightLabelSmall)
        self.labelSmall.move(board,board+hightWindow//4)
        self.labelSmall.setFont(QFont("Trattatello",size//4))
        self.labelSmall.show()

        self.labelHistory=QLabel("",self,objectName="labelHistory")
        self.labelHistory.resize(widthLabelHistory,hightLabelHistory)
        self.labelHistory.move(widthWindow*5//8+board,hightWindow//8+board)
        self.labelHistory.show()
        #создание кнопок
        buttonTextList=[['+','-','×','÷','C'],
                        ['7','8','9','±','<'],
                        ['4','5','6','X²','^'],
                        ['1','2','3','(',')'],
                        ['.','0','↑','√x','=']]
        self.buttonList=[]

        for row in range(countRowButton):
            self.buttonList.append([])

            for col in range(countColumnButton):
                btn = QPushButton(buttonTextList[row][col],self,objectName=("button"+str(row)+str(col)))
                btn.resize(widthButton,hightButton)
                btn.clicked.connect(self.calculation)
                btn.move(board+(board+widthButton)*col,hightWindow*3//8+(board + hightButton)*row)
                self.buttonList[row].append(btn)
                self.buttonList[row][col].show()




# Выполнение программы
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
