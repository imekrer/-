from flask import Flask, url_for, redirect, session

app= Flask(__name__)
app.config['SECRET KEY']='kjflwejgvvl;xckfjlbjdfkfd'
question_num= None
#главная страница
def index():
    test_url= url_for('test')
    session[question_num]= 0
    print(test_url)
    result= f'''<h1>Главная страница</h1>
    <h3>Список виктоин</h3>
    <ul>
        <li><a href='{test_url}'>Виктоина 1</a></li>
        <li>Виктоина 2</li>
        <li>Виктоина 3</li>
    '''
    return result
#тест
def test():
    next_url=url_for('test')
    res= f'''Ворос первый{session[question_num]}
    <br><a href='{next_url}'>Следующий вопрос</a>
    '''
    session[question_num]+= 1
    if session[question_num] >= 4:
        return redirect(url_for('result'))
    return res
def result():
    index_url= url_for('index')
    return f"""<h1>Вы справились</h1>
    <a href='{index_url}'>Перейти на главную</a>
    """

#сайты
app.add_url_rule('/', 'index', index)
app.add_url_rule('/test', 'test', test)
app.add_url_rule('/result', 'result', result)

app.run()