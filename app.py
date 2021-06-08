<!doctype html>
<html lang="en">
    <head>

        <!-- Webpage Title -->
        <title>예약HAIR</title>

        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bulma CSS -->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.1/css/bulma.min.css">
        <!-- Font Awesome CSS -->
        <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">

        <!-- JS -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-cookie/1.4.1/jquery.cookie.js"></script>
        <style>
            body {
    background-image:url("../static/hair.png");
    min-height: 100vh;

}

.section {
    padding: 1rem 1.5rem;
    max-width: 750px;
    margin: auto;
}

.title {
    font-weight: 800;
    font-size: 5rem;
}

.subtitle {
    font-size: 2rem;
}

.logo img{
    width: 200px;
    position:relative;
    bottom:65px;
    display: block;
    background: black;
}

.button.is-sparta {
    background-color: black;
    border-color: white;
    color: #fff !important;
    transition: all .3s linear;
    border-radius: 30px;
}

.button.is-sparta.is-outlined {
    background-color: black;
    border-color: white;
    color: white !important;
    border-radius: 30px;
}
.button.is-sparta:hover{
     color:green;
}
.help {
    color: gray;
}
        </style>
        <script>
            // {% if msg %}
            //     alert("{{ msg }}")
            // {% endif %}
     function sign_in() {
    let username = $("#input-username").val()
    let password = $("#input-password").val()

    if (username == "") {
        $("#help-id-login").text("아이디를 입력해주세요.")
        $("#input-username").focus()
        return;
    } else {
        $("#help-id-login").text("")
    }

    if (password == "") {
        $("#help-password-login").text("비밀번호를 입력해주세요.")
        $("#input-password").focus()
        return;
    } else {
        $("#help-password-login").text("")
    }
    $.ajax({
        type: "POST",
        url: "/sign_in",
        data: {
            username_give: username,
            password_give: password
        },
        success: function (response) {
            if (response['result'] == 'success') {
                $.cookie('mytoken', response['token'], {path: '/'});
                window.location.replace("/")
            } else {
                alert(response['msg'])
            }
        }
    });
}
       function sign_up() {
    let username = $("#input-username").val()
    let password = $("#input-password").val()
    let password2 = $("#input-password2").val()
    console.log(username, password, password2)


    if ($("#help-id").hasClass("is-danger")) {
        alert("아이디를 다시 확인해주세요.")
        return;
    } else if (!$("#help-id").hasClass("is-success")) {
        alert("아이디 중복확인을 해주세요.")
        return;
    }

    if (password == "") {
        $("#help-password").text("비밀번호를 입력해주세요.").removeClass("is-safe").addClass("is-danger")
        $("#input-password").focus()
        return;
    } else if (!is_password(password)) {
        $("#help-password").text("비밀번호의 형식을 확인해주세요. 영문과 숫자 필수 포함, 특수문자(!@#$%^&*) 사용가능 8-20자").removeClass("is-safe").addClass("is-danger")
        $("#input-password").focus()
        return
    } else {
        $("#help-password").text("사용할 수 있는 비밀번호입니다.").removeClass("is-danger").addClass("is-success")
    }
    if (password2 == "") {
        $("#help-password2").text("비밀번호를 입력해주세요.").removeClass("is-safe").addClass("is-danger")
        $("#input-password2").focus()
        return;
    } else if (password2 != password) {
        $("#help-password2").text("비밀번호가 일치하지 않습니다.").removeClass("is-safe").addClass("is-danger")
        $("#input-password2").focus()
        return;
    } else {
        $("#help-password2").text("비밀번호가 일치합니다.").removeClass("is-danger").addClass("is-success")
    }
    $.ajax({
        type: "POST",
        url: "/sign_up/save",
        data: {
            username_give: username,
            password_give: password
        },
        success: function (response) {
            alert("회원가입을 축하드립니다!")
            window.location.replace("/login")
        }
    });

}
            function toggle_sign_up() {
    $("#sign-up-box").toggleClass("is-hidden")
    $("#div-sign-in-or-up").toggleClass("is-hidden")
    $("#btn-check-dup").toggleClass("is-hidden")
    $("#help-id").toggleClass("is-hidden")
    $("#help-password").toggleClass("is-hidden")
    $("#help-password2").toggleClass("is-hidden")
}
        function is_nickname(asValue) {
            var regExp = /^(?=.*[a-zA-Z])[-a-zA-Z0-9_.]{2,10}$/;
            return regExp.test(asValue);
        }

        function is_password(asValue) {
            var regExp = /^(?=.*\d)(?=.*[a-zA-Z])[0-9a-zA-Z!@#$%^&*]{8,20}$/;
            return regExp.test(asValue);
        }
        function check_dup() {
    let username = $("#input-username").val()
    console.log(username)
    if (username == "") {
        $("#help-id").text("아이디를 입력해주세요.").removeClass("is-safe").addClass("is-danger")
        $("#input-username").focus()
        return;
    }
    if (!is_nickname(username)) {
        $("#help-id").text("아이디의 형식을 확인해주세요. 영문과 숫자, 일부 특수문자(._-) 사용 가능. 2-10자 길이").removeClass("is-safe").addClass("is-danger")
        $("#input-username").focus()
        return;
    }
    $("#help-id").addClass("is-loading")
    $.ajax({
        type: "POST",
        url: "/sign_up/check_dup",
        data: {
            username_give: username
        },
        success: function (response) {

            if (response["exists"]) {
                $("#help-id").text("이미 존재하는 아이디입니다.").removeClass("is-safe").addClass("is-danger")
                $("#input-username").focus()
            } else {
                $("#help-id").text("사용할 수 있는 아이디입니다.").removeClass("is-danger").addClass("is-success")
            }
            $("#help-id").removeClass("is-loading")

        }
    });
}
        </script>

    </head>
    <body>
<section class="hero is-white">
    <div class="hero-body has-text-centered" style="padding-bottom:1rem;margin:auto;">
      <div class="logo"> <img class="title is-sparta" src="../static/logo.jpeg"/></div>

    </div>
</section>
    <section class="section">
    <div class="container">
        <div class="box" style="max-width: 630px;margin:auto;">
            <article class="media">
                <div class="media-content">
                    <div class="content">
                        <div class="field has-addons">
                            <div class="control has-icons-left" style="width:100%">
                                <input id="input-username" class="input" type="text" placeholder="아이디">
                                <span class="icon is-small is-left"><i class="fa fa-user"></i></span>
                            </div>
                            <div id="btn-check-dup" class="control is-hidden">
                                <button class="button is-sparta" onclick="check_dup()">중복확인</button>
                            </div>

                        </div>
                        <p id="help-id" class="help is-hidden">아이디는 2-10자의 영문과 숫자와 일부 특수문자(._-)만 입력 가능합니다.</p>
                        <p id="help-id-login" class="help is-danger"></p>

                        <div class="field">
                            <div class="control has-icons-left">
                                <input id="input-password" class="input" type="password" placeholder="비밀번호">
                                <span class="icon is-small is-left"><i class="fa fa-lock"></i></span>
                            </div>
                            <p id="help-password" class="help is-hidden">영문과 숫자 조합의 8-20자의 비밀번호를 설정해주세요. 특수문자(!@#$%^&*)도 사용 가능합니다.</p>
                        </div>


                    </div>
                    <div id="div-sign-in-or-up" class="has-text-centered">
                        <nav class="level is-mobile">
                            <button class="level-item button is-sparta" onclick="sign_in()">
                                로그인
                            </button>

                        </nav>
                        <hr>
                        <h4 class="mb-3">회원이 아니신가요?</h4>
                        <nav class="level is-mobile">

                            <button class="level-item button is-sparta is-outlined"
                                    onclick="toggle_sign_up()">
                                새 계정 만들기
                            </button>
                        </nav>
                    </div>

                    <div id="sign-up-box" class="is-hidden">
                        <div class="mb-5">
                            <div class="field">
                                <div class="control has-icons-left" style="width:100%">
                                    <input id="input-password2" class="input" type="password"
                                           placeholder="비밀번호 재입력">
                                    <span class="icon is-small is-left"><i class="fa fa-lock"></i></span>
                                </div>
                                <p id="help-password2" class="help is-hidden">비밀번호를 다시 한 번 입력해주세요.</p>

                            </div>
                        </div>
                        <nav class="level is-mobile">
                            <button class="level-item button is-sparta" onclick="sign_up()">
                                회원가입
                            </button>
                            <button class="level-item button is-sparta is-outlined" onclick="toggle_sign_up()">
                                취소
                            </button>
                        </nav>
                    </div>


                </div>
            </article>
        </div>

    </div>
</section>
    </body>
</html>
