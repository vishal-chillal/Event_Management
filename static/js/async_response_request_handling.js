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


var handle_fuctions = {
    "signin.html": handle_login,
    "signup.html": handle_registration,
    // "home.html": handle_home_req
};

var login_response = {
    "success": "You are logged in!",
    "Invalid": "username or password is incorrect!",
    "timeout": "Server is not respondig!"
};

function handle_login(response, user_name) {
    // show_status(login_response[response]);
    if (response == 'Success') {
        sessionStorage.setItem("session", user_name);
        // window.location.href = "dashboard.html";
        window.location.href = "signup.html";
    }
    else{
        alert("Login FAILED");
    }
}

function handle_registration(response, user_name) {
    // show_status(login_response[response]);
    if (response == 'Success') {
        alert("Login Successful....");
        window.location.href = "signin.html";
    }
    else{
        alert("registration failed");
    }

}


function excecute_service(request_json){
    $.ajax({
        type: "POST",
        dataType: "application/JSON",
        url: "/event/events",
        data: JSON.stringify(request_json),
        complete: function(data){
            if("signin.html".substring(request_json.pageName)){
                    handle_login(data.responseText, request_json.user_name);
            }
            else{
                console.log("zxcc");
            }
        }
    });
  
}

// readyState 4 
// getResponseHeader function .ajax/E.getResponseHeader() 
// getAllResponseHeaders function .ajax/E.getAllResponseHeaders() 
// setRequestHeader function .ajax/E.setRequestHeader() 
// overrideMimeType function .ajax/E.overrideMimeType() 
// statusCode function .ajax/E.statusCode() 
// abort function .ajax/E.abort() 
// state function .Deferred/i.state() 
// always function .Deferred/i.always() 
// catch function .Deferred/i.catch() 
// pipe function .Deferred/i.pipe() 
// then function .Deferred/i.then() 
// promise function .Deferred/i.promise() 
// progress function w.Callbacks/l.add() 
// done function w.Callbacks/l.add() 
// fail function w.Callbacks/l.add() 
// responseText Success 
// status 200 
// statusText OK 