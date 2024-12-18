const apiBaseUrl = "http://127.0.0.1:8000/api";


async function fetchAllData() {
    try {
        const response = await fetch(`${apiBaseUrl}/data`);
        if (!response.ok) throw new Error("Failed to fetch data");

        const data = await response.json();
        displayDataAsTable(data);
    } catch (error) {
        console.error("Error:", error);
        alert("An error occurred while fetching data.");
    }
}


function displayDataAsTable(data) {
    const container = document.getElementById("data-table");

    if (data.length === 0) {
        container.innerHTML = "<p>No data available.</p>";
        return;
    }

    let table = "<table border='1' cellspacing='0' cellpadding='5'>";
    table += "<tr>";
    Object.keys(data[0]).forEach(key => {
        table += `<th>${key}</th>`;
    });
    table += "</tr>";

    data.forEach(row => {
        table += "<tr>";
        Object.values(row).forEach(value => {
            table += `<td>${value}</td>`;
        });
        table += "</tr>";
    });

    table += "</table>";
    container.innerHTML = table;
}


let dataLoaded = false;

// Fetch All Data
async function fetchAllData() {
    try {
        const response = await fetch("http://127.0.0.1:8000/api/data");
        if (!response.ok) throw new Error("Failed to fetch data");

        const data = await response.json();
        displayDataAsTable(data);

        // Esconder o botão de load e mostrar os restantes
        document.getElementById("load-btn").style.display = "none";
        document.getElementById("nav-buttons").innerHTML += `
            <button onclick="showProcessingMenu()">Data Processing</button>
            <button onclick="showVisualization()">Data Visualization</button>
        `;
        dataLoaded = true;
    } catch (error) {
        console.error("Error:", error);
        alert("Failed to load data.");
    }
}

// Mostrar Dropdowns
function showProcessingMenu() {
    document.getElementById("processing-container").style.display = "block";
}

// Mostrar Dados em Tabela
function displayDataAsTable(data) {
    const container = document.getElementById("data-table");
    container.innerHTML = ""; // Resetar

    let table = "<table border='1'><tr>";
    Object.keys(data[0]).forEach(key => table += `<th>${key}</th>`);
    table += "</tr>";

    data.forEach(row => {
        table += "<tr>";
        Object.values(row).forEach(value => table += `<td>${value}</td>`);
        table += "</tr>";
    });

    table += "</table>";
    container.innerHTML = table;
}

// Processamento de Dados
async function processData() {
    const type = document.getElementById("processing-type").value;
    const column = document.getElementById("column-type").value;

    if (!type || !column) {
        alert("Please select both options.");
        return;
    }

    const response = await fetch(`http://127.0.0.1:8000/api/process?type=${type}&column=${column}`);
    const result = await response.json();
    document.getElementById("processing-result").innerText = `Result: ${result.value}`;
}

// Placeholder de Visualização
function showVisualization() {
    alert("Data visualization coming soon!");
}
