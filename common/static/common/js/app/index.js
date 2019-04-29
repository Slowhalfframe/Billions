function show_child_menu(obj) {
    $.ajax({
        url:'/get_child_menu?id='+obj,
        method:'GET',
        types:'json',
        success:function (data) {
            if (data.code >= 0){
                $('#menu'+obj)[0].onmouseenter = '';
                if(data.data.length > 0){
                    count = 0;
                    li = '';
                    while (count<data.data.length) {
                        li_html = '<li><a href="'+data.data[count].link+'">'+ data.data[count].name +'</a></li>';
                        count += 1
                    }
                    li += li_html;
                    $('#menu'+obj).append('<ul class="sub">'+li+'</ul>');
                    $('#menu'+obj).attr('class','menu');
                }else{

                }

            }else{
                alert("网络异常")
            }
        }
    })
}