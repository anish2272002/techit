var loadFile = function(event){
    var output = document.getElementById('image_file');
    if(event.target.files[0]){
        output.src = URL.createObjectURL(event.target.files[0]);
        output.onload = function() {
            URL.revokeObjectURL(output.src)
        };
    }
};

const addBtn = document.querySelector("#add-image-btn");
const imgfile = document.querySelector("#id_file");
const backdropClose = document.querySelector(".backdrop-close");
const errorlist = document.querySelector(".errorlist");

if(errorlist){
    errorlist.style.cssText = "list-style-type:none;";
    errorlist.firstChild.classList.add('alert');
    errorlist.firstChild.classList.add('alert-danger');
}

if(imgfile){
    addBtn.addEventListener("click",()=>{
        document.querySelector(".backdrop").style.display = 'flex';
    })
    imgfile.style.display = 'none';
    imgfile.addEventListener("change",loadFile);
}
if(backdropClose){
    backdropClose.addEventListener("click",()=>{
        document.querySelector(".backdrop").style.display = 'none';
    })
}