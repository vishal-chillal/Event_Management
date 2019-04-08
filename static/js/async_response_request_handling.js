// var configuration = read_configuration();
// function read_configuration() {
//     var data;
//     $.ajax({
//         type: "POST",
//         url: "../config/js_config.JSON",
//         datatype: "JSON",
//         async: false
//     }).done(function(conf) {
//         data = conf;
//     });
//     return data
// }
// var mod_python_script = configuration['mod_python'];
// var make_request_asynch = mod_python_script + "/make_request_asynch";
// var get_response_asych = mod_python_script + "/get_response_asych";
// var retry_time_intv = configuration['time_interval'];

// function excecute_service(request_json,asych) {
//     // request_json['config'] = configuration['mod_python_config'];
//     $.post(
//             make_request_asynch,
//             request_json
	
//         )
//         .done(function(request_id) {
//             console.log("request_made = ",request_id);
//             setTimeout(fetch_response, retry_time_intv);
//             function fetch_response() {
//                 var request = new Object();
//                 request['request_id'] = request_id;
//                 request['config'] = configuration['mod_python_config'];
//                 $.post(get_response_asych, request).done(function(data) {
// 		    console.log(data);
//                     if (data != request_id) {
//                         console.log("response got = ",data);
//                         clearTimeout(fetch_response);
//                         show_status("");
//                         handle_response(request_json, data)
//                     } else {
//                         clearTimeout(fetch_response);
//                         show_status("Please wait, request in process!");
//                         setTimeout(fetch_response, retry_time_intv)
//                     }
//                 });
//             }
//         });
// }

function excecute_service(request_json){
    $.ajax({ 
        type: "POST",
        dataType: "Json",
        url: "/event/events",
        data:request_json,
        success: function(data){        
        alert(data);
        }
    });
}