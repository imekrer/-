from flask import Flask, url_for, redirect, session, request

data={
    '1': {
        'title':'Викторина 1',
        'questions':[
            {
                'title':'Вопрос 1',
                'answer':[1, 2, 3, 4],
                'right_answer': 0
            },
        'answer':''
        ]
    }
}

app= Flask(__name__)
app.config['SECRET KEY']='kjflwejgvvl;xckfjlbjdfkfd'
question_num= None

#главная страница
def index():
    test_url= url_for('test')
    print(test_url)
    if request.method == 'GET':
        return render_template('index.html', data=data)
        return result
    if request.method == 'POST':
        session['quiz'] = request.form.get['quiz']
        return redirect(url_for('test'))


#тест
def test():
    # if not ('quiz' in session) or int(session[quiz]) <0:
    #     return redirect(url_for('index'))
    # else:
    #     if request.method == 'POST':
    #         save_answer()
    #     next_question = get_question_after(
    #         session['last_question'], session['quiz']
    #         )
    #     if next_question is None or len(next_question)==0:
    #         return redirect(url_for('result'))
    #     else:
    #         return question_form(next_question)
        
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
app.add_url_rule('/', 'index', index, methods=['GET', 'POST'])
app.add_url_rule('/test', 'test', test, methods=['GET', 'POST'])
app.add_url_rule('/result', 'result', result, methods=['GET', 'POST'])

app.run()