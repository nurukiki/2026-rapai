var data = document.querySelector("#data")
var now = document.querySelector("#now")
var record = document.querySelector("#record")

now.addEventListener("click", function(){
    fetch('/api/now', {
        method : "POST"
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("HTTP error " + response.status);
        }
        return response.json();
    })
    .then(result => {
        data.replaceChildren();
        var row = data.insertRow(); // 새 행 하나 만들기
	row.insertCell().textContent = "now";
   	row.insertCell().textContent = result.created_at;
   	row.insertCell().textContent = result.temperature + "°C";
   	row.insertCell().textContent = result.humidity + "%";
    })
    .catch(error => alert(error));
});

record.addEventListener("click", function(){
    fetch('api/record', {
        method : "GET"
    })
    .then (response => {
        if (!response.ok) {
            throw new Error("HTTP error " + response.status);
        }
        return response.json();
    })
    .then (result => {
        data.innerHTML = "";

      for (var i = 0; i < result.length; i++){
	      var row = data.insertRow();

	      row.insertCell().textContent = result[i].id;
	      row.insertCell().textContent = result[i].created_at;
	      row.insertCell().textContent = result[i].temperature + "°C";
	      row.insertCell().textContent = result[i].humidity + "%";
        }
    })

})
