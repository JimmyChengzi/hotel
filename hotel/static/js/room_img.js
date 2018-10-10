/**
 * Created by tarena on 18-10-10.
 */
function imgshow(event) {
    var file = event.target.files || event.dataTransfer.files
    if(file){
        var reader = new FileReader();
        reader.onload = function () {
            $("#imgshow").attr("src",this.result)
        };
        reader.readAsDataURL(file[0])
    }
}
$(function () {
    $("#uploadimg").change(function (event) {
        imgshow(event);
    })
});