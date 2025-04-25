let images = ["https://lh3.googleusercontent.com/p/AF1QipNk54IMo6U4YNXEnM61MrnIBv0HYMdjDLqVgLTT=s680-w680-h510", "https://npr.brightspotcdn.com/legacy/sites/knau/files/201912/arch1.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3Nr5VCBZIMENzs8WiZPigvecq6FX5NgU8qA&s", "https://images.discerningassets.com/image/upload/c_fit,h_1000,w_1000/c_fit,fl_relative,h_1.0,o_100,w_1.0/v1565830969/Sacred_Land_20x30_izxyli.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVXMVBeKZ5JHTyBPkOQ6k2QZt6CDAjuJ_DqgwBGYjbjkwTLdTY3_1sgxA5SOOVZLj2J0M&usqp=CAU", "https://i.ytimg.com/vi/3_0iOHDBIkg/maxresdefault.jpg"]

count = 0
function change(){
    document.getElementById("one").style.height = "150px"
    document.getElementById("one").src = images[count]
    if(count === 5){
        count = 0
    }else{
        count += 1
    }
}

let native = ["https://res.cloudinary.com/simpleview/image/upload/v1544569460/clients/scottsdale/Hopi_Dancers_on_Feast_Days_499de77f-906e-4f95-9d05-cb1b90615900.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_U8OdWqB320JZdJHHrcrzMICGE2gautlzaA&s", "https://ndcfs.org/wp-content/uploads/2024/09/navajo-nation-generations960.jpg", "https://www.uvu.edu/news/2023/11/images/2023_11_02_native_american_heritage_month_1.jpg", "", "", ""]
count = 0
function diff(){
    document.getElementById("three").style.height = "150px"
    document.getElementById("three").src = images[count]
    if(count === 6){
        count = 0
    }else{
        count += 1
    }
}