(function() {
    // your page initialization code here
    // the DOM will be available here
    var array=Array.from(document.querySelectorAll(".table tbody tr td.rentals"))
    var element = Array.from(document.querySelectorAll(".table tbody tr td.rentals")).map(e =>e.getAttribute("id"));
    var set=new Set(element)
  arr=array.map(e =>{
        
        var flag= set.has(e.id);
        set.delete(e.id);
        if(flag==false)
         return e.parentNode.removeChild(e);
        })
    console.log(arr)
  
    
 })();
 
