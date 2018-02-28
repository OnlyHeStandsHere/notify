console.log('script loaded for clients');

var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data:{
        clients: [],
    },

    created(){
        fetch('http://127.0.0.1:5000/clients/api/index')
            .then(response => response.json())
            .then(json => {
                this.clients = json
            })
    }
});