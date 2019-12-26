from app.api import api
from flask import jsonify, request
from app.api import utils

network_nsp = utils.loadNet_NSP('app/api/nsp_model.pt')
network_class = utils.loadNet_CLASS('app/api/class_model.pt')

@api.route('/nsp', methods=['GET'])
def NSP():
    """
        Given a GET request containing our attributes we return our
        predicted class and the probability of all of them in a JSON format.
    """

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
    ind,probs = utils.predict_NSP(network_nsp,elems)
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

@api.route('/class', methods=['GET'])
def CLASS():
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

    ind,probs = utils.predict_CLASS(network_class,elems)

    if ind==0:
        classe='A: calm sleep'
    elif ind==1:
        classe='B: REM sleep'
    elif ind==2:
        classe='C: Calm vigilance'
    elif ind==3:
        classe='D: Active vigilance'
    elif ind==4:
        classe='E/SH: Shift pattern'
    elif ind==5:
        classe='AD: accelerative/decelerative pattern (stress situation)'
    elif ind==6:
        classe='DE: decelerative pattern (vagal stimulation)'
    elif ind==7:
        classe='LD: largely decelerative pattern'
    elif ind==8:
        classe='FS: flat-sinusoidal pattern (pathological state)'
    elif ind==9:
        classe='SUSP: suspect pattern'

    dic = {'CLASS':classe,'Probs':{'A':probs[0],'B':probs[1],'C':probs[2],'D':probs[3],'E/SH':probs[4],'AD':probs[5],'DE':probs[6],'LD':probs[7],'FS':probs[8],'SUSP':probs[9]}}


    return jsonify(dic)
