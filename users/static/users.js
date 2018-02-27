console.log('users.js loaded');

var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data:{
        users:[],
        test: 'Jesse'
    },
    methods:{
        showDetails: function (event) {
            var id = Number(event.target.id);
            for (i=0; i < this.users.length; i++){
                if(this.users[i].id === id){
                    this.users[i].details_visible = !this.users[i].details_visible;
                }
            }
            //this.users[id].details_visible = !this.users[id].details_visible;
        }
    },
    created(){
        fetch('http://127.0.0.1:5000/users/api/index')
            .then(response => response.json())
            .then(json => {
                this.users = json
            })
    }
});