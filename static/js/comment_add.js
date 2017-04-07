/*$('#comments__new').click(function (e){
    e.preventDefault();
    $.ajax({
        url: $('form[name=comment_new]').attr('action'),
        type: 'POST',
        data: {
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            'message': $('form textarea[name=message]').val(),
        },
        success: function(data){
            if (data){
                var div = $("<div>");
                div.attr("class","comments-item__body");
                div.appendTo('.comments__item');
                div.html("<div class='comments-item__info'><div class='comments-item-info__author'>"+$('input[name=comments_user_name]').val()+"</div><div class='comments-item-info__divider'><i class='fa fa-circle'></i></div><div class='comments-item-info__timestamp'>0 분전</div><div class='comments-item__content'>"+$('form textarea[name=message]').val()+"</div></div>");
                ///div.text($('form textarea[name=message]').val());
                //console.log($('input[name=comment_user_name]').val());

            }
            else{
                console.error('데이터가 안넘어옴');
            }
        },
        error: function(xhr,errmsg,err){
            console.error(err);
        },
    });
});*/

$('#comments__new').click(function (e){
    e.preventDefault();
        $.ajax({
        url: $('form[name=comment_new]').attr('action'),
        type: 'POST',
        data: {
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            'message': $('form textarea[name=message]').val(),
        },
        success: function(data){
            if (data){
                $('.comments').html(data);

            }
            else{
                console.error('데이터가 안넘어옴');
            }
        },
        error: function(xhr,errmsg,err){
            console.error(err);
        },
        complete: function() {
            $.getScript(js_root, function(){});
        }
    });
});
