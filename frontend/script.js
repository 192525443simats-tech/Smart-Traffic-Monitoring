async function analyzeTraffic() {

    const vehicleCount = document.getElementById("vehicleCount").value;

    if (vehicleCount === "") {
        alert("Please enter the number of vehicles.");
        return;
    }

    try {
        const response = await fetch("http://localhost:3000/traffic", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                vehicle_count: Number(vehicleCount)
            })
        });

        const data = await response.json();

        if (!response.ok) {
            alert(data.error || "Something went wrong.");
            return;
        }

        document.getElementById("count").textContent = data.vehicle_count;
        document.getElementById("level").textContent = data.traffic_level;
        document.getElementById("greenTime").textContent = data.green_time;
        document.getElementById("signal").textContent = "GREEN";

    } catch (error) {
        console.error("Error:", error);
        alert("Unable to connect to backend.");
    }
}