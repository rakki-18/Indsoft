function login(){

    var to_url = "https://4w2yztgs06.execute-api.ap-south-1.amazonaws.com/demo/login" + "?username=" + frm.username.value + "&passwd=" + frm.passwd.value;
    
    $.ajax({
        url: to_url,
        type: 'get',
        success: function(data){
            
            if(data)
             response = "logged in";
            else
             response = "wrong password or username";
            
            var response_htm = '<div id = "response_css">' + response + '</div>';
            $('#response').html(response_htm);
        },
        error: function (xhr, ajaxOptions, thrownError) {
            var errorMsg = 'Ajax request failed: ' + xhr;
            console.log(thrownError);
            $('#response').html(errorMsg);
        }
    });
}