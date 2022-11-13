videocontainers = document.querySelectorAll(".gallery-video-container");
videocontainers.forEach((videocontainer) => {
    videocontainer.addEventListener("click",()=>{
        if(videocontainer.children[0].paused){
            videocontainer.children[0].setAttribute("controls","controls");
            document.querySelectorAll("video").forEach((video)=>{
                if(video!=videocontainer.children[0]){
                    video.pause()
                }
            })
            videocontainer.children[0].play();
            videocontainer.children[1].style.display = "none";
        }else{
            videocontainer.children[0].removeAttribute("controls");
            videocontainer.children[0].pause();
            videocontainer.children[1].style.display = "block";
        }
    })
});