function show(){
    document.getElementById("hidden").style.display = "block"
}

let images = ["https://www.mypetchicken.com/cdn/shop/products/buff-orpington-chicken2-mpc.jpg?v=1735939699&width=1946", "https://i0.wp.com/valleyhatchery.com/wp-content/uploads/2021/12/Blue-Ameraucana-Chicks.webp", "https://www.mcmurrayhatchery.com/images/global/mc/McMurrayHatchery_SingleCombBrownLeghorn.jpg", "https://thecountrysmallholder.com/wp-content/uploads/Silver-Seabright.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWS8c_kbj41LoHVdQbbopEMFXAnunuYCry-Q&s", "", "", "", "", "", ""]

count = 0
function change(){
    document.getElementById("img").style.height = "150px"
    document.getElementById("img").src = "https://media.istockphoto.com/id/149078834/photo/mount-timpanogos.jpg?s=612x612&w=0&k=20&c=lAyRPoZZ17xlIfoYFDrx0ZP5HaIwh4u1AItsqNSpwxk="
    document.getElementById("img").src = images[count]
    if(count === 9){
        count = 0
    }else{
        count += 1
    }
}
