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
            if(data.status=="1") {
                var orderhtml = '';
                var pagehtml = '';
                console.log(data.showorders);
                var orders = JSON.parse(data.showorders);
                var pagelist = JSON.parse(data.pagelist);
                var page = data.page;
                var lastpage = data.lastpage;
                var rightpage = (Number(page) + 1).toString();
                var leftpage = (Number(page) - 1).toString();
                $.each(orders, function (i, obj) {
                    var order = obj.fields;
                    var ordermsg = order.ordermessage;
                    var orderid = order.orderid;
                    orderhtml += "<div name='" + orderid + "'>" + ordermsg + "</div>";
                });
                pagehtml += "<button id='left' name='page" + leftpage + "'";
                if (page == "1") {
                    pagehtml += " disabled='disabled'"
                }
                console.log("-----------pagehtml:" + pagehtml);
                pagehtml += '>上一页</button> ';
                console.log("-----------pagehtml:" + pagehtml);
                $.each(pagelist, function (i, obj) {
                    pagehtml += "<button name='page" + obj + "' class='pagebtn'";
                    console.log(obj);
                    console.log(page);
                    if (page == obj) {
                        pagehtml += " disabled='disabled' id='onpage'"
                    }
                    pagehtml += '>';
                    pagehtml += obj;
                    pagehtml += "</button> ";
                });
                pagehtml += "<button id='right' name='page" + rightpage + "' ";
                if (page == lastpage) {
                    pagehtml += "disabled='disabled'"
                }
                pagehtml += '>下一页</button>';
                console.log(orderhtml);
                console.log(pagehtml);
                $("#showorders").html(orderhtml);
                $("#showbtns").html(pagehtml);
            }else{
                $("#main").html("数据已更新，请刷新页面")
            }
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