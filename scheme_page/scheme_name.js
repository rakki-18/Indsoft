var chit_key , amount , brnch_key;
$( document ).ready(function(){
   
    $.ajax({
        url : 'https://617b6vvwjd.execute-api.ap-south-1.amazonaws.com/demo/',
        type: 'get',
        success: function(data){
            chit_key = data['chit_key'];
            amount = data['amount'];
            brnch_key = data['brnch_key'];
            $('#scheme_name').html(data['scheme_name']);
            $('#Date_of_joining').html(data['date_of_joining']);
            var codeblock =  '<div id = "payment">' + 
            '<span class="left">' + data['due_months'] + '</span' +
             '<span class="right">' + data['amount'] + '</span>' + '<br>'
             + '</div>';

             document.getElementById("due_month").innerHTML += data['due_months'];
             document.getElementById("amount").innerHTML += data['amount']; 



        },
        error: function (xhr, ajaxOptions, thrownError) {
            var errorMsg = 'Ajax request failed: ' + xhr;
            console.log(thrownError);
            $('#content').html(errorMsg);
          }

     });
});
function pay(){
    $.ajax({
        url: 'https://617b6vvwjd.execute-api.ap-south-1.amazonaws.com/demo/pay?chit_key=' + chit_key + '&amount=' + amount + '&brnch_key=' + brnch_key,
        type: 'get',
        success: function(data){
    
                alert("paid");
        },
        error: function (xhr, ajaxOptions, thrownError) {
            var errorMsg = 'Ajax request failed: ' + xhr;
            console.log(thrownError);
            $('#content').html(errorMsg);
          }

     });
}