
$(document).on('click', '#show', function () {
    console.log('khasbcjhbasc')

    // var x = $("#password_show").val();
    let input = $(this).parent().find("#password");
    input.attr('type', input.attr('type') === 'password' ? 'text' : 'password');
})


$(document).on('click', '#btnsave', function () {
    
    let name = $('#name').val();

    let email = $('#email').val();
    console.log(email);
    let password = $('#password').val();
    console.log(password);

    let csr = $('input[name= csrfmiddlewaretoken]').val();

    if (name == '') {
        console.log('please enter the username')
        $('#username_msg').html('Please enter username')
    }
    else if (email == '' || email.length == '@gmail.com') {
        console.log('please enter the valid email')
        $('#email_msg').html('please enter valid email')
    }
    else if (password == '') {
        console.log('please enter the password')
        $('#pass_msg').html('enter the password')
    }
    else {
        console.log(name);
        console.log(email);
        console.log(password);
        let my_obj = { name:name , email:email , password:password ,  csrfmiddlewaretoken: csr }
        console.log(my_obj);
        $.ajax({
            url: '/signup/',
            method: 'POST',
            data: my_obj,
            success: function(data){
                console.log(data);
                $('form')[0].reset();
            }

        })

    }
})

