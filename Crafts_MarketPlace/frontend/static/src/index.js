function sortByRating(){
    var box = document.getElementById('box')
    var tempBox = box
    var children = tempBox.children
    for(i = 0; i < children.length;i++){
        for(j=0;j<children.length-1;j++){
            if(Number(children[j].children[5].innerHTML) < Number(children[j+1].children[5].innerHTML) ){
                tempChild = children[j]
                tempChild1 = children[j+1]
                children[j].replaceWith(children[j+1])
                tempBox.appendChild(tempChild)
            }
            // console.log(tempBox.children.length);
        }
    }
    // console.log(children);
    document.getElementById("ougterBox").appendChild(tempBox)
    // console.log("Hello");
}
function sortByPriceLimit(maxPrice){
    var box = document.getElementById('box')
    var tempBox = box
    var children = tempBox.children

    for(i = 1; i <= children.length;i++){
        var btn = document.getElementById('btn'+i)
        price = btn.innerText.substring(8,btn.innerText.length-1)
        if(price.includes(',') > 0){
            price = price.replace(',','')
        }
        if(Number(price) > Number(maxPrice)){
            var product = document.getElementById(''+i)
            product.remove()
        }
    }
    sortByRating();
}



