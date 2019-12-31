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
                                <input v-focus ref='lolinput' type="text" name="" id="input1" @keyup.enter="$emit('enter')" v-bind:value="value" @input="$emit('input', $event.target.value)">
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
                                <a class="waves-effect waves-light btn" @click="$emit('gonext')">Okay</a>                                
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
        show : [true, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false],
        pos : 0,
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
                this.show = [false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false]
                this.show[this.pos] = true
            }
            // isNaN(Number(app.oneElem))
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
