var url_dict = {
    "signin": "/event/login_user",
    "signup": "/event/register_user",
    "dashboard": "/event/add_event"
}

var handle_fuctions = {
    "signin": handle_login,
    "signup": handle_registration,
    "dashboard": handle_dashboard
};
function render_all_events(all_event_list) {
    var array = all_event_list;
    var entries = ["id", "event_name", "location", "date_time", "capacity"]
    var str = "<thead><tr>"
    for (var i = 0; i < entries.length; i++) {
        str += "<th>" + entries[i] + "</th>"
    }
    str += "</tr></thead>"

    for (let index = 0; index < array.length; index++) {
        const element = array[index];
        str += "<tr>"
        for (var i = 0; i < entries.length; i++) {
            str += "<td>" + element[entries[i]] + "</td>"
        }
        str += "</tr>"
    }
    $("#event_table_id").html(str);
}

function handle_dashboard(response, status, user_name) {
    // console.log(response, status);
    // handle server is not responding
    if (status == 200){
    response = JSON.parse(response)
    var all_event_list = response.all_events
    render_all_events(all_event_list);
}
else if (status == 200){
    location.reload()
    console.log("Event created")
}
else{
    console.log(response)
}

}


var response_msg = {
    200: "You are logged in!",
    201: "registration Successful",
    403: "username or password is incorrect!",
    408: "Server is not respondig!",
    409: "username already exists"
};

function handle_login(response, status, user_name) {
    if (response == 'Success') {
        sessionStorage.setItem("session", user_name);
        console.log(response_msg[status]);
        window.location.href = "dashboard";
    }
    else {
        console.log(response_msg[status]);
        console.log("Login Failed");
    }
}

function handle_registration(response, status, user_name) {
    // show_status(login_response[response]);
    if (response == 'Success') {
        console.log(response_msg[status]);
        window.location.href = "signin";
    }
    else {
        console.log(response_msg[status]);
        console.log("registration failed");
    }

}

function excecute_service(request_json, method = "POST") {
    $.ajax({
        type: method,
        dataType: "application/JSON",
        url: url_dict[request_json.pageName],
        data: JSON.stringify(request_json),
        complete: function (data) {
            handle_fuctions[request_json.pageName](data.responseText, data.status, request_json.user_name)
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