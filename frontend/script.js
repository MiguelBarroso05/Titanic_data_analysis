const baseUrl = 'http://localhost:8000';
let currentPage = 1;
let currentSortColumn = null;
let currentSortOrder = 'asc';

/**
 * Fetches data from the API and updates the table.
 *
 * - Sends a GET request to fetch paginated and sorted data.
 * - Clears the existing table rows and adds new ones with the fetched data.
 * - Handles missing values for "Cabin" and "Embarked" by displaying "N/A".
 * - Logs errors to the console if the fetch fails.
 */

function fetchTableData() {
    const queryParams = new URLSearchParams({
        page: currentPage,
        per_page: 10,
        ...(currentSortColumn && { column: currentSortColumn, order: currentSortOrder })
    });

    fetch(`${baseUrl}/data?${queryParams}`)
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('tableBody');
            tableBody.innerHTML = '';
            data.forEach(row => {
                tableBody.innerHTML += `
                    <tr>
                        <td>${row.PassengerId}</td>
                        <td>${row.Name}</td>
                        <td>${row.Survived}</td>
                        <td>${row.Pclass}</td>
                        <td>${row.Sex}</td>
                        <td>${row.Age}</td>
                        <td>${row.SibSp}</td>
                        <td>${row.Parch}</td>
                        <td>${row.Ticket}</td>
                        <td>${row.Fare}</td>
                        <td>${row.Cabin || 'N/A'}</td>
                        <td>${row.Embarked || 'N/A'}</td>
                    </tr>
                `;
            });
        })
        .catch(error => console.error('Error fetching table data:', error));
}

/**
 * Sorts the table based on the specified column.
 *
 * - Toggles the sort order (ascending/descending) if the column is already sorted.
 * - Sets a new column to sort and resets the order to ascending.
 * - Resets to the first page before fetching the sorted data.
 * - Calls `fetchTableData` to update the table with the new sort order.
 *
 * @param {string} column - The column to sort by.
 */

function sortTable(column) {
    if (currentSortColumn === column) {
        currentSortOrder = currentSortOrder === 'asc' ? 'desc' : 'asc';
    } else {
        // Set new column and default order
        currentSortColumn = column;
        currentSortOrder = 'asc';
    }
    // Reset to first page and fetch sorted data
    currentPage = 1;
    fetchTableData();
}

/**
 * Moves to the next page and fetches data.
 *
 * - Increments the current page number.
 * - Calls `fetchTableData` to update the table with the next page of data.
 */

function nextPage() {
    currentPage++;
    fetchTableData();
}

/**
 * Moves to the previous page and fetches data.
 *
 * - Decrements the current page number, but only if it is greater than 1.
 * - Calls `fetchTableData` to update the table with the previous page of data.
 */

function prevPage() {
    if (currentPage > 1) {
        currentPage--;
        fetchTableData();
    }
}

/**
 * Searches for data based on the input query and updates the table.
 *
 * - Converts the input value to lowercase and sends it as a query to the API.
 * - Clears the current table rows and populates the table with the search results.
 * - Handles missing values for "Cabin" and "Embarked" by displaying "N/A".
 * - Logs errors to the console if the search fails.
 */

document.getElementById('searchBar').addEventListener('input', function () {
    const query = this.value.toLowerCase();
    fetch(`${baseUrl}/data/search?query=${query}`)
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('tableBody');
            tableBody.innerHTML = '';
            data.forEach(row => {
                tableBody.innerHTML += `
                    <tr>
                        <td>${row.PassengerId}</td>
                        <td>${row.Name}</td>
                        <td>${row.Survived}</td>
                        <td>${row.Pclass}</td>
                        <td>${row.Sex}</td>
                        <td>${row.Age}</td>
                        <td>${row.SibSp}</td>
                        <td>${row.Parch}</td>
                        <td>${row.Ticket}</td>
                        <td>${row.Fare}</td>
                        <td>${row.Cabin || 'N/A'}</td>
                        <td>${row.Embarked || 'N/A'}</td>
                    </tr>
                `;
            });
        })
        .catch(error => console.error('Error searching data:', error));
});

// Initial data fetch
fetchTableData();


const chartCanvas = document.getElementById('chartCanvas').getContext('2d');
let currentChart;

/**
 * Updates the chart with new data and options.
 *
 * - Destroys the current chart if it exists to ensure a clean update.
 * - Creates a new horizontal bar chart using the provided data and options.
 * - Configures the chart to start the x-axis at zero and adjusts the y-axis font size.
 * - Sets the legend's position to the top of the chart.
 * - Updates the chart description text displayed in the DOM.
 *
 * @param {Object} chartData - The data to display in the chart.
 * @param {Object} options - Additional configuration options for the chart.
 * @param {string} description - A description of the chart to display.
 */

function updateChart(chartData, options, description) {
    if (currentChart) {
        currentChart.destroy();
    }
    currentChart = new Chart(chartCanvas, {
        type: 'bar', // Keeps the chart type as 'bar'
        data: chartData,
        options: {
            ...options,
            indexAxis: 'y', // Changes the chart to horizontal bars
            plugins: {
                legend: {
                    position: 'top' // Adjusts the position of the legend
                }
            },
            scales: {
                x: {
                    beginAtZero: true
                },
                y: {
                    ticks: {
                        font: {
                            size: 12 // Adjusts font size if needed
                        }
                    }
                }
            }
        }
    });
    document.getElementById('chartDescription').innerText = description;
}

/**
 * Generates a survival chart showing the percentage of passengers who survived and died.
 *
 * - Fetches data from the API to calculate survival and death counts.
 * - Calculates the percentages of survivors and fatalities.
 * - Updates the chart with the calculated data, using green for survivors and red for fatalities.
 * - Displays a descriptive text below the chart summarizing the survival statistics.
 *
 * Calls the `updateChart` function to render the chart.
 */
function generateSurvivalChart() {
    fetch(`${baseUrl}/data`)
        .then(response => response.json())
        .then(data => {
            const survived = data.filter(row => row.Survived === 1).length;
            const died = data.filter(row => row.Survived === 0).length;
            const total = survived + died;
            const survivedPercent = ((survived / total) * 100).toFixed(2);
            const diedPercent = ((died / total) * 100).toFixed(2);

            updateChart(
                {
                    labels: ['Survived', 'Died'],
                    datasets: [{
                        label: 'Passenger Count',
                        data: [survived, died],
                        backgroundColor: ['green', 'red']
                    }]
                },
                {
                    responsive: true,
                    indexAxis: 'y',
                    scales: {
                        x: {
                            beginAtZero: true
                        }
                    }
                },
                `This chart shows that ${diedPercent}% of passengers died, while ${survivedPercent}% survived. A larger proportion of passengers did not survive the Titanic tragedy.`
            );
        });
}

/**
 * Generates a gender-based survival chart comparing male and female survival rates.
 *
 * - Fetches data from the API to calculate survival and death counts for males and females.
 * - Calculates the survival rates for both genders.
 * - Updates the chart with the calculated data, using green for survivors and red for fatalities.
 * - Displays a descriptive text below the chart summarizing the gender-based survival statistics.
 *
 * Calls the `updateChart` function to render the chart.
 */

function generateGenderSurvivalChart() {
    fetch(`${baseUrl}/data`)
        .then(response => response.json())
        .then(data => {
            const maleSurvived = data.filter(row => row.Sex === 'male' && row.Survived === 1).length;
            const femaleSurvived = data.filter(row => row.Sex === 'female' && row.Survived === 1).length;

            const maleDied = data.filter(row => row.Sex === 'male' && row.Survived === 0).length;
            const femaleDied = data.filter(row => row.Sex === 'female' && row.Survived === 0).length;

            const totalMale = maleSurvived + maleDied;
            const totalFemale = femaleSurvived + femaleDied;

            const maleSurvivalRate = ((maleSurvived / totalMale) * 100).toFixed(2);
            const femaleSurvivalRate = ((femaleSurvived / totalFemale) * 100).toFixed(2);

            updateChart(
                {
                    labels: ['Male', 'Female'],
                    datasets: [
                        { label: 'Survived', data: [maleSurvived, femaleSurvived], backgroundColor: 'green' },
                        { label: 'Died', data: [maleDied, femaleDied], backgroundColor: 'red' }
                    ]
                },
                {
                    responsive: true,
                    indexAxis: 'y',
                    scales: {
                        x: {
                            beginAtZero: true
                        }
                    }
                },
                `This chart shows that ${femaleSurvivalRate}% of females survived, compared to ${maleSurvivalRate}% of males. Women had a significantly higher survival rate than men.`
            );
        });
}

/**
 * Generates a class distribution chart showing the number of passengers in each class.
 *
 * - Fetches data from the API to calculate the number of passengers in each class (1st, 2nd, 3rd).
 * - Updates the chart with the class counts, using different colors for each class.
 * - Displays a descriptive text below the chart summarizing the class distribution.
 *
 * Calls the `updateChart` function to render the chart.
 */

function generateClassDistributionChart() {
    fetch(`${baseUrl}/data`)
        .then(response => response.json())
        .then(data => {
            const classCounts = [1, 2, 3].map(cls => data.filter(row => row.Pclass === cls).length);

            updateChart(
                {
                    labels: ['1st Class', '2nd Class', '3rd Class'],
                    datasets: [{
                        label: 'Passenger Count',
                        data: classCounts,
                        backgroundColor: ['blue', 'orange', 'purple']
                    }]
                },
                {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                },
                `This chart shows the distribution of passengers by class. The 3rd class had the highest number of passengers, followed by the 1st and 2nd classes.`
            );
        });
}

/**
 * Generates a class-based survival chart comparing survival rates across classes.
 *
 * - Fetches data from the API to calculate the number of survivors and fatalities in each class.
 * - Updates the chart with the survival and death data, using green for survivors and red for fatalities.
 * - Displays a descriptive text below the chart summarizing the survival rates by class.
 *
 * Calls the `updateChart` function to render the chart.
 */
function generateClassSurvivalChart() {
    fetch(`${baseUrl}/data`)
        .then(response => response.json())
        .then(data => {
            const survived = [1, 2, 3].map(cls => data.filter(row => row.Pclass === cls && row.Survived === 1).length);
            const died = [1, 2, 3].map(cls => data.filter(row => row.Pclass === cls && row.Survived === 0).length);

            updateChart(
                {
                    labels: ['1st Class', '2nd Class', '3rd Class'],
                    datasets: [
                        { label: 'Survived', data: survived, backgroundColor: 'green' },
                        { label: 'Died', data: died, backgroundColor: 'red' }
                    ]
                },
                {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                },
                `This chart shows survival by class. Passengers in 1st class had the highest survival rate, while those in 3rd class had the lowest.`
            );
        });
}

/**
 * Generates a survival chart based on embarkation port.
 *
 * - Fetches data from the API to calculate the number of survivors and fatalities for each embarkation port (Cherbourg, Queenstown, Southampton).
 * - Updates the chart with the survival and death data, using green for survivors and red for fatalities.
 * - Displays a descriptive text below the chart summarizing the survival rates by embarkation port.
 *
 * Calls the `updateChart` function to render the chart.
 */
function generateEmbarkedSurvivalChart() {
    fetch(`${baseUrl}/data`)
        .then(response => response.json())
        .then(data => {
            const ports = ['C', 'Q', 'S'];
            const survived = ports.map(port => data.filter(row => row.Embarked === port && row.Survived === 1).length);
            const died = ports.map(port => data.filter(row => row.Embarked === port && row.Survived === 0).length);

            updateChart(
                {
                    labels: ['Cherbourg (C)', 'Queenstown (Q)', 'Southampton (S)'],
                    datasets: [
                        { label: 'Survived', data: survived, backgroundColor: 'green' },
                        { label: 'Died', data: died, backgroundColor: 'red' }
                    ]
                },
                {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                },
                `This chart shows survival by embarkation port. Passengers from Cherbourg (C) had the highest survival rate, followed by those from Southampton (S) and Queenstown (Q).`
            );
        });
}

/**
 * Generates a chart comparing the average age of survivors and non-survivors.
 *
 * - Fetches data from the API and calculates the average age for survivors and fatalities.
 * - Updates the chart with the calculated average ages, using green for survivors and red for fatalities.
 * - Displays a descriptive text below the chart summarizing the average ages of survivors and non-survivors.
 *
 * Calls the `updateChart` function to render the chart.
 */
function generateAverageAgeChart() {
    fetch(`${baseUrl}/data`)
        .then(response => response.json())
        .then(data => {
            const survivedAvgAge = (
                data.filter(row => row.Survived === 1).reduce((sum, row) => sum + (row.Age || 0), 0) /
                data.filter(row => row.Survived === 1).length
            ).toFixed(1);
            const diedAvgAge = (
                data.filter(row => row.Survived === 0).reduce((sum, row) => sum + (row.Age || 0), 0) /
                data.filter(row => row.Survived === 0).length
            ).toFixed(1);

            updateChart(
                {
                    labels: ['Survived', 'Died'],
                    datasets: [{
                        label: 'Average Age',
                        data: [survivedAvgAge, diedAvgAge],
                        backgroundColor: ['green', 'red']
                    }]
                },
                {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                },
                `This chart shows the average age of survivors and non-survivors. Survivors had an average age of ${survivedAvgAge} years, compared to ${diedAvgAge} years for those who did not survive.`
            );
        });
}
