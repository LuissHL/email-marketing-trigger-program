document.getElementById('attachFileIcon').addEventListener('click', function() {
    document.getElementById('fileInput').click();
});

let btn = document.getElementById('seta-rotate')
let isRotated = false;

function rotateButton() {
    if(isRotated){
    btn.style.transform = 'rotate(0deg)'
    } else {
        btn.style.transform = 'rotate(180deg)'
    }

    isRotated = !isRotated
}
