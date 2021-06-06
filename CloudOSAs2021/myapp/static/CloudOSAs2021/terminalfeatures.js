//terminal function


//press submit button
//send post request to server
//with data as json
//retrieve data
async function submit_query() {
    console.log("press submit");
    let val = document.getElementById('command_input').value;
    console.log(val);
    $.ajax({
        url: '/api/',
        type: 'POST',
        data:JSON.stringify({command: val}),
        success: function(data) {
            console.log(data);
            document.getElementById('query_result_div').innerHTML = data.response ;
        }
    });
}
