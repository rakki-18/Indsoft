
function update_password(){
    var to_url = "https://35i970cxs5.execute-api.ap-south-1.amazonaws.com/demo/password" + "?old=" + frm.old.value + "&new=" + frm.new.value + "&con=" + frm.confirm.value;
    
    $.ajax({
        url: to_url,
        type: 'get',
        success: function(data){
            var response;
            
            
             
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