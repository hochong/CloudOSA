//homepage function


let loop = true;

//press start button, start looping
async function press_start() {
    loop = true;
    console.log("press start");
    await loop_OSA_data();
}

//press stop button, stop looping
async function press_stop() {
    loop = false;
    console.log("press stop");
}

//press trace button, render once
async function press_trace() {
    loop = false;
    console.log("press trace");
    await refresh_chart();
}

//set loop and do stuff while loop = true
async function loop_OSA_data() {
    setTimeout(function () {
        setInterval(function () {
            //if loop=true, loop every 1 second
            if (loop) {
                refresh_chart();
            }
        }, 1000);
    });
}

// get data and render chart
async function refresh_chart() {
    $.ajax({
      url: '/onetrace/',
      success: function(data) {
      $('#refresh_div').html(data);
      }
    });
}
