async function predict() {
    const age = document.getElementById("age").value;
    const gender = document.getElementById("gender").value;

    if ( age < 0 ) {
        //document.getElementById("prediction").innerText = "Error: Age must above 0";
        window.alert("Error: Age must above 0")
        return
    }

    API_URL = "http://127.0.0.1:8000"

    const response = await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            age: age,
            gender: gender
        })
    });

    const data = await response.json();

    const prediction = data.prediction[0];  // Extract the first element from the prediction array

    document.getElementById("prediction").innerText = "Predicted Music Genre: " + prediction;
}
