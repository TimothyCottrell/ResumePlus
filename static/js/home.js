
var selected = null;
var actions = [];

// Element declarations, yes there will be a ton :)
//
//var element = document.getElementById("elementName") - Example
var font_size = document.getElementById("font-size");
var left_align = document.getElementById("leftAlign");

// ---------------------- Event listeners --------------------------

// ---------------------- Logging Functions ------------------------
// Method to add an action to the log
// @param The the setting before being changed
// @param the new setting that the object is changed too
// @param the method used to change settings
function addAction(old_setting, new_setting, method){
  var info = {
    item : selected,
    old_setting : old_setting,
    new_setting : new_setting,
    method : method,
    text : String(method.name) + " " + String(old_setting) + " -> " + String(new_setting)
  };
  console.log(info.text);
  actions.push(info);
}

function undo(){
  console.log(actions);
  var action = actions.pop();
  console.log(actions);
  selected = action.item;
  action.method(action.old_setting);
  actio.pop();
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
  item.style.textAlign = alignment;
  var new_setting = item.style.textAlign;
  var method = alignText;
  addAction(old_setting, new_setting, method);
}

function fontsize(size){
  var old_setting = selected.style.fontSize.substr(0, selected.style.fontSize.length - 2);
  selected.style.fontSize = size.toString() + "px";
  var new_setting = size.toString();
  var method = fontsize;
  addAction(old_setting, new_setting, method);
}

function changeText(item, text){
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
  if (ev.target != selected){
    ev.target.style.border = "1px dotted grey";
  }
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
  // console.log(this);
  e.dataTransfer.setData('text', this.id);
}

function handleDragEnter(e){
  //this.appendChild(e.dataTransfer.getData('text/html'));
  // console.log(this);
}

function handleDragLeave(e){
  //this.removeChild(e.dataTransfer.getData('text/html'));
}

function create(item){
  console.log(item);
}

function deleteCur(undo) {
  if (undo != null){
<<<<<<< HEAD
    create(undo)
=======
    create(undo);
>>>>>>> timain
  }
  if (selected != null && undo == null){
    old_setting = selected;
    new_setting = selected.parent;
    method = deleteCur;
    selected.remove();
    selected = null;
    addAction(old_setting,new_setting,method);
  }

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
      alignText("left");
    }
  }


  document.getElementById("centerAlign").onclick = function(){
    if (selected != null){
      alignText("center");
    }
  }

  document.getElementById("rightAlign").onclick = function(){
    if (selected != null){
      alignText("right");
    }
  }

  document.getElementById("font-size").onchange = function(){
    if (selected != null){
      fontsize(this.value);
    }
  }

  document.getElementById("text-search").onchange = function(e){
    if (selected != null){
      changeText(selected, document.getElementById("text-search").value);
    }
  }
  document.getElementById("undo").addEventListener("click", undo)
  document.getElementById("delete").addEventListener("click", deleteCur);

  document.getElementById("heading-choice-one").addEventListener('dragstart', handleDragStart);
  document.getElementById("subheading").addEventListener('dragstart', handleDragStart);
  document.getElementById("body-text").addEventListener('dragstart', handleDragStart);
  var videos = document.getElementById("videos").children;
  for (var i = 0; i < videos.length; i++){
    videos[i].setAttribute('id', 'video' + String(i));
    videos[i].addEventListener('dragstart', handleDragStart);
  }

// Adds event listeners to the resume so that we can select items :3
  resume = document.getElementById("sheet");
  children = resume.children;
  resume.addEventListener('drop', handleDrop);
  resume.addEventListener('dragover', handleDragOver);
  resume.addEventListener('dragenter', handleDragEnter);
  resume.addEventListener('dragleave', handleDragLeave);
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
