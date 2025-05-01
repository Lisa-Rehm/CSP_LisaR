let images = ["https://lh3.googleusercontent.com/p/AF1QipNk54IMo6U4YNXEnM61MrnIBv0HYMdjDLqVgLTT=s680-w680-h510", "https://npr.brightspotcdn.com/legacy/sites/knau/files/201912/arch1.jpg", "https://images.discerningassets.com/image/upload/c_fit,h_1000,w_1000/c_fit,fl_relative,h_1.0,o_100,w_1.0/v1565830969/Sacred_Land_20x30_izxyli.jpg", "https://www.nps.gov/rabr/learn/nature/images/rainbow-animation.jpg?maxwidth=1300&maxheight=1300&autorotate=false&format=webp"]

count = 0
function change(){
    document.getElementById("one").style.width = "625px"
    document.getElementById("one").src = images[count]
    if(count === 3){
        count = 0
    }else{
        count += 1
    }
}

let reasons = ["https://i.ytimg.com/vi/3_0iOHDBIkg/maxresdefault.jpg", "https://cross-country-trips.com/sites/default/files/images/7k/180707_082431_6153.preview.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJCR2cDdXd02rAIXRcJnuqhyR5D0w8KigRXA&s", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQjgKaBbBS7R9LVct2m4eG3Pic4eBTkkPEKQ&s"]

coun = 0
function dif(){
    document.getElementById("two").style.width = "625px"
    document.getElementById("two").src = reasons[coun]
    if(coun === 3){
        coun = 0
    }else{
        coun += 1
    }
}

let native = ["https://res.cloudinary.com/simpleview/image/upload/v1544569460/clients/scottsdale/Hopi_Dancers_on_Feast_Days_499de77f-906e-4f95-9d05-cb1b90615900.jpg", "https://ndcfs.org/wp-content/uploads/2024/09/navajo-nation-generations960.jpg", "https://www.uvu.edu/news/2023/11/images/2023_11_02_native_american_heritage_month_1.jpg", "https://i0.wp.com/newmexiconomad.com/wp-content/uploads/2023/10/Gallup-Inter-Tribal-Ceremonial-PowWow-Zuni-Olla-dancers.jpg?ssl=1", "https://www.naturalarches.org/blog/wp-content/uploads/2017/09/rainbow-bridge-national-monument-do-not-approach-sign.jpg"]
num = 0
function diff(){
    document.getElementById("three").style.width = "700px"
    document.getElementById("three").src = native[num]
    if(num === 4){
        num = 0
    }else{
        num += 1
    }
}

function push(){
    if(document.getElementById("bottom").style.display != "grid"){
        document.getElementById("bottom").style.display = "grid"
    document.getElementById("btn").innerHTML = "Show Less"
    }else{
        document.getElementById("bottom").style.display = "none"
    document.getElementById("btn").innerHTML = "Click here for more information!"
    }
}