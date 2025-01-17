function encrypt(test_string){
    var encrypted_string = "";
    for(let i= 0; i < test_string.length;i++)
    {
        encrypted_string+=(test_string.charCodeAt(i) + 100).toString();
    }
    return encrypted_string;
}

/* sending a get request to the API with the parameters that the user entered while submitting the form and then outputting the data returned by the 
   lambda function in the html page */
function update_password(){

    const urlParams = new URLSearchParams(window.location.search);
    const username = urlParams.get('username');

    var   encrypted_old = encrypt(frm.old.value);
    var  encrypted_new = encrypt(frm.new.value);
    var  encrypted_con = encrypt(frm.confirm.value);
    

    var to_url = "https://35i970cxs5.execute-api.ap-south-1.amazonaws.com/demo/password" + "?old=" + encrypted_old + "&new=" + encrypted_new + "&con=" + encrypted_con
    +'&username='+username;
    
    $.ajax({
        url: to_url,
        type: 'get',
        success: function(data){
            var response;
            
            
             
            var response_htm = '<div id = "response_css">' + data + '</div>';
            $('#response').html(response_htm);
            if(data == "password updated")
            location.href = "/profile_page/profile.htm?username="+username; 
            
        },
        error: function (xhr, ajaxOptions, thrownError) {
            var errorMsg = 'Ajax request failed: ' + xhr;
            console.log(thrownError);
            $('#response').html(errorMsg);
        }
    });
    
}