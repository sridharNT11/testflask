$( document ).ready(function() {
    alert("in check jquery");

    $('input[type="checkbox"]').click(function(){
        if($(this).prop("checked") == true){
            alert('inside check validation');
            var rp_addr = $("#rp_addr").val();
            alert(rp_addr); 
            $("#c_addr").val(rp_addr);

            var rp_city = $("#rp_city").val();
            alert(rp_city);
            $("#c_city").val(rp_city);

            var rp_pin = $("#rp_pin").val();
            alert(rp_pin);
            $("#c_pin").val(rp_pin);
            //return false;
        }

        else if($(this).prop("checked") == false){
            alert('inside uncheck');
            var c_addr = '';
            $("#c_addr").val(c_addr);

            var c_city = '';
            $("#c_city").val(c_city);

            var c_pin = '';
            $("#c_pin").val(c_pin);

        }
    });
});


 