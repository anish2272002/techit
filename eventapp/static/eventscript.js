var slider = document.getElementById("id_duration");
if(slider){
    slider.style.cursor = 'pointer';
    var output = document.getElementById("duration_value");
    output.innerHTML = slider.value+" hour";
    output.style.width = (slider.value*100/48)+'%';
    slider.oninput = function() {
        if(this.value<=1){
            output.innerHTML = this.value+" hour";
            output.style.width = (slider.value*100/48)+'%';
        }else{
            output.innerHTML = this.value+" hours";
            output.style.width = (slider.value*100/48)+'%';
        }
    }
}

var loadFile = function(event){
    var output = document.getElementById('event_picture');
    if(event.target.files[0]){
        output.src = URL.createObjectURL(event.target.files[0]);
        output.onload = function() {
        URL.revokeObjectURL(output.src) // free memory
        };
    }
};
const imginp = document.querySelector("#id_picture");
if(imginp){
    imginp.style.display = 'none';
    imginp.addEventListener("change",loadFile);
}