function uploadOnclick() {
    $("#file-selector").click();
}

function fileOnChange() {
    let selectedFile = $("#file-selector").prop("files")[0];
    doUpload(selectedFile);
}

function popUp() {
    $("#pop-up, #pop-up *").css("display", "block");
    $("body *:not('#pop-up, #pop-up *')").css("filter", "blur(10px)");
}

function doUpload(uploadFile) {
    formdata = new FormData();
    formdata.append("file", uploadFile);
    $.ajax({
        type: "POST",
        url: "api",
        data: formdata,
        cache: false,
        processData: false,
        contentType: false,
        success: resp => {
            resp = JSON.parse(resp);
            if (resp["status"] == "success") {
                $("#img-res").attr("src", "data:image/png;base64," + resp["image"]);
                popUp();
            }
        }
    })
}
