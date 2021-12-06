var selected = null;
var actions = [];

// Element declarations, yes there will be a ton :)
//
//var element = document.getElementById("elementName") - Example
var font_size = document.getElementById("font-size");
var left_align = document.getElementById("left-align");

// ---------------------- Event listeners --------------------------

// ---------------------- Logging Functions ------------------------
// Method to add an action to the log ;
// @param The the setting before being changed
// @param the new setting that the object is changed too
// @param the method used to change settings
function addAction(old_setting, new_setting, method){
  var info = {
    oldSetting : old_setting,
    new_setting : new_Setting,
    method : method,
    text : string(method) + string(oldSetting) + " -> " + string(new_setting)
  };
  console.log(info.text);
  actions.push(info);
}

function undo(action){
  action.method(action.oldSetting);
  actions.remove(actions.length - 1);
}

function getLastAction(){
  return actions[actions.length - 1];
}



function getLog(){
  return actions;
}

// ---------------------- Common Functions --------------------------
// Function to align text object
// @param item is the text item to align
// @param alignment [0,1,2]
// @return None
function alignText(item, alignment){
  if (item == null || alignment > 3 || alignment < 0){
    console.log("ERROR | Invalid argument")
    return;
  }
  old_setting = item.style.textAlign;
  switch(alignment){
    case 0:{
      item.style.textAlign("left");
      break;
    }
    case 1:{
      item.style.textAlign("center");
      break;
    }
    case 2:{
      item.style.textAlign("right");
      break;
    }
  }
  var new_setting = item.style.textAlign
  var method = alignText;
  addAction(old_setting, new_setting, method);
}

function changeText(item,text){
  var old_text = item.innerHTML;
  var item.innerHTML = text;
  var new_text = text;
  addAction(old_text, new_text, changetext);
}

//----------------------- On-click events ----------------------------
left_align.onclick = function left_align_clicked(){
  if (selected != null){
    alignText(left_align, 0);
  }
}

left_align.addEventListener("click", left_align_clicked)
