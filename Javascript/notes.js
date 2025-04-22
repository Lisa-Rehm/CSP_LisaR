let images = ["https://images.squarespace-cdn.com/content/v1/63c60d44c98af85334537583/644359f9-c213-4d77-bdb0-b78b7f8424f3/Mount_Timpanogos_at_sunset.jpg", "https://media.istockphoto.com/id/149078834/photo/mount-timpanogos.jpg?s=612x612&w=0&k=20&c=lAyRPoZZ17xlIfoYFDrx0ZP5HaIwh4u1AItsqNSpwxk=", "https://i.etsystatic.com/37394532/r/il/27e6c7/5018857984/il_fullxfull.5018857984_l9h3.jpg"]
function hello(){
    document.getElementById("title").style.color = "green"
    document.getElementById("title").innerHTML = "Hello World"
}

count = 0
function change(){
    document.getElementById("img").style.height = "150px"
    document.getElementById("img").src = "https://media.istockphoto.com/id/149078834/photo/mount-timpanogos.jpg?s=612x612&w=0&k=20&c=lAyRPoZZ17xlIfoYFDrx0ZP5HaIwh4u1AItsqNSpwxk="
    document.getElementById("img").src = images[count]
    if(count === 2){
        count = 0
    }else{
        count += 1
    }
}

function highlight(){
    document.getElementById("btn").style.backgroundColor = "orange"
    document.getElementById("btn").style.color = "white"
}

function normal(){
    document.getElementById("btn").style.backgroundColor = "gray"
    document.getElementById("btn").style.color = "black"
}

function show(){
    document.getElementById("hidden").style.display = "block"
}

function pop(){
    
}