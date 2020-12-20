function encrypt(test_string){
    var encrypted_string = "";
    for(let i= 0; i < test_string.length;i++)
    {
        encrypted_string+=(test_string.charCodeAt(i) + 100).toString();
    }
    
    return encrypted_string;
}


function login(){
    encrypted_password = encrypt(frm.passwd.value);
    encrypted_username = encrypt(frm.username.value);
    
    var to_url = "https://4w2yztgs06.execute-api.ap-south-1.amazonaws.com/demo/login" + "?username=" + encrypted_password + "&passwd=" + encrypted_username;
    
    $.ajax({
        url: to_url,
        type: 'get',
        success: function(data){
            
            
            
            var response_htm = '<div id = "response_css">' + data + '</div>';
            $('#response').html(response_htm);
            if(data == "logged in")
            {
                location.href = "/profile_page/profile.htm?username="+encrypted_username; 
            }
        },
        error: function (xhr, ajaxOptions, thrownError) {
            var errorMsg = 'Ajax request failed: ' + xhr;
            console.log(thrownError);
            $('#response').html(errorMsg);
        }
    });
}