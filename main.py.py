from scrapping import get_jobs
from flask import Flask, request, redirect
from flask import render_template, send_from_directory
#from salva import save_to_csv

app = Flask('Aguinaldo Konzo')


@app.route('/')
def hello_world():
    return redirect('/search')


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/result')
def result():
    keyword = request.args.get('keyword')
    keyword = keyword.lower()
    if keyword:
        search_result = get_jobs(keyword)
        #save_to_csv(search_result)
    else:
        return redirect('/')
    return render_template('result.html', jobs=search_result, keyword=keyword)





app.run(host='0.0.0.0')

'''@app.route('/<user>')
def welcome(user):
    print(user)
    return f'Bem-Vindo sr(a), {user}.'''


# https://www.jobartis.com/vagas-emprego

# jobs_all_vagas = scrapping_jobartis('https://www.jobartis.com/vagas-emprego')
# jobs_Ti = scrapping_jobartis('https://www.jobartis.com/vagas-emprego/luanda/informatica-e-ti')
# print(len(jobs_Ti))
# print(len(jobs_all_vagas))


# https://www.jobartis.com/vagas-emprego?utf8=%E2%9C%93&q%5Bcontent_matches_tsquery%5D=&q%5Brequired_general_specializations_id_eq%5D=29&q%5Bindustry_id_eq%5D=&q%5Bjob_type_id_eq%5D=&q%5Bprovince_id_in%5D=&q%5Bopen_true%5D=0
# print(scrapping_jobartis('https://jobartis.com/vagas-emprego/gestor'))
# result = search_keyword(['informatica'])
# save_to_csv(result)
'''search = 'gestor'
result_jobartis = search_keyword(search)
all_result = result_jobartis
save_to_csv(all_result)'''
