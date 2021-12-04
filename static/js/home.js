
// Element declarations, yes there will be a ton :)
//
//var element = document.getElementById("elementName") - Example


// ----------------Opening and closing the left toolbar ------------------

// These variables keep track of each tabs status [true = open | false = closed]
var more = false;
var upload = false;
var templates = false;
var texts = false;
var elements = false;
var map = false;

//Open Features
function openTemplates() {
    document.getElementById("sidebar-popout-text").style.width = "0px";
    document.getElementById("sidebar-popout-element").style.width = "0px";
    document.getElementById("sidebar-popout-map").style.width = "0px";
    document.getElementById("sidebar-popout-upload").style.width = "0px";
    document.getElementById("sidebar-popout-more").style.width = "0px";
    document.getElementById("sidebar-popout-template").style.width = "250px";
    document.getElementById("sidebar-popout-template").style.paddingTop = "20px";
    document.getElementById("sidebar-popout-template").style.paddingRight = "10px";
}
function openTexts() {
    document.getElementById("sidebar-popout-template").style.width = "0px";
    document.getElementById("sidebar-popout-template").style.padding = "0px";
    document.getElementById("sidebar-popout-element").style.width = "0px";
    document.getElementById("sidebar-popout-map").style.width = "0px";
    document.getElementById("sidebar-popout-upload").style.width = "0px";
    document.getElementById("sidebar-popout-more").style.width = "0px";
    document.getElementById("sidebar-popout-text").style.width = "260px";
}
function openElements() {
    document.getElementById("sidebar-popout-template").style.width = "0px";
    document.getElementById("sidebar-popout-template").style.padding = "0px";
    document.getElementById("sidebar-popout-text").style.width = "0px";
    document.getElementById("sidebar-popout-map").style.width = "0px";
    document.getElementById("sidebar-popout-upload").style.width = "0px";
    document.getElementById("sidebar-popout-more").style.width = "0px";
    document.getElementById("sidebar-popout-element").style.width = "260px";
}
function openMap() {
    document.getElementById("sidebar-popout-template").style.width = "0px";
    document.getElementById("sidebar-popout-template").style.padding = "0px";
    document.getElementById("sidebar-popout-text").style.width = "0px";
    document.getElementById("sidebar-popout-element").style.width = "0px";
    document.getElementById("sidebar-popout-upload").style.width = "0px";
    document.getElementById("sidebar-popout-more").style.width = "0px";
    document.getElementById("sidebar-popout-map").style.width = "250px";
}
function openUpload() {
    document.getElementById("sidebar-popout-template").style.width = "0px";
    document.getElementById("sidebar-popout-template").style.padding = "0px";
    document.getElementById("sidebar-popout-text").style.width = "0px";
    document.getElementById("sidebar-popout-element").style.width = "0px";
    document.getElementById("sidebar-popout-map").style.width = "0px";
    document.getElementById("sidebar-popout-more").style.width = "0px";
    document.getElementById("sidebar-popout-upload").style.width = "250px";
}
function openMore() {
    document.getElementById("sidebar-popout-template").style.width = "0px";
    document.getElementById("sidebar-popout-template").style.padding = "0px";
    document.getElementById("sidebar-popout-text").style.width = "0px";
    document.getElementById("sidebar-popout-element").style.width = "0px";
    document.getElementById("sidebar-popout-map").style.width = "0px";
    document.getElementById("sidebar-popout-upload").style.width = "0px";
    document.getElementById("sidebar-popout-more").style.width = "250px";
}

//Close Features

function closeTemplates() {
    document.getElementById("sidebar-popout-template").style.width = "0px";
    document.getElementById("sidebar-popout-template").style.padding = "0px";
}
function closeTexts() {
    document.getElementById("sidebar-popout-text").style.width = "0px";
}
function closeElements() {
    document.getElementById("sidebar-popout-element").style.width = "0px";
}
function closeMap() {
    document.getElementById("sidebar-popout-map").style.width = "0px";
}
function closeUpload() {
    document.getElementById("sidebar-popout-upload").style.width = "0px";
}
function closeMore() {
    document.getElementById("sidebar-popout-more").style.width = "0px";
}


// For each tab if its closed we open it and close all others if open we close
function toggle_templates(){
  if (templates == true){
    closeTemplates();
    templates = false;
  }else{
    openTemplates();
    closeUpload();
    closeTexts();
    closeElements();
    closeMap();
    closeMore();
    templates = true;
  }
}

function toggle_texts(){
  if (texts == true){
    closeTexts();
    texts = false;
  }else{
    openTexts();
    closeUpload();
    closeTemplates();
    closeElements();
    closeMap();
    closeMore();
    texts = true;
  }
}

function toggle_elements(){
  if (elements == true){
    closeElements();
    elements = false;
  }else{
    openElements();
    closeUpload();
    closeTemplates();
    closeTexts();
    closeMap();
    closeMore();
    elements = true;
  }
}

function toggle_map(){
  if (map == true){
    closeMap();
    map = false;
  }else{
    openMap();
    closeUpload();
    closeTemplates();
    closeTexts();
    closeElements();
    closeMore();
    map = true;
  }
}

function toggle_upload(){
  if (upload == true){
    closeUpload();
    upload = false;
  }else{
    openUpload();
    closeMap();
    closeTemplates();
    closeTexts();
    closeElements();
    closeMore();
    upload = true;
  }
}

function toggle_more(){
  if (more == true){
    closeMore();
    more = false;
  }else{
    openMore();
    closeMap();
    closeTemplates();
    closeTexts();
    closeElements();
    closeUpload();
    more = true;
  }
}

// ---------------- END Opening and closing the left toolbar ------------------
console.log("Successfully loaded editor!")
