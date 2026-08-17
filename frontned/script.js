async function analyzeTraffic() {

    const vehicleCount = document.getElementById("vehicleCount").value;

    if (vehicleCount === "") {
        alert("Please enter the number of vehicles.");
        return;
    }

    const response = await fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            vehicle_count: Number(vehicleCount)
        })
    });

    const data = await response.json();

    document.getElementById("count").textContent = data.vehicle_count;
    document.getElementById("level").textContent = data.traffic_level;
    document.getElementById("greenTime").textContent = data.green_time;
    document.getElementById("signal").textContent = "GREEN";
}