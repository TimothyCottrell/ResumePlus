
var selected = null;
var actions = [];

// Element declarations, yes there will be a ton :)
//
//var element = document.getElementById("elementName") - Example
var font_size = document.getElementById("font-size");
var left_align = document.getElementById("leftAlign");

// ---------------------- Event listeners --------------------------

// ---------------------- Logging Functions ------------------------
// Method to add an action to the log ;
// @param The the setting before being changed
// @param the new setting that the object is changed too
// @param the method used to change settings
function addAction(old_setting, new_setting, method){
  var info = {
    old_setting : old_setting,
    new_setting : new_setting,
    method : method,
    text : String(method.name) + " " + String(old_setting) + " -> " + String(new_setting)
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
function alignText(alignment){
  var item = selected;
  if (item == null || alignment > 3 || alignment < 0){
    console.log("ERROR | Invalid argument");
    return;
  }
  var old_setting = item.style.textAlign;
  switch(alignment){
    case 0:{
      item.style.textAlign = "left";
      break;
    }
    case 1:{
      item.style.textAlign = "center";
      break;
    }
    case 2:{
      item.style.textAlign = "right";
      break;
    }
  }
  var new_setting = item.style.textAlign;
  var method = alignText;
  addAction(old_setting, new_setting, method);
}

function fontsize(size){
  item = selected;
  var old_setting = item.style.fontSize;
  item.style.fontSize = size.toString() + "px";
  var new_setting = item.style.fontSize;
  var method = fontsize;
  addAction(old_setting, new_setting, method);
}

function changeText(item,text){
  var old_text = item.innerHTML;
  item.innerHTML = text;
  var new_text = text;
  addAction(old_text, new_text, changeText);
}

function updateSettings(){

}

function selectItem(ev){
  var item = ev.target;
  if (selected != null){
    selected.style.border = "None";
  }
  if (item == selected){
    selected.style.border = "None";
    selected = null;
    return;
  }
  selected = item;
  selected.style.border = "dotted red";
  if (selected.innerText != null){
    box = document.getElementById("text-search");
    box.value = selected.innerText;
  }
}

function hoverItem(ev){
  ev.target.style.border = "1px dotted grey"
}

function hoverEnd(ev){
  if (ev.target != selected){
    ev.target.style.border = "None";
  }

}



function handleDrop(e){
  e.stopPropagation();
  var node = document.getElementById(e.dataTransfer.getData('text'));
  var clone = node.cloneNode();
  console.log((((e.target.getBoundingClientRect().bottom - e.target.getBoundingClientRect().top) / 2) + e.target.getBoundingClientRect().top));
  console.log(e.y);
  if ( (((e.target.getBoundingClientRect().bottom - e.target.getBoundingClientRect().top) / 2) + e.target.getBoundingClientRect().top) < e.y) {
    var newItem = document.createElement(e.target.tagName);
    newItem.appendChild(clone);
    e.target.appendChild(newItem);
  } else {
    var newItem = document.createElement(e.target.tagName);
    newItem.appendChild(clone);
    e.target.parentElement.insertBefore(newItem, e.target);
  }
}

function handleDragOver(e){
  if (e.preventDefault){
    e.preventDefault();
  }
}

function handleDragStart(e){
  e.dataTransfer.effectAllowed = "copy";
  console.log(this);
  e.dataTransfer.setData('text', this.id);
}

function handleDragEnter(e){
  //this.appendChild(e.dataTransfer.getData('text/html'));
  console.log(this);
}

function handleDragLeave(e){
  //this.removeChild(e.dataTransfer.getData('text/html'));
}

function deleteCur() {
  selected.remove();
  selected = null;
}

function loadTemplate(template){
  // first remove old things
  old_setting = document.getElementById("sheet").innerHTML;
  document.getElementById("sheet").innerHTML = template;
  new_setting = template;
  addAction(old_setting, new_setting, loadTemplate);
}

//----------------------- On-click events ----------------------------

window.onload = function(){


  // Aligment click functions
  document.getElementById("leftAlign").onclick = function(){
    if (selected != null){
      alignText(0);
    }
  }

  document.getElementById("centerAlign").onclick = function(){
    if (selected != null){
      alignText(1);
    }
  }

  document.getElementById("rightAlign").onclick = function(){
    if (selected != null){
      alignText(2);
    }
  }

  document.getElementById("font-size").onchange = function(){
    if (selected != null){
      fontsize(this.value);
    }
  }

  document.getElementById("text-search").onchange = function(e){
    if (selected != null){
        changeText(selected, document.getElementById("text-search").value)
    }
  }

  document.getElementById("heading-choice-one").addEventListener('dragstart', handleDragStart);
  document.getElementById("subheading").addEventListener('dragstart', handleDragStart);
  document.getElementById("body-text").addEventListener('dragstart', handleDragStart);






// Adds event listeners to the resume so that we can select items :3
  resume = document.getElementById("sheet");
  children = resume.children;

  for (var i = 0; i < children.length; i++){
    children[i].addEventListener('click', selectItem);
    children[i].addEventListener('dragover', handleDragOver);
    children[i].addEventListener('dragenter', handleDragEnter);
    children[i].addEventListener('dragleave', handleDragLeave);
    children[i].addEventListener('drop', handleDrop);
    children[i].addEventListener("mouseover", hoverItem);
    children[i].addEventListener("mouseout", hoverEnd);
  }

}
