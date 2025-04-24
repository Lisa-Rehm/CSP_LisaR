function push(){
    if(document.getElementById("brodmann").style.display != "block"){
        document.getElementById("brodmann").style.display = "block"
    document.getElementById("btn").innerHTML = "Show Less"
    }else{
        document.getElementById("brodmann").style.display = "none"
    document.getElementById("btn").innerHTML = "Click here if you want to know more about Brodmann Areas!"
    }
}
let images = ["https://www.simplypsychology.org/wp-content/uploads/brodmanns-areas-1536x864.jpeg", "https://www.simplypsychology.org/wp-content/uploads/Brodmann-areas-map-1536x1194.jpeg"]

count = 0
function change(){
    document.getElementById("img").style.width = "400px"
    document.getElementById("img").src = "https://media.istockphoto.com/id/149078834/photo/mount-timpanogos.jpg?s=612x612&w=0&k=20&c=lAyRPoZZ17xlIfoYFDrx0ZP5HaIwh4u1AItsqNSpwxk="
    document.getElementById("img").src = images[count]
    if(count === 1){
        count = 0
    }else{
        count += 1
    }
}