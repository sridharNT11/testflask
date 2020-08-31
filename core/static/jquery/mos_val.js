$( document ).ready(function() {
    alert('in jquery');
    errorClass: 'errors',
    $("#personalia").validate({
        
        rules: {
            prefix: "required",
            name: "required",
            email: {
                required : true,
                email: true
            },
            mobile : "required",
            dob : "required",
            age: "required",
            pob: "required",
            inlineRadioOptions: "required"
        },

        messages: {
            
            prefix : "Please specify the prefix",
            name : "Please enter the name",
            email : {
                required : "Please enter the email id",
                email : "Please enter valid email id"
            },
            mobile : "Please enter the mobile number",
            dob : "Please enter the Date of Birth",
            age : "Please mention the age",
            pob : "Please enter the Place of birth",
            inlineRadioOptions : "Please specify the gender"
            
        },

        highlight: function(element) {
            $(element).parent().addClass('error')
        },
    
        unhighlight: function(element) {
            $(element).parent().removeClass('error')
        },

        submitHandler: function(form) {
            form.submit();
        }
    });

    $("#communication").validate({
        
        
        rules: {
            rp_addr: "required",
            rp_city: "required",
            rp_pin : "required",
            c_addr : "required",
            c_city: "required",
            c_pin: "required"
        },

        messages: {
            
            rp_addr : "Please enter the address",
            rp_city: "Please enter the city",
            rp_pin : "Please enter the pin code",
            c_addr : "Please enter the clinical address",
            c_city : "Please mention the city",
            c_pin : "Please enter the pin code"
        },
    

        highlight: function(element) {
            $(element).parent().addClass('error')
        },
    
        unhighlight: function(element) {
            $(element).parent().removeClass('error')
        },

        submitHandler: function(form) {
            form.submit();
        }

    });

    $("#qualifications").validate({
        
        rules: {
            row1_deg: "required",
            row1_univ: "required",
            row1_year : "required"
        },

        messages: {
            row1_deg : "Please fill atleast one row for degree",
            row1_univ: "Please fill atleast one row for university",
            row1_year: "Please fill out atleast one row for year obtained"
        },
        // errorPlacement: function(){
        //     return false;
        // },

        highlight: function(element) {
            $(element).parent().addClass('error')
        },
    
        unhighlight: function(element) {
            $(element).parent().removeClass('error')
        },

        

        submitHandler: function(form) {
            form.submit();
        }

    });


    $("#prof_att").validate({
        
        
        rules: {
            row1_ins: "required",
            row1_desig: "required",
            row1_from : "required",
            row1_to:"required"
        },

        messages: {
            row1_ins : "Please fill atleast one row",
            row1_desig: "Please fill atleast one row",
            row1_from: "Please fill out atleast one row",
            row1_to:"Please fill out atleast onr row"


        },
        // errorPlacement: function(){
        //     return false;
        // },

        highlight: function(element) {
            $(element).parent().addClass('error')
        },
    
        unhighlight: function(element) {
            $(element).parent().removeClass('error')
        },

        submitHandler: function(form) {
            form.submit();
        }

    });
});