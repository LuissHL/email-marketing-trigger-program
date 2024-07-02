


function previewText() {
    let preview = document.getElementById('btn-preview')
    preview.ariaSelected = true

    let write = document.getElementById('btn-write')
    write.ariaSelected = false
}

function writeText() {
    let write = document.getElementById('btn-write')
    write.ariaSelected = true


    let preview = document.getElementById('btn-preview')
    preview.ariaSelected = false
}