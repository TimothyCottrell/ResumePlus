var selected = null;
// Element declarations, yes there will be a ton :)
//
//var element = document.getElementById("elementName") - Example
var font_size = document.getElementById("font-size");
var left_align = document.getElementById("left-align");

// ---------------------- Event listeners --------------------------
left_align.addEventListener("click", left_align_clicked)

//----------------------- On-click events ----------------------------
function left_align_clicked(){
  console.log("ALIGNTEXT");
}

left_align.addEventListener("click", left_align_clicked)
