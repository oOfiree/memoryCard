
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle, randint
import time

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
questions_list.append(Question('Какой национальности не существует?', 'Смурфы', 'Энцы', 'Алеуты', 'Чулымцы'))
questions_list.append(Question('Какая фигура завершает игру в комбинации "мат легаля" ?', 'Конь', 'Слон', 'Ферзь', 'Пешка'))
questions_list.append(Question('Под каким названием известна единица с последующими ста нулями?', 'Гугол', 'Мегатрон', 'Гигабит', 'Наномоль'))
questions_list.append(Question('Какой химический элемент составляет более половины массы тела человека?', 'Кислород', 'Углерод', 'Кальций', 'Железо'))



app = QApplication([])
main_win = QWidget()
main_win.resize(500, 400)
main_win.setWindowTitle('MemoryCard')

lbl_question = QLabel("Какой-то очень сложный вопрос")
btn_answer = QPushButton("Ответить")


RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Вариант1')
rbtn_2 = QRadioButton('Вариант2')
rbtn_3 = QRadioButton('Вариант3')
rbtn_4 = QRadioButton('Вариант4')

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
RadioGroup.setExclusive(True)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
RadioGroupBox.show()

AnswerGroupBox = QGroupBox("Результат теста")
lbl_ans1 = QLabel("Правильно/неправильно")
lbl_ans2 = QLabel("Правильный ответ")
layout_ans4 = QVBoxLayout()
layout_ans4.addWidget(lbl_ans1, alignment = Qt.AlignLeft) 
layout_ans4.addWidget(lbl_ans2, alignment = Qt.AlignCenter)
AnswerGroupBox.setLayout(layout_ans4)
AnswerGroupBox.hide()


layout_main = QVBoxLayout()

layoutH1 = QHBoxLayout()
layoutH1.addWidget(lbl_question, alignment = Qt.AlignCenter)

layoutH2 = QHBoxLayout()
layoutH2.addWidget(RadioGroupBox)
layoutH2.addWidget(AnswerGroupBox)

layoutH3 = QHBoxLayout()

layoutH3.addWidget(btn_answer)


layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)


main_win.setLayout(layout_main)



def show_answer():
    RadioGroupBox.hide()
    AnswerGroupBox.show()
    btn_answer.setText("Следующий вопрос")

def show_question():
    
    RadioGroupBox.show()
    AnswerGroupBox.hide()
    btn_answer.setText("Ответить")
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)  
 
def click_OK():
    
    if btn_answer.text() == "Ответить":
        check_answer()
    else:
        next_question()

def ask(q):

    lbl_question.setText(q.question)
    lbl_ans2.setText(q.right_answer)
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    show_question()

def check_answer():
    if answer[0].isChecked():
        main_win.score += 1
        show_correct("Правильно!")
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct("Неправильно!")

def show_correct(res):
    
    lbl_ans1.setText(res)
    print("Статистика:")
    print("- всего вопросов:", main_win.total)
    print("- правильных ответов:", main_win.score)
    print("Рейтинг:", int(main_win.score/main_win.total*100),"%")
    show_answer()

def next_question():
    
    cur_question = randint(0, len(questions_list) - 1)
   
    ask(questions_list[cur_question])
    main_win.total += 1   
      

answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
main_win.score = 0
main_win.total = 0

next_question()
btn_answer.clicked.connect(click_OK)

main_win.show()
app.exec_()