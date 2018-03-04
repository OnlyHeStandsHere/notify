console.log('users.js loaded');

var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data:{
        users:[],
        first_name: '',
        last_name:'',
        email:'',
        phone:'',
        password:'',
        showNewUserForm: false
    },
    methods: {
        showDetails: function (event) {
            var id = Number(event.target.id);
            for (i = 0; i < this.users.length; i++) {
                if (this.users[i].id === id) {
                    this.users[i].details_visible = !this.users[i].details_visible;
                }
            }
            //this.users[id].details_visible = !this.users[id].details_visible;
        },
        showNewUser: function () {
            this.showNewUserForm = !this.showNewUserForm;
        },
       cancelNewUser: function(){
            this.showNewUserForm = ! this.showNewUserForm;
            this.first_name = '';
            this.last_name = '';
            this.phone = '';
            this.email = '';
        },

        submitNewUser: function () {
            data = {
                first_name: this.first_name,
                last_name: this.last_name,
                email: this.email,
                phone: this.phone,
                password: this.password
            };

            fetch('/users/api/new', {
                                    method: 'POST', // or 'PUT'
                                    body: JSON.stringify(data),
                                    headers: new Headers({'Content-Type': 'application/json'})
                                    })
                .then(response => response.json())
                .then(json =>console.log(json))
        },
    },
    created(){
        fetch('/users/api/index')
            .then(response => response.json())
            .then(json => {
                this.users = json
            })
    }
});