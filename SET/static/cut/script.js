const $upload = $('#upload'),
    $crop = $('#crop'),
    $result = $('#result'),
    $croppie = $('#croppie');

var cr,
    cr_img = '',
    img_w = 320,
    img_h = 320,
    isCrop = 0;

//アップロードファイルの判定
$(function () {
    if (window.File && window.FileList && window.FileReader)
        fileInit();
    else
        alert('ご使用のデバイスに対応していません');
});

//********* file select/drop *********
var fileselect = document.getElementById("image"),
    filedrag = document.getElementById("filedrag");

function fileInit() {
    // file select
    fileselect.addEventListener("change", FileSelectHandler, false);
    // is XHR2 available?
    var xhr = new XMLHttpRequest();
    // file drop
    if (xhr.upload) {
        filedrag.addEventListener("dragover", FileDragHover, false);
        filedrag.addEventListener("dragleave", FileDragHover, false);
        filedrag.addEventListener("drop", FileSelectHandler, false);
    }
}

// file selection
function FileSelectHandler(e) {
    // cancel event and hover styling
    FileDragHover(e);
    // fetch FileList object
    var files = e.target.files || e.dataTransfer.files;
    if (files[0] && files[0].type.match('image.*')) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $upload.hide();
            if (cr_img == '') { //最初のアップロード
                cr_img = e.target.result;
                cropInit();
            }
            else {// 画像のバインド
                cr_img = e.target.result;
                bindCropImg();
            }
            $crop.fadeIn(300);
        }
        reader.readAsDataURL(files[0]);
    }
}

// file drag hover
function FileDragHover(e) {
    e.stopPropagation();
    e.preventDefault();
    filedrag.className = (e.type == "dragover" ? "hover" : "");
}

//********* crop *********
//トリミングの設定
function cropInit() {
    cr = $croppie.croppie({
        viewport: {
            width: img_w,
            height: img_h
        },
        boundary: {
            width: img_w,
            height: img_h
        },
        mouseWheelZoom: false,
        enableOrientation: true
    });

    $(".cr-slider-wrap")

    bindCropImg();
}

//画像のバインド
function bindCropImg() {
    cr.croppie('bind', {
        url: cr_img
    });
}

//回転
function cropRotate(deg) {
    cr.croppie('rotate', parseInt(deg));
}

//トリミングの中止
function cropCancel() {
    if ($upload.is(':hidden')) {
        $upload.fadeIn(300).siblings().hide();
        fileselect.value = "";
        isCrop = 0;
    }
}

//画像の切り抜き
function cropResult() {
    if (!isCrop) {
        isCrop = 1;
        cr.croppie('result', {
            type: 'canvas', // canvas(base64)|html
            size: { width: img_w, height: img_h }, //'viewport'|'original'|{width:500, height:500}
            format: 'jpeg', //'jpeg'|'png'|'webp'
            quality: 1 //0~1
        }).then(function (resp) {
            $crop.hide();
            $result.find('img').attr('src', resp);
            $result.fadeIn(300);
        });
			// document.getElementById('image1').innerHTML = numx;
    }
}

