/**
 * Created by tarena on 18-9-29.
 */
function changepage(event){
    var page = event.target.name
    $.ajax({
        url:"/merchant_manage/m_o_pages/",
        type:"post",
        data{
            csrfmiddlewaretoken:$("[name='csrfmiddlewaretoken']").val(),
            page:page
        },
        dataType:"json",
        async:false,
        success:function (data) {
            if(data.status==0){
                var orderhtml = ''
                var pagehtml = ''
                $.each(data,function (i,obj) {
                    var thepage = toString(i+1);
                    var order = JSON.parse(obj);
                    var ordermsg = order.message;
                    var orderid = order.id;
                    orderhtml += "<div name='"+orderid+"'>"+ordermsg+"</div>";
                    pagehtml += "<button value='"+thepage+"'>"+thepage+"</button>"
                });
                var html = orderhtml + pagehtml
                $("#ordershow").html(html)
            }
        }
    })
}

$(function () {
    $(".pagebtn").click(function (event) {
        changepage(event);
    })
});