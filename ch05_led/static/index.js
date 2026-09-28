
var led = document.querySelector("#led");
var on = document.querySelector("#on");
var off = document.querySelector("#off");

on.addEventListener("click", function(){
    fetch('/on', {
        method : "GET"
    })
    .then(response => {
        if (!response.ok){
            throw new Error("HTTO error" +response.status)
        }
        return response.text();
    })
    .then(result => {
        led.src = "https://e7.pngegg.com/pngimages/922/441/png-clipart-of-yellow-light-bulb-incandescent-light-bulb-lighting-creative-bulb-flag-fashion-thumbnail.png";

    })
    .catch(error => alert(error));
})

off.addEventListener("click", function(){
    fetch('/off', {
        method : "GET"
    })
    .then(response => {
        if (!response.ok){
            throw new Error("HTTP error" +response.status)
        }
        return response.text();
    })
    .then(result => {
        led.src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7f3i84nfY5Tx_Ib1CY8XCETNc3sbZscBmX8lDKkGCSG6RXK8bHtn-rd8&s=10";

    })
    .catch(error => alert(error));
})
