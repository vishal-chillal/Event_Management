var session_id;
var pageName;

var handle_fuctions = {
    "login.html": handle_login,
    // "reg.html": handle_reg,
    // "home.html": handle_home_req
};
var login_response = {
    "success": "You are logged in!",
    "Invalid": "username or password is incorrect!",
    "timeout": "Server is not respondig!"
};


$(document).ready(function(event) {
    pageName = get_pagename();
    if (pageName != "signin.html" && pageName != "signup.html") {
	    session_id = sessionStorage.getItem("session");
	    if (!session_id) {
	        alert("please login");
	        window.location.href = "signin.html";
	    }
    }
    if (session_id && pageName != "lable.html") {
	get_service_list();
	document.getElementById('home').getElementsByTagName('span')[0].innerHTML = "welcome " + session_id;
    }
});

function get_pagename() {
    var a = window.location.href,
        b = a.lastIndexOf("/");
    return a.substr(b + 1);
}


function handle_login(response, user_name) {
    show_status(login_response[response]);
    if (response == 'success') {
        sessionStorage.setItem("session", user_name);
        window.location.href = "home.html";
    }
}

function show_status(msg) {
    document.getElementById('status').getElementsByTagName('span')[0].innerHTML = msg;
}

$("#register").click(function(e) {
	e.preventDefault();
	window.location.href = "reg.html";
});

$("#log_out").click(function(e) {
	e.preventDefault();
	sessionStorage.removeItem("session");
	window.location.href = "login.html";
});

function handle_response(request_json, response) {
    if (request_json['pageName'] == 'home.html') {
        handle_fuctions[request_json['pageName']](response, request_json);
    }else if (request_json['pageName'] == 'lable.html'){
    }else {
        handle_fuctions[request_json['pageName']](response, request_json['user_name']);
    }
}

$(document).ready(function(event) {
    $("#login_btn").click(function(e) {
        e.preventDefault();
        request_json = create_login_request();
        console.log("Login request sent");
        excecute_service(request_json);
        // test(request_json);
    });
});


function create_login_request() {
    var obj = $('.login-form').serializeArray();
    var request_json = new Object()
    for (entry in obj) {
        request_json[obj[entry]['name']] = obj[entry]['value']
    }
    request_json['pageName'] = 'signin.html';
    return request_json
}