function show(){
    document.getElementById("hidden").style.display = "block"
}

let images = ["https://www.mypetchicken.com/cdn/shop/products/buff-orpington-chicken2-mpc.jpg?v=1735939699&width=1946", "https://i0.wp.com/valleyhatchery.com/wp-content/uploads/2021/12/Blue-Ameraucana-Chicks.webp", "https://www.mcmurrayhatchery.com/images/global/mc/McMurrayHatchery_SingleCombBrownLeghorn.jpg", "https://thecountrysmallholder.com/wp-content/uploads/Silver-Seabright.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWS8c_kbj41LoHVdQbbopEMFXAnunuYCry-Q&s", "https://www.mypetchicken.com/cdn/shop/products/rhode-island-red-mpc_1.jpg?v=1735939578", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTEwpwTS0IvwO3LQtZ9vrrFa5B8U5eNeVOZZg&s", "https://www.heritagehatchingandhens.com.au/wp-content/uploads/2023/03/2023-03-17_11-58-38.jpg", "https://www.mypetchicken.com/cdn/shop/products/delaware-chicken-mpc_1.jpg?v=1735939718&width=600g", "https://blog.meyerhatchery.com/wp-content/uploads/2021/09/Speckled-Sussex-4-1.png"]

count = 0
function change(){
    document.getElementById("hidden").style.height = "150px"
    document.getElementById("hidden").src = images[count]
    if(count === 9){
        count = 0
    }else{
        count += 1
    }
}
