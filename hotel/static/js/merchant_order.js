/**
 * Created by tarena on 18-9-29.
 */
function changepage(event){
    var page = event.target.name;
    console.log('调用merchant_order.js')
    $.ajax({
        url:"/merchant_orders/m_o_pages/",
        type:"post",
        data:{
            csrfmiddlewaretoken:$("[name='csrfmiddlewaretoken']").val(),
            page:page
        },
        dataType:"json",
        async:false,
        success:function (data) {
            var orderhtml = '';
            var pagehtml = '';
            console.log(data.showorders);
            var orders = JSON.parse(data.showorders);
            var pagelist = JSON.parse(data.pagelist);
            $.each(orders,function (i,obj) {
                var order = obj.fields;
                var ordermsg = order.ordermessage;
                var orderid = order.orderid;
                orderhtml += "<div name='"+orderid+"'>"+ordermsg+"</div>";
            });
            $.each(pagelist,function (i,obj) {
                pagehtml += "<button name='page"+obj+"' class='pagebtn'>"+obj+"</button> "
            });
            console.log(orderhtml);
            console.log(pagehtml);
            $("#showorders").html(orderhtml);
            $("#showbtns").html(pagehtml);
        }
    })
}

$(function () {
    console.log('调用merchant_order.js')
    // $(".pagebtn").click(function (event) {
    //     changepage(event);
    // })
    $("#showbtns").on("click","button",function (event) {
        changepage(event);
    })
});