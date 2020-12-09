function signup(){

    var to_url = "https://fldz51d8j6.execute-api.ap-south-1.amazonaws.com/demo/signup" + "?username=" + frm.username.value + "&passwd=" + frm.passwd.value
    + "&otp=" + frm.otp.value+ "&branch=" + frm.branch.value+ "&Phone=" + frm.phone.value
    + "&email=" + frm.email.value+ "&confirm=" + frm.confirm.value;
    
    $.ajax({
        url: to_url,
        type: 'get',
        success: function(data){
            

            
            var response_htm = '<div id = "response_css">' + data + '</div>';
            $('#response').html(response_htm);
        },
        error: function (xhr, ajaxOptions, thrownError) {
            var errorMsg = 'Ajax request failed: ' + xhr;
            console.log(thrownError);
            $('#response').html(errorMsg);
        }
    });
}