from app.api import api
from flask import jsonify, request
from app.api import utils

@api.route('/nsp', methods=['GET'])
def NSP():
    #127.0.0.1:5000/api/nsp?lb=137&ac=1&fm=0&uc=0&astv=20&mstv=2&altv=0&mltv=0&dl=5&ds=0&dp=0&width=74&min=86&max=160&nmax=1&nzeros=0&mode=126&mean=128&median=130&variance=23
    lb = request.args.get('lb')
    ac = request.args.get('ac')
    fm = request.args.get('fm')
    uc = request.args.get('uc')
    astv = request.args.get('astv')
    mstv = request.args.get('mstv')
    altv = request.args.get('altv')
    mltv = request.args.get('mltv')
    dl = request.args.get('dl')
    ds = request.args.get('ds')
    dp = request.args.get('dp')
    width = request.args.get('width')
    mini = request.args.get('min')
    maxi = request.args.get('max')
    nmax = request.args.get('nmax')
    nzeros = request.args.get('nzeros')
    mode = request.args.get('mode')
    mean = request.args.get('mean')
    median = request.args.get('median')
    variance = request.args.get('variance')

    elems = [lb,ac,fm,uc,astv,mstv,altv,mltv,dl,ds,dp,width,mini,maxi,nmax,nzeros,mode,mean,median,variance]
    elems = [int(i) for i in elems]
    #make prediction and return NSP
    print(elems)
    ind,probs = utils.predict(elems)
    if ind==0:
        nsp='Normal'
    elif ind==1:
        nsp='Suspect'
    else:
        nsp='Pathologic'
    dic = {'NSP':nsp,'Probs':{'N':probs[0],'S':probs[1],'P':probs[2]}}
    # print(elems)
    # print(ac)
    return jsonify(dic)

@api.route('/class', methods=['POST'])
def CLASS():
    lb = request.args.get['lb']
    ac = request.args.get['ac']
    fm = request.args.get['fm']
    uc = request.args.get['uc']
    astv = request.args.get['astv']
    mstv = request.args.get['mstv']
    altv = request.args.get['altv']
    mltv = request.args.get['mltv']
    dl = request.args.get['dl']
    ds = request.args.get['ds']
    dp = request.args.get['dp']
    width = request.args.get['width']
    mini = request.args.get['min']
    maxi = request.args.get['max']
    nmax = request.args.get['nmax']
    nzeros = request.args.get['nzeros']
    mode = request.args.get['mode']
    mean = request.args.get['mean']
    median = request.args.get['median']
    variance = request.args.get['variance']

    return 'nothing yet'
