// // variable that keeps all the filter information
//
// var send_data = {}
//
// $(document).ready(function () {
//     // reset all parameters on page load
//
//     resetFilters();
//     // bring all the data without any filters
//
//     getAPIData();
//     // get all colleges from database via
//
//     // AJAX call into college select options
//
//     getColleges();
//     // get all varities from database via
//
//     // on selecting the college option
//
//     $('#colleges').on('change', function () {
//         // since province and region is dependent
//
//         // on college select, emty all the options from select input
//
//
//         // update the selected college
//
//         if(this.value == "all")
//             send_data['college'] = "";
//         else
//             send_data['college'] = this.value;
//
//         //get province of selected college
//
//         // get api data of updated filters
//
//         getAPIData();
//     });
//
//
//     // sort the data according to price/points
//
//     $('#sort_by').on('change', function () {
//         send_data['sort_by'] = this.value;
//         getAPIData();
//     });
//
//     // display the results after reseting the filters
//
//     $("#display_all").click(function(){
//         resetFilters();
//         getAPIData();
//     })
// })
//
//
// /**
//     Function that resets all the filters
// **/
// function resetFilters() {
//     $("#colleges").val("all");
//     $("#sort_by").val("none");
//
//     //clearing up the province and region select box
//
//     send_data['college'] = '';
//     send_data["sort_by"] = '',
//     send_data['format'] = 'json';
// }
//
// /**.
//     Utility function to showcase the api data
//     we got from backend to the table content
// **/
// function putTableData(result) {
//     // creating table row for each result and
//
//     // pushing to the html cntent of table body of listing table
//
//     let row;
//     if(result["results"].length > 0){
//         $("#no_results").hide();
//         $("#list_data").show();
//         $("#listing").html("");
//         $.each(result["results"], function (a, b) {
//             row = "<tr> <td>" + b.college + "</td>" +
//                 "<td title=\"" + b.title + "\">" + b.title.slice(0, 50) + "..." + "</td>" +
//                 "<td>" + b.college + "</td>" +
//                 "<td>" + b.subject + "</td></tr>"
//             $("#listing").append(row);
//         });
//     }
//     else{
//         // if no result found for the given filter, then display no result
//
//         $("#no_results h5").html("No results found");
//         $("#list_data").hide();
//         $("#no_results").show();
//     }
//     // setting previous and next page url for the given result
//
//     let prev_url = result["previous"];
//     let next_url = result["next"];
//     // disabling-enabling button depending on existence of next/prev page.
//
//     if (prev_url === null) {
//         $("#previous").addClass("disabled");
//         $("#previous").prop('disabled', true);
//     } else {
//         $("#previous").removeClass("disabled");
//         $("#previous").prop('disabled', false);
//     }
//     if (next_url === null) {
//         $("#next").addClass("disabled");
//         $("#next").prop('disabled', true);
//     } else {
//         $("#next").removeClass("disabled");
//         $("#next").prop('disabled', false);
//     }
//     // setting the url
//
//     $("#previous").attr("url", result["previous"]);
//     $("#next").attr("url", result["next"]);
//     // displaying result count
//
//     $("#result-count span").html(result["count"]);
// }
//
// function getAPIData() {
//     let url = $('#list_data').attr("url")
//     $.ajax({
//         method: 'GET',
//         url: url,
//         data: send_data,
//         beforeSend: function(){
//             $("#no_results h5").html("Loading data...");
//         },
//         success: function (result) {
//             putTableData(result);
//         },
//         error: function (response) {
//             $("#no_results h5").html("Something went wrong");
//             $("#list_data").hide();
//         }
//     });
// }
//
// $("#next").click(function () {
//     // load the next page data and
//
//     // put the result to the table body
//
//     // by making ajax call to next available url
//
//     let url = $(this).attr("url");
//     if (!url)
//         $(this).prop('all', true);
//
//     $(this).prop('all', false);
//     $.ajax({
//         method: 'GET',
//         url: url,
//         success: function (result) {
//             putTableData(result);
//         },
//         error: function(response){
//             console.log(response)
//         }
//     });
// })
//
// $("#previous").click(function () {
//     // load the previous page data and
//
//     // put the result to the table body
//
//     // by making ajax call to previous available url
//
//     let url = $(this).attr("url");
//     if (!url)
//         $(this).prop('all', true);
//
//     $(this).prop('all', false);
//     $.ajax({
//         method: 'GET',
//         url: url,
//         success: function (result) {
//             putTableData(result);
//         },
//         error: function(response){
//             console.log(response)
//         }
//     });
// })
//
// function getColleges() {
//     // fill the options of colleges by making ajax call
//
//     // obtain the url from the colleges select input attribute
//
//     let url = $("#colleges").attr("url");
//
//     // makes request to getColleges(request) method in views
//
//     $.ajax({
//         method: 'GET',
//         url: url,
//         data: {},
//         success: function (result) {
//
//             colleges_option = "<option value='all' selected>All colleges</option>";
//             $.each(result["colleges"], function (a, b) {
//                 colleges_option += "<option>" + b + "</option>"
//             });
//             $("#colleges").html(colleges_option)
//         },
//         error: function(response){
//             console.log(response)
//         }
//     });
// }
