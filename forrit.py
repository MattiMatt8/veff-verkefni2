from bottle import *
import os

@route('/')
def index():
    return '''
    <h2>Verkefni 2</h2>
    <a href="1">Liður 1</a>
    <a href="2">Liður 2</a>
    '''
@route('/1')
def lidur1():
    return '''
    <h2>Verkefni 2 <span style="font-size:18px;">Liður 1</span></h2>
    <a href="lidur1/1">Síða 1</a>
    <a href="lidur1/2">Síða 2</a>
    <a href="lidur1/3">Síða 3</a>
    <a href="/">Til baka</a>
    '''
@route('/lidur1/<tala>')
def sida(tala):
    return '''
    <h3>Þetta er síða ''',tala,'''
    </h3><a href="/1">Til baka</a>
    '''
@route('/myndir/<skjal>')
def myndir(skjal):
    return static_file(skjal, root='./img')
@route('/2')
def lidur2():
    return '''
    <h2>Verkefni 2 <span style="font-size:18px;">Liður 2</span></h2>
    <h3>Veldu bókstaf:</h3>
    <a href="lidur2?stafur=y"><img height="140px" src="myndir/y.png"></a>
    <a href="lidur2?stafur=v"><img height="140px" src="myndir/v.png"></a>
    <a href="lidur2?stafur=z"><img height="140px" src="myndir/z.png"></a>
    <a href="/">Til baka</a>
    '''
@route('/lidur2')
def sida2():
    x = request.query.stafur
    if x == "y" or x == "v" or x == "z":
        return '''
        <h3>Stafurinn þinn er:</h3>
        <img height="200px" src="myndir/''',x,'''.png">
        <a href="2">Til baka</a>
        '''
    else:
        return '''
        <h3>Síða ekki til</h3>
        <a href="2">Til baka</a>
        '''
@error(404)
def villa(error):
    return '''
    <h2>Error 404</h2>
    <h3>Síða finnst ekki</h3>
    <a href="/">Til Baka</a>
    '''

if os.environ.get('HEROKU'):
    run(host="0.0.0.0", port=os.environ.get('PORT'))
else:
    run()