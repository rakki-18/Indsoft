
function update_password(){
    var to_url = "https://35i970cxs5.execute-api.ap-south-1.amazonaws.com/demo/password" + "?old=" + frm.old.value + "&new=" + frm.new.value + "&con=" + frm.confirm.value;
    
    $.ajax({
        url: to_url,
        type: 'get',
        success: function(data){
            var response;
            
            if(data == 1)
             response = "wrong password";
            else if(data == 2)
             response = "passwords don't match";
            else
             response = "updated successfully";
             
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