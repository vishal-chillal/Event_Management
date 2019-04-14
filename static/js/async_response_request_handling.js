var url_dict = {
    "signin": "/event/login_user",
    "signup": "/event/register_user"
}

var handle_fuctions = {
    "signin": handle_login,
    "signup": handle_registration,
    // "home.html": handle_home_req
};

var response_msg = {
    200 : "You are logged in!",
    201 : "registration Successful",
    403 : "username or password is incorrect!",
    408 : "Server is not respondig!",
    409 : "username already exists"
};

function handle_login(response, status, user_name) {
    if (response == 'Success') {
        sessionStorage.setItem("session", user_name);
        console.log(response_msg[status]);

        window.location.href = "dashboard.html";
        // window.location.href = "signup.html";
    }
    else{
        console.log(response_msg[status]);
        console.log("Login Failed");
    }
}

function handle_registration(response, status, user_name) {
    // show_status(login_response[response]);
    if (response == 'Success') {
        console.log(response_msg[status]);
        // window.location.href = "signin";
    }
    else {
        console.log(response_msg[status]);
        console.log("registration failed");
    }

}


function excecute_service(request_json){
    $.ajax({
        type: "POST",
        dataType: "application/JSON",
        url: url_dict[request_json.pageName],
        data: JSON.stringify(request_json),
        complete: function(data){
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