console.log("the script is here");

function viewModel() {
    var self = this;

    this.first_name = "";
    this.last_name= "";
    this.email = "";
    this.phone = "";

    this.pw = ko.observable();
    this.pw_confirm = ko.observable();
    this.passwordValid = ko.observable(false);
    this.disableSave = ko.observable(true);


    this.pw_validation = function () {

        if(self.pw() === self.pw_confirm()){
            self.passwordValid(false);
            self.disableSave(false);
        }
        else {
            self.passwordValid(true);
        }

    };

    this.pw.subscribe(this.pw_validation);
    this.pw_confirm.subscribe(this.pw_validation);


    function validateName(name) {
        return name;
    }

    function validateEmail(email) {
        return email;
    }

    function validatePhone(phone){
        return phone;
    }

    this.saveUser = function () {

        var formData = {
            first_name: self.first_name,
            last_name: self.last_name,
            email: self.email,
            phone: self.phone,
            pw: self.pw(),
            pw_conf: self.pw_confirm()
        };
        var data = ko.toJSON(formData);
        $.post('/new/user', data, function(returnData){
            console.log('callback worked')
            console.log(returnData)
        });


        console.log(formData)
    }

}

ko.applyBindings(new viewModel());