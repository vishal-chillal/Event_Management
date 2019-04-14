var session_id;
var pageName;



$(document).ready(function(event) {

    $("#re_password, #password").keyup(checkPasswordMatch);
    pageName = get_pagename();
    if (!("signin.html".includes(pageName)) && !("signup.html".includes(pageName))) {
	    session_id = sessionStorage.getItem("session");
	    if (!session_id) {
	        alert("please login now");
	        window.location.href = "/event/signin.html";
	    }
    }
    $("#login_btn").click(function(e) {
        e.preventDefault();
        var obj = $('.login-form').serializeArray();
        request_json = create_request(obj, pageName);
        console.log("Login request sent");
        excecute_service(request_json);
    });

    $("#signup_btn").click(function(e) {
        $("input").prop('required',true);

        e.preventDefault();
        if (document.getElementById('divCheckPasswordMatch').innerHTML != "Passwords do not match!"){
            var obj = $('.register-form').serializeArray();
            request_json = create_request(obj, pageName);
            console.log("register request sent");
            excecute_service(request_json);
        }
    }); 

    $("#log_out_btn").click(function(e) {
        e.preventDefault();
        sessionStorage.removeItem("session");
        window.location.href = "signin";
    });
    

});

function checkPasswordMatch() {
    var password = $("#password").val();
    var confirmPassword = $("#re_password").val();

    if (password != confirmPassword)
        $("#divCheckPasswordMatch").html("Passwords do not match!");
    else
        $("#divCheckPasswordMatch").html("Passwords match.");
}

function get_pagename() {
    var a = window.location.href,
        b = a.lastIndexOf("/");
    return a.substr(b + 1);
}


function show_status(msg) {
    document.getElementById('status').getElementsByTagName('span')[0].innerHTML = msg;
}


function handle_response(request_json, response) {
    if (request_json['pageName'] == 'home.html') {
        handle_fuctions[request_json['pageName']](response, request_json);
    }else if (request_json['pageName'] == 'lable.html'){
    }else {
        handle_fuctions[request_json['pageName']](response, request_json['user_name']);
    }
}


function create_request(obj, pageName) {
    var request_json = new Object()

    for (entry in obj) {
        request_json[obj[entry]['name']] = obj[entry]['value']
    }
    request_json['pageName'] = pageName;
    return request_json
}