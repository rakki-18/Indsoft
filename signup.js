function encrypt(test_string){
    var encrypted_string = "";
    for(let i= 0; i < test_string.length;i++)
    {
        encrypted_string+=(test_string.charCodeAt(i) + 100).toString();
    }
    return encrypted_string;
}

/* when the user signs up with some credentials, call the API with the credentials and then redirect to the profile page if it is a successful sign up */
function signup(){
    var  encrypted_username = encrypt(frm.username.value);
    var encrypted_passwd = encrypt(frm.passwd.value);
    var confirm_passwd = encrypt(frm.confirm.value);
    console.log(encrypted_username);
    console.log(frm.username.value);
   

    var to_url = "https://fldz51d8j6.execute-api.ap-south-1.amazonaws.com/demo/signup" + "?username=" + encrypted_username + "&passwd=" + encrypted_passwd
    + "&otp=" + frm.otp.value+ "&branch=" + frm.branch.value+ "&Phone=" + frm.phone.value
    + "&email=" + frm.email.value+ "&confirm=" + confirm_passwd;
    
    $.ajax({
        url: to_url,
        type: 'get',
        success: function(data){
            

            
            var response_htm = '<div id = "response_css">' + data + '</div>';
            $('#response').html(response_htm);
            if(data == "data updated")
            location.href = "/profile_page/profile.htm?username="+encrypted_username; 
        },
        error: function (xhr, ajaxOptions, thrownError) {
            var errorMsg = 'Ajax request failed: ' + xhr;
            console.log(thrownError);
            $('#response').html(errorMsg);
        }
    });
}