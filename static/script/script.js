$(document).ready(function() {
    $('#fform').submit(function(e) {
        e.preventDefault();
        var jm = $('#jm').val();        
        
        $.ajax({
            url: "/api/nickname/" + jm,
            success: function(result){
                if (result == "NOT OK") {
                    $("#jm").css("background-color", "#ff9999");
                    alert("Toto jméno je zabráno!");
                }

                else {
                    $("#jm").css("background-color", "white");
                    e.currentTarget.submit();
                }

            }
            
        });

    });

    $("#jm").change(function(){
        jm = $("#jm").val();
        $.ajax({
            url: "/api/nickname/" + jm,
            success: function(result){
                if (result == "NOT OK") {
                    $("#jm").css("background-color", "#ff9999");
                    alert("Toto jméno je zabráno!");
                }

                else {
                    $("#jm").css("background-color", "white");
                }

            }
            
        });
    });
});