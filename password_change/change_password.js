function api_get_call()
{
    $( document ).ready(function(){
    
    var details = document.getElementById("frm");
    alert("fucker");
    to_url = 'https://em7ialrwbi.execute-api.ap-south-1.amazonaws.com/demo' + '?old=' + details.old.value + '&new=' + details.new.value + '&con=' + details.confirm.value;
    $.ajax({
        url: to_url;
        type: 'get',
        success: function(data){
            $('#response').html(data);
        },
        error: function (xhr, ajaxOptions, thrownError) {
            var errorMsg = 'Ajax request failed: ' + xhr;
            console.log(thrownError);
            $('#response').html(errorMsg);
          }
    });
});
}