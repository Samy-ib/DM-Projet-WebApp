Vue.component('inputcard', {
    props: ['title', 'body', 'value'],
    template: `
                <div class="card">
                    <div class="card-content">
                        <span class="card-title">{{title}}</span>
                        <p><slot></slot></p>     
                        <div class="card-action">
                        <slot name='error'></slot>
                            <div class="row">
                                <div class="col s6 offset-s3">
                                <input v-focus type="text" @keyup.enter="$emit('enter')" v-bind:value="value" @input="$emit('input', $event.target.value)">
                                </div>
                            </div>
                            <div class="row">
                                <mybuttons @gonext="$emit('gonext')" @goprev="$emit('goprev')"></mybuttons>
                            </div>
                        </div>
                    </div>
                </div>
            `
    })

Vue.component('welcomecard', {
    props: ['title', 'body'],
    template: `
                <div class="card rounded">
                    <div class="card-content">
                        <span class="card-title">{{title}}</span>
                        <p><slot></slot></p>     
                        <div class="card-action">
                            
                            <div class="row">
                                <a class="waves-effect waves-light btn" @click="$emit('gonext')">Alright !</a>                                
                            </div>
                        </div>
                    </div>
                </div>
            `
})

Vue.component('resultcard', {
    props: ['title'],
    template:   `
                <div class="card rounded">
                    <div class="card-content">
                        <span class="card-title">{{title}}</span>
                        <p><slot></slot></p>     
                        <div class="card-action">
                            
                            <div class="row">
                                <a class="waves-effect waves-light btn" @click="$emit('retry')">Retry<i class="material-icons right">autorenew</i></a>                                
                            </div>
                        </div>
                    </div>
                </div>
    
    
    `
})

Vue.component('mybuttons', {
    template:   `
                <div class="row">
                    <div class="col s4 offset-s2">
                        <a class="waves-effect waves-light btn" @click="$emit('goprev')">Back<i class="material-icons left">arrow_back</i></a>
                    </div>  
                    <div class="col s4">
                        <a class="waves-effect waves-light btn" @click="$emit('gonext')">Next
                        <i class="material-icons right">arrow_forward</i>
                                  </a>
                    </div>
                    
                </div>
                `
})

var app = new Vue({
    el : '#root',
    data : {
        oneElem : '',
        elems: ['','','','','','','','','','','','','','','','','','','',''],
        errMsg : '',
        show : [true, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false],
        pos : 0,
        resultCLASS : '',
        resultNSP : '',
    },
    methods : {
        nextElem() {
            this.errMsg = ''
            if ( isNaN(Number(this.oneElem)) ) {
                this.errMsg = 'Incorrect type !'
            }else if (this.oneElem == '') {
                this.errMsg = 'You have to put something !'
            }if (this.errMsg == '' || this.pos==0){
                this.errMsg = ''
                this.addElem()
                this.increment()
                this.show = [false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false]
                this.show[this.pos] = true
            }if (this.pos==21) {
                axios.get('http://127.0.0.1:5000/api/class', {
                    params: {
                        lb:this.elems[0], ac:this.elems[1], fm:this.elems[2], uc:this.elems[3], astv:this.elems[4], mstv:this.elems[5], altv:this.elems[6], mltv:this.elems[7],
                        dl:this.elems[8], ds:this.elems[9], dp:this.elems[10], width:this.elems[11], min:this.elems[12], max:this.elems[13], nmax:this.elems[14],
                        nzeros:this.elems[15], mode:this.elems[16], mean:this.elems[17], median:this.elems[18], variance:this.elems[19]
                    }
                    }).then(response => this.resultCLASS = response.data)
                console.log(this.resultCLASS)
                // this.resultCLASS.Prob = this.resultCLASS.Prob.toFixed(2)
                axios.get('http://127.0.0.1:5000/api/nsp', {
                    params: {
                        lb:this.elems[0], ac:this.elems[1], fm:this.elems[2], uc:this.elems[3], astv:this.elems[4], mstv:this.elems[5], altv:this.elems[6], mltv:this.elems[7],
                        dl:this.elems[8], ds:this.elems[9], dp:this.elems[10], width:this.elems[11], min:this.elems[12], max:this.elems[13], nmax:this.elems[14],
                        nzeros:this.elems[15], mode:this.elems[16], mean:this.elems[17], median:this.elems[18], variance:this.elems[19]
                    }
                    }).then(response => this.resultNSP = response.data)
                // this.resultNSP.Prob = this.resultNSP.Prob.toFixed(2)                
            }
            // isNaN(Number(app.oneElem))
        },
        prevElem() {
            this.errMsg = ''
            this.delElem()
            this.decrement()
            this.oneElem = this.elems[this.pos - 1]
            this.show = [false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false]
            this.show[this.pos] = true
        },
        increment() {
            this.pos += 1
            if (this.pos == this.show.length) {
                this.pos=this.show.length -1;
            }
        },
        decrement() {
            this.pos -= 1
            if (this.pos == -1) {
                this.pos = 0;
            }
        },
        addElem() {
            this.elems[this.pos - 1] = this.oneElem;
            this.oneElem = ''
        },
        delElem() {
            this.elems[this.pos - 1] = ''
            this.oneElem = ''
        },
        retry(){
            this.oneElem = '',
            this.elems = ['','','','','','','','','','','','','','','','','','','',''],
            this.errMsg = '',
            this.show = [true, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false],
            this.pos = 0,
            this.resultCLASS = '',
            this.resultNSP = ''
        }
    }
})
Vue.directive('focus', {
    // Quand l'élément lié est inséré dans le DOM...
    inserted: function (el) {
      // L'élément prend le focus
      Vue.nextTick(() => el.focus());
    }
  })


