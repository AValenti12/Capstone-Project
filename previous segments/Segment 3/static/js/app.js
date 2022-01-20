// from data.js
const tableData = data;

// get table references
var tbody = d3.select("tbody");

function buildTable(data) {
  // First, clear out any existing data
  tbody.html("");

  // Next, loop through each object in the data
  // and append a row and cells for each value in the row
  data.forEach((dataRow) => {
    // Append a row to the table body
    let row = tbody.append("tr");

    // Loop through each field in the dataRow and add
    // each value as a table cell (td)
    Object.values(dataRow).forEach((val) => {
      let cell = row.append("td");
      cell.text(val);
    });
  });
}

// 1. Create a variable to keep track of all the filters as an object.
const filterTrac = {};

// 3. Use this function to update the filters. 
function updateFilters() {
    // const filterTrac = {};

    // 4a. Save the element that was changed as a variable.
    var chgElem = d3.select(this);
    // console.log(chgElem);
    // 4b. Save the value that was changed as a variable.
    var chgVal = chgElem.property("value");
    console.log(chgVal);
        // 4c. Save the id of the filter that was changed as a variable.
    // let chgId - chgElem('input.id').text();
    var chgId = chgElem.attr('id');
    console.log(chgId);
    // 5. If a filter value was entered then add that filterId and value
    // to the filters list. Otherwise, clear that filter from the filters object.
    if (chgVal) {
      // filteredData = filteredData.filter(row => row.chgId === chgVal);
      // filterTrac[0] = {'id': chgId, 'value': chgVal}
      filterTrac[chgId] = chgVal; 
      // console.log("True")
      // console.log(filterTrac);
    } else {
      // filetrTrac = [];
      delete filterTrac[chgId];
      // console.log(filterTrac);
      // console.log("false");//
    };
     
    // 6. Call function to apply all filters and rebuild the table
    filterTable();
  
  }
  
  // 7. Use this function to filter the table when data is entered.
  function filterTable() {
  
    // 8. Set the filtered data to the tableData.
    filteredData = tableData;
  
    // 9. Loop through all of the filters and keep any data that
    // matches the filter values
    for ([key, val] of Object.entries(filterTrac)){
    // Object.entries(filterTrac).forEach((key, val) => {
      // console.log(filterTrac)
      console.log(`key: ${key}, value: ${val}`);
    // console.log(`key: ${key[0]}, value: ${key[1]}`);
      // filteredData = filteredData.filter(row => row[i] === i.value);
    // filteredData = filteredData.filter(row => row.key[0] === key[1]);
    console.log(filteredData)
    // filteredData.filter(row => console.log(val))
    filteredData = filteredData.filter(row => row[key].toString() === val);
    console.log(typeof key)
    console.log(typeof val)
    
      // console.log(Object.keys(i));
      // console.log(row.i);
      // console.log(i);

    };
    console.log(filteredData);
    // 10. Finally, rebuild the table using the filtered data
    buildTable(filteredData);
  }
  
  // 2. Attach an event to listen for changes to each filter
  d3.selectAll("#Price").on("input", updateFilters);
  d3.selectAll("#Accommodates").on("input", updateFilters);
  d3.selectAll("#Beds").on("input", updateFilters);
  d3.selectAll("#Neighborhood").on("input", updateFilters);
  d3.selectAll("#Review Rating").on("input", updateFilters);

  // Build the table when the page loads
  buildTable(tableData);
