const apiBaseUrl = "http://127.0.0.1:8000/api";

let dataLoaded = false;

// Fetch All Data
async function fetchAllData() {
    try {
        showLoading()
        const response = await fetch(`${apiBaseUrl}/data`);
        if (!response.ok) throw new Error("Failed to fetch data");

        const data = await response.json();
        if (data.message) {
            alert(data.message); // Caso a tabela esteja vazia
            return;
        }

        displayDataAsTable(data);

        // Esconder o botão de Load e mostrar os novos
        document.getElementById("load-btn").style.display = "none";
        document.getElementById("nav-buttons").innerHTML = `
            <button onclick="showProcessingMenu()">Data Processing</button>
            <button onclick="showVisualization()">Data Visualization</button>
        `;
    } catch (error) {
        console.error("Error fetching data:", error);
        alert("An error occurred while fetching data.");
    }
}

// Mostrar Dropdowns
function showProcessingMenu() {
    document.getElementById("processing-container").style.display = "block";
}

// Mostrar Dados em Tabela
function displayDataAsTable(data, page = 1, rowsPerPage = 10) {
    const container = document.getElementById("data-table");
    const totalRows = data.length;
    const start = (page - 1) * rowsPerPage;
    const end = start + rowsPerPage;
    const paginatedData = data.slice(start, end);

    let table = "<table border='1'><tr>";
    Object.keys(data[0]).forEach(key => table += `<th>${key}</th>`);
    table += "</tr>";

    paginatedData.forEach(row => {
        table += "<tr>";
        Object.values(row).forEach(value => table += `<td>${value}</td>`);
        table += "</tr>";
    });

    table += "</table>";

    container.innerHTML = table;

    // Adicionar controles de paginação
    const pagination = document.getElementById("pagination-controls");
    pagination.innerHTML = `
        <button ${page === 1 ? "disabled" : ""} onclick="displayDataAsTable(data, ${page - 1}, ${rowsPerPage})">Previous</button>
        <span>Page ${page} of ${Math.ceil(totalRows / rowsPerPage)}</span>
        <button ${end >= totalRows ? "disabled" : ""} onclick="displayDataAsTable(data, ${page + 1}, ${rowsPerPage})">Next</button>
    `;
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


function showLoading() {
    const container = document.getElementById("data-table");
    container.innerHTML = "<p>Loading...</p>";
}