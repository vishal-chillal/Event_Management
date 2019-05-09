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
    var entries = ["event_name", "location", "capacity", "date_time"]
    var str = "<thead><tr>"
    var colour_dict = {
        "Out door Sports": "primary",
        "Indoor Sports": "success",
        "Movie": "info",
        "Conference": "secondary",
        "Dinner": "danger"
    }
    for (var i = 0; i < entries.length; i++) {
        str += "<th>" + entries[i] + "</th>"
    }
    str += "</tr></thead>"

    for (let index = 0; index < array.length; index++) {
        const element = array[index];
        str += "<tr>"
        for (var i = 0; i < entries.length; i++) {
            str += "<td>"
            if (i == entries.indexOf("event_name")) {
                str += '<span class="mr-2"> <i class="fas fa-circle text-' + colour_dict[element.event_type] + '"></i></span> '
            }
            str += element[entries[i]] + "</td>"
        }
        str += "</tr>"
    }
    $("#event_table_id").html(str);
}

function handle_dashboard(response, status, user_name) {
    // console.log(response, status);
    // handle server is not responding
    if (status == 200) {
        response = JSON.parse(response)
        var all_event_list = response.all_events
        render_all_events(all_event_list);
    }
    else if (status == 200) {
        location.reload()
        console.log("Event created")
    }
    else {
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
        var msg = response_msg[status] + "<h3> Login Failed</h3>"
        $("#errorMsg").html(msg);
    }
}

function handle_registration(response, status, user_name) {
    // show_status(login_response[response]);
    if (response == 'Success') {
        console.log(response_msg[status]);
        window.location.href = "signin";
    }
    else {
        var msg = response_msg[status] + "<h3>Registration Failed</h3>"
        $("#errorMsg").html(msg);
    }

}

function excecute_service(request_json, method = "POST") {
    if (request_json == -1) {

        var msg = "<h4> Please fill the required fields </h4>"
        $("#errorMsg").html(msg);
        document.getElementById("errorMsg").style.color = "red";
        return;
    }
    console.log(request_json, typeof (request_json));
    $.ajax({
        type: method,
        dataType: "application/JSON",
        url: url_dict[request_json.pageName],
        data: JSON.stringify(request_json),
        // data: request_json,
        complete: function (data) {
            handle_fuctions[request_json.pageName](data.responseText, data.status, request_json.user_name)
        }
    });

}